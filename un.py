from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def start_screen():
    return '<b>Миссия Колонизация Марса<b>'


@app.route('/index')
def index():
    return '<b>И на Марсе будут яблони цвести!<b>'


@app.route('/promotion')
def promotion():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <p>Человечество вырастает из детства.<p>
                    <p>Человечеству мала одна планета.<p>
                    <p>Мы сделаем обитаемыми безжизненные пока планеты.<p>
                    <p>И начнем с Марса!<p>
                    <p>Присоединяйся!<p>
                  </body>
                </html>'''


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                        <p>Вот она какая, красная планета</p>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
