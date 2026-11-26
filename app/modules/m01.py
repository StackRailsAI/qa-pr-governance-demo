def handler_01(payload):
    """Synthetic module 01 for the 30-file PR timing check."""
    return {"module": 1, "size": len(payload or [])}
