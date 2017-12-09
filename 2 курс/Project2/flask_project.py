from flask import Flask
from flask import url_for, render_template, request, redirect
import json
import urllib.request


app = Flask(__name__)


@app.route('/')
def index():
    urls = {'main_page': url_for('index'),
           'thank_user': url_for('thanks'),
           'statistics_data': url_for('stats'),
           'json_data': url_for('json'),
           'search_data': url_for('search'),
           'results_data': url_for('results')}
    return render_template('index.html', urls=urls)


@app.route('/thanks')
def thanks():
    with open('data.json', 'a', encoding='utf-8') as file:
        file.write(json.dumps(request.args, ensure_ascii=False, indent = 4))
    return render_template('thanks.html')

@app.route('/stats')
def statistics():
    listAge = []
    countGenderM = 0
    countGenderW = 0
    number = 0
    with open('data.json', 'r', encoding = 'utf-8') as file:
        data = json.loads(file.read())
        for key, value in data: 
            if key == 'age': 
                listAge.append(value)
                number += 1
            if key == 'gender':
                if value == 'male':
                    countGenderM += 1
                else:
                    countGenderW += 1

    stats = {'Минимальный возраст опрошенных': min(listAge),
            ' Максимальный возраст опрошенных': max(listAge),
             'Количество мужчин': 'countGenderM',
             'Количество женщин': 'countGenderW'}
    return render_template('stats.html', number=number, stats=stats)
            

@app.route('/json')
def data():
    json_list = []
    js = json.dump(request.args, ensure_ascii=False)
        json_list.append(js)
    return render_template('json.html', js = json_list)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/results')
def show_results():
    with open('data.json', 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        search_word = request.args
        results = []
        for result in data:
                if search_word in result:
                    results.append(result)
        if results == []:
            results.append('По Вашему запросу ничего не найдено' + '\n' + 'Попробуйте изменить входные данные')
        else:
            for idx, result in enumerate(results):
                results[idx] = str(indx+1) + ',' + result
    return render_template('results.html', results=results, word=word)


if __name__ == '__main__':
    app.run(debug=True)







































            
            
