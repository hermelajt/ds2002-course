import os
from pymongo import MongoClient

# Read Atlas environment variables
MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")


def main():

    # Build connection string
    uri = f"{MONGODB_ATLAS_URL}"

    # Connect to MongoDB Atlas
    client = MongoClient(uri, username=MONGODB_ATLAS_USER, password=MONGODB_ATLAS_PWD)

    # Select database and collection
    db = client["bookstore"]
    authors = db["authors"]

    # Total number of authors
    total = authors.count_documents({})
    print(f"\nTotal authors: {total}\n")

    # Print report of authors
    for author in authors.find({}, {"_id": 0, "name": 1, "nationality": 1, "birthday": 1}):
        print(f"Name: {author.get('name')}")
        print(f"Nationality: {author.get('nationality')}")
        if "birthday" in author:
            print(f"Birthday: {author.get('birthday')}")
        print("-" * 30)

    # Close connection
    client.close()


if __name__ == "__main__":
    main()