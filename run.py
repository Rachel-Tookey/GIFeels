from app import create_app
import os
from socket import gethostname
from settings import Config

app = create_app(config_class=Config)

if __name__ == "__main__":
    app.run(debug=True, ssl_context=('certs/certificate.pem', 'certs/private.pem'), host='0.0.0.0', port=443)
