from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def times():
    now = datetime.now()  # Получаем текущее время
    time = now.strftime("%d-%m-%Y %H:%M:%S")  # Форматируем время
    return f"<h1>Текущая дата и время:</h1><p>{time}</p>"


if __name__ == '__main__':
    app.run(debug=True)

