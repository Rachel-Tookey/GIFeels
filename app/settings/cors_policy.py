cors_resource = {

    r"/*": {"origins": ["https://127.0.0.1:8443", "https://www.googleapis.com/", "http://127.0.0.1:8443"],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
            }
}