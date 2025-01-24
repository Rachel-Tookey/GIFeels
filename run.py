from app import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
     #app.run(debug=True, ssl_context=('certs/certificate.pem', 'certs/private.pem'), host='0.0.0.0', port=443)
     serve(app, host='0.0.0.0', port=8000, url_scheme='http')
