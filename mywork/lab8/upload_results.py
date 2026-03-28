import boto3
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)

def parse_args():
    return sys.argv[1], sys.argv[2]

def upload(input_folder, destination):
    s3 = boto3.client('s3', region_name='us-east-1')

    bucket, prefix = destination.split('/', 1)

    try:
        for file in os.listdir(input_folder):
            if file.startswith("results") and file.endswith(".csv"):
                path = os.path.join(input_folder, file)
                s3.upload_file(path, bucket, prefix + file)
                logging.info(f"Uploaded {file}")
    except Exception as e:
        logging.error(e)

def main():
    input_folder, destination = parse_args()
    upload(input_folder, destination)
    logging.info("Done")

if __name__ == "__main__":
    main()
