
from flask import Flask, render_template, request
import requests
import csv

app = Flask(__name__)



def geocode(phone)->str:
    parameters = {'phone':phone,'key': 'e4c7e9009404fa14d3d26e3a0606f69c'}
    base = 'http://apis.juhe.cn/mobile/get'
    response = requests.get(base, parameters)
    answer = response.json()
    return str(answer['result'])

def geocode1(names):
    with open('records_a.csv') as data:
        for x in data:
            c = str(x[12:15].strip(','))
            b = str(names)
            if b == c:
                return str(x)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phone = request.form['phonenumber']
    title = '这是查询结果:'
    results = geocode(phone)
    return render_template('results.html',
                            the_title=title,
                            the_phonenumber=phone,
                            the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎使用上午班python手机号归属地查询网站')


if __name__ == '__main__':
    app.run(debug=True)
