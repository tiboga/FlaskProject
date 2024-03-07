from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def now():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def countdown():
    countdown_list = """Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!""".split('\n')
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                <title>Привет, Марс!</title>
              </head>
              <body>
                <h1>Жди нас, Марс!</h1>
                <img src="{url_for('static', filename='img/MARS.png')}" 
                alt="здесь должна была быть картинка, но не нашлась">
                <p>ААААААААААААААААААААААААААААААА, Марс!</p>
              </body>
            </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />                
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>             
                    <h1>Какааааая планета</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-danger" role="alert">
                      Вери гууд планета
                    </div>
                    <div class="alert alert-success" role="alert">
                      Хороши планета
                    </div>
                    <div class="alert alert-info " role="alert">
                      Тре бьен планета
                    </div>
                    <div class="alert alert-warning " role="alert">
                        Сделаем плане2
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('astronaut_reg.html', data=url_for('static', filename='css/style2.css'))


@app.route('/choice/<planet_name>')
def planet(planet_name):
    return render_template('planet.html', planet=planet_name)


@app.route('/results/<nickname>/<level>/<rating>')
def selection(nickname, level, rating):
    return render_template('selection.html', nick=nickname, selection_stage=level, points=rating)


@app.route('/carousel')
def carousel():
    image1_url = url_for('static', filename='img/image1.jpg')
    image2_url = url_for('static', filename='img/image2.jpg')
    image3_url = url_for('static', filename='img/image3.jpg')
    image4_url = url_for('static', filename='img/image4.jpg')
    style = url_for('static', filename='css/style2.css')
    return render_template('carousel.html', im1=image1_url, im2=image2_url, im3=image3_url, im4=image4_url, style=style)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
