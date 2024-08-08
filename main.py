from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message='Hello, my name is Urangoo')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    return render_template('news.html')   

@app.route('/form', methods=['GET', 'POST'])
def form():
    message = ''
    if request.method == 'POST':
        text = request.form.get('text')
        if request.form['submit_button'] == 'Lowercase':
            message = text.lower()
        elif request.form['submit_button'] == 'Capital':
            message = text.upper()
        elif request.form['submit_button'] == 'Urangoo':
            message = "Hi Urangoo"

        elif request.form['submit_button'] == 'Count Words':
            word_counts = len(text.split())
            message = f"there are {word_counts} word in the text"
    return render_template('form.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
