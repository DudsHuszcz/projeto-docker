from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, Professor! A aplicação está rodando via Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
