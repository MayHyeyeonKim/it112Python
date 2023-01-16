from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result222')
def user_info(username):
    return render_template('result.html',
                           users=[
                               {
                                   "name": "Sara",
                                   "color": "red",
                                   "number": "1"
                               },
                               {},
                               {},
                           ])


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        userName = request.form['userName']
        color = request.form['color']
        number = request.form['number']
        print(userName)
        print(color)
        print(number)
        colors = {"red": "빨간", "green": "푸른", "blue": "파란", "yellow": "노란"}
        numbers = {"1": "하루", "2": "사과", "3": "바나나", "4": "키위", "5": "자몽"}
        fortune = f"{colors[color]} {numbers[number]}"
        return render_template('result.html',
                               user={
                                   "name": userName,
                                   "fortune": fortune,
                               })
    else:
        return "Handle GET request"


app.run(host='0.0.0.0', port=81)
