from app import create_app
from waitress import serve
from dotenv import load_dotenv
import os

app = create_app()
load_dotenv()

if __name__ == "__main__":
     if os.getenv("ENVIRONMENT") == 'DEVELOPMENT':
          app.run(debug=True, ssl_context=('certs/certificate.pem', 'certs/private.pem'), host='0.0.0.0', port=443)
     else:
          serve(app, host='0.0.0.0', port=8000, url_scheme='http')
