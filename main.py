# Импорт
from flask import Flask, render_template

# Создание объекта приложения Flask
app = Flask(__name__)

# Функция для расчета результатов
def result_calculate(size, lights, device):
    # Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Первая страница
@app.route('/')
def index():
    return render_template('index.html')

# Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

# Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Расчет
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    result = result_calculate(int(size), int(lights), int(device))
    return render_template('end.html', result=result)

# Новый маршрут для экологичной сборки
@app.route('/<size>/<lights>/our_eco_build')
def our_eco_build(size, lights):
    # Добавьте логику для страницы с экологичной сборкой здесь
    return render_template('our_eco_build.html', size=size, lights=lights)

# Запуск приложения в режиме отладки
app.run(debug=True)


<!-- lights.html -->
<!doctype html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
  >
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="../static/css/style.css">
  <title>Расчет энергоэффективности умного дома</title>
</head>
<body>
  <header class="header">
    <div class="header__text">
      <h1>Расчитай энергоэффективность своего дома!</h1>
      <p>Реши проблему излишнего электропотребления самостоятельно!</p>
    </div>
  </header>
  <main>
    {% block content %}
    <h2 class="main__title">Выбери освещение:</h2>
    <ul class="list" id="list">
      <li class="list__item">
        <a href="{{size + '/3' }}">
          <img class="item__img" src="../static/img/light.svg" alt="light">
          <span>2-4 лампочки</span>
        </a>
      </li>
      <!-- Задание №2 -->
      <li class="list__item">
        <a href="{{size + '/7' }}">
          <img class="item__img" src="../static/img/light.svg" alt="light">
          <span>4-6 лампочек</span>
        </a>
      </li>
      <li class="list__item">
        <a href="{{size + '/10' }}">
          <img class="item__img" src="../static/img/light.svg" alt="light">
          <span>8 и более</span>
        </a>
      </li>
      <!-- New button for eco-friendly build -->
      <li class="list__item">
        <a href="{{size + '/our_eco_build' }}">
          <img class="item__img" src="YOUR_ECO_IMAGE_URL" alt="Eco Build">
          <span>Наша экологичная сборка</span>
        </a>
      </li>
    </ul>
    {% endblock %}
  </main>
  <footer>
    <!-- Your footer content goes here -->
  </footer>
</body>
</html>

