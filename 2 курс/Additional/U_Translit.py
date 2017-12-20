from flask import Flask
from flask import url_for, render_template, request, redirect
import urllib.request
import re
import json
import requests

app = Flask(__name__)


@app.route('/index')
def index():
    urls = {'Главная': url_for('index'),
           'transliteration': url_for('transliteration'),
           'Тест': url_for('test'),
           'result': url_for('result'),
           'Новостной сайт': url_for('news')}
    
    s_city = "Skopje,MK"
    appid = "c1dd72e84406fad58c65a4baf83e19d7"
    response = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = response.json()
    conditions = data['weather'][0]['description']
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    return render_template('index.html', urls=urls, conditions=conditions, temp=temp, temp_min=temp_min,temp_max=temp_max)


@app.route('/transliteration')
def transliteration():
    translit_wr = {}
    answer = ''
    with open('dict_.csv', 'r', encoding='utf-8') as file:
        for lines in file:
            lines = lines[0:-1]
            line = lines.split('\t')
            translit_wr[line[1]] = line[3]
    with open('user_word.txt', 'w+', encoding='utf-8') as file:
        file.write(json.dumps(request.args['word'], ensure_ascii=False, indent = 4))
        for line in file.read():
            if line.lower() == translit_wr[key].lower():
                answer = translit_wr[value]
    return render_template('transliteration.html', answer=answer)


@app.route('/news')
def news():
    commonUrl = 'https://lenta.ru/'
    regex = re.compile('[А-Яа-яЁё]+', flags = re.DOTALL)   
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    req = urllib.request.Request(commonUrl, headers = {'User-Agent':user_agent})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        words = re.search(regex, html)
        with open('user.txt', 'a', encoding='utf-8') as file:
            file.write(words)     
    return('news.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/result')
def result():
    num_right = 0
    num_wrong = 0
    
    with open('user_answers.txt', 'w+', encoding='utf-8') as file:
        file.write(json.dumps(request.args['april'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['pale'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['brown'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['maiden'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['beast'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['laziness'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['copper'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['unleavened'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['gray'], ensure_ascii=False, indent = 4) + '\n')
        file.write(json.dumps(request.args['be'], ensure_ascii=False, indent = 4) + '\n')

    with open('user_answers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            l = line.find('1')
            if l > -1:
                num_right += 1
            else:
                l = line.find('2')
                if l > -1:
                    num_wrong += 1
    return render_template('result.html', num_right=num_right, num_wrong=num_wrong)


if __name__ == '__main__':
    app.run(debug=True)
    






                
