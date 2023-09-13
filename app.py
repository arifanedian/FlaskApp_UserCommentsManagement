from flask import Flask,render_template,request

app = Flask(__name__)

#homepage
@app.route('/')
def home():
    return render_template('home.html')

#aboutpage
@app.route('/about')
def about():
    return render_template('about.html')

#homepage
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submitdata', methods=['POST','GET'])
def submitdata():
    if request.method == 'GET':
        pass
    else:
        return render_template('submitdata.html',
                           email = request.form['useremail'],
                           ch1 = request.form['choice1'],
                           ch2 = request.form['choice2'],
                           comments = request.form['comment']
                           )

if __name__ == "__main__":
    app.run(debug=True)