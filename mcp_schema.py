from datetime import datetime

def build_mcp_response(context_type: str, data: dict):
    return {
        "type": "context_response",
        "timestamp": datetime.utcnow().isoformat(),
        "context_type": context_type,
        "data": data
    }

def build_mcp_error(message: str):
    return {
        "type": "context_error",
        "error": message,
        "timestamp": datetime.utcnow().isoformat()
    }
