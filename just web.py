from flask import Flask


app = Flask(__name__)

# Определяем функцию, которая будет обрабатывать GET запросы к корневому URL
@app.route("/")
def hello():
    return "Hello, World wide web!"

# Запускаем приложение на локальном сервере
if __name__ == "__main__":
    app.run()