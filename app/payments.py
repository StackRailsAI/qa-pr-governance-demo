import boto3


def payments_client():
    # Credentials come from the environment or the instance role.
    return boto3.client("s3")
