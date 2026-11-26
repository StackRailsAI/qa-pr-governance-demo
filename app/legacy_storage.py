import os


def legacy_storage_key():
    # Fake AWS documentation example key: the known violation a QA PR fixes.
    return os.environ.get("ORDERS_STORAGE_KEY", "AKIAIOSFODNN7EXAMPLE")
