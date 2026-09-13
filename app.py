from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Привет, DevOps!</h1>
    <p>Это моё первое приложение, собранное Jenkins'ом.</p>
    <p><b>Хост:</b> {hostname}</p>
    <p><b>Время:</b> {now}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
