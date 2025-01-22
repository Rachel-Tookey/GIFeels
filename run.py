from app import create_app

app = create_app()

if __name__ == "__main__":
    # HTTPS: app.run(debug=True, ssl_context=('certs/certificate.pem', 'certs/private.pem'), host='0.0.0.0', port=8443)
     app.run(debug=True, host='0.0.0.0', port=8443)
