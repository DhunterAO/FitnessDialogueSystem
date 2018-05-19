from flask import Flask, send_file, request
from main import answer

app = Flask('__name__')


@app.route('/', methods=['GET', 'POST'])
def index():
    return send_file('test.html')


@app.route('/input', methods=['POST'])
def answer_question():
    question = request.form.get('question')
    print(question)
    return answer(question)


@app.route('/<static_file>', methods=['GET'])
def return_js(static_file):
    return send_file(static_file)


if __name__ == '__main__':
    app.run()
