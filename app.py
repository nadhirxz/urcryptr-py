from flask import Flask, render_template
from flask_socketio import SocketIO
import hashlib

SECRET_KEY = "random secret key"


def cipher(m, u, k):
	key = hashlib.pbkdf2_hmac('sha256', bytes(k, encoding='utf-8'), bytes(SECRET_KEY, encoding='utf-8'), 500, dklen=len(u))
	if (m == 0):
		u = bytes(u, encoding='utf-8')
		v = [x ^ y for (x, y) in zip(u, key)]
		b = bytearray(v).hex()
	else:
		u = bytes.fromhex(u)
		v = [chr(x ^ y) for (x, y) in zip(u, key)]
		b = "".join(i for i in v)
	return b


app = Flask("__name__")
socket = SocketIO(app)


@app.route('/')
def home():
	return render_template('index.html')


@socket.on("input")
def msg(data):
	try:
		v = cipher(data['method'], data['text'], data['key'])
		print(data['key'])
		socket.emit("output", v)
	except:
		socket.emit("error")


if __name__ == "__main__":
	socket.run(app)
