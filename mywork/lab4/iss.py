#!/usr/bin/env python3

"""
iss.py - ETL pipeline to track the International Space Station (ISS) location over time.
"""

import sys
import os
import json
import logging
from datetime import datetime, timezone

import requests
import pandas as pd


def init_logger() -> logging.Logger:
    """Initialize a console logger."""
    logger = logging.getLogger("iss_etl")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if reloaded
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
def extract(logger: logging.Logger) -> dict:
    """
    Extract: Download the JSON data from the ISS Location Now API.
    Returns the parsed JSON record (dict). Handles errors gracefully.
    """
    url = "http://api.open-notify.org/iss-now.json"
    logger.info("Extract: requesting %s", url)

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        # Optional: save raw JSON so you can inspect structure
        with open("iss_raw.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        logger.info("Extract: received message=%s", data.get("message"))
        return data

    except requests.RequestException as e:
        logger.error("Extract: request failed: %s", e)
        return {}

    except ValueError as e:
        logger.error("Extract: JSON parse failed: %s", e)
        return {}

def transform(record: dict, logger: logging.Logger) -> pd.DataFrame:
    """
    Transform: Convert extracted JSON dict into a single-row pandas DataFrame.
    Converts UNIX timestamp (seconds) into YYYY-MM-DD HH:MM:SS (UTC).
    """
    logger.info("Transform: converting record to tabular format")

    if not record:
        logger.warning("Transform: empty record; returning empty DataFrame")
        return pd.DataFrame()

    try:
        ts = int(record["timestamp"])
        pos = record["iss_position"]
        lat = float(pos["latitude"])
        lon = float(pos["longitude"])

        dt_utc = datetime.fromtimestamp(ts, tz=timezone.utc)
        ts_str = dt_utc.strftime("%Y-%m-%d %H:%M:%S")

        df = pd.DataFrame([{
            "timestamp_unix": ts,
            "timestamp_utc": ts_str,
            "latitude": lat,
            "longitude": lon
        }])

        logger.info("Transform: produced 1 row")
        return df

    except Exception as e:
        logger.error("Transform: failed: %s", e)
        return pd.DataFrame()
def load(df: pd.DataFrame, csv_file: str, logger: logging.Logger) -> None:
    """
    Load: Append the passed single-row DataFrame to the specified CSV file.
    Creates the file if it doesn't exist; appends otherwise.
    """
    if df is None or df.empty:
        logger.warning("Load: nothing to write (empty DataFrame)")
        return

    try:
        file_exists = os.path.exists(csv_file)
        df.to_csv(csv_file, mode="a", header=not file_exists, index=False)
        logger.info("Load: appended %d row(s) to %s", len(df), csv_file)
    except Exception as e:
        logger.error("Load: failed: %s", e)


def main() -> int:
    """
    Orchestrate the ETL pipeline: extract -> transform -> load.
    Script accepts one command-line argument: output CSV filename.
    """
    logger = init_logger()

    if len(sys.argv) != 2:
        logger.error("Usage: python3 iss.py <output_csv_file>")
        return 2

    csv_file = sys.argv[1]
    logger.info("Starting ISS ETL; output=%s", csv_file)

    record = extract(logger)
    df = transform(record, logger)
    load(df, csv_file, logger)

    logger.info("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

