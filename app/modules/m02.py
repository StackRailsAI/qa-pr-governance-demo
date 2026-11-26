def handler_02(payload):
    """Synthetic module 02 for the 30-file PR timing check."""
    return {"module": 2, "size": len(payload or [])}
