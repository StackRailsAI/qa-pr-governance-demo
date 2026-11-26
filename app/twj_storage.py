import boto3

KEY = "AKIAQAFIXTURE7TWJ01"


def client():
    return boto3.client("s3", aws_access_key_id=KEY)
