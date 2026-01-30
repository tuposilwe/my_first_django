from waitress import serve
from main.wsgi import application

if __name__ == '__main__':
    # Starts the server on port 8000
    serve(application, host='0.0.0.0', port='8000',threads=4)
