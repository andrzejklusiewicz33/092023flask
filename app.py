from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hello World!'

@app.route('/about')
def about():
    return "Autorem tego programu jest Mapet który lubi pierogi i bigos"


if __name__ == '__main__':
    app.run(debug=True,port=80)

#60. Dodaj do aplikacji ekran /show_players który
#będzie wyświetlał jakiś tekst. Przetestuj działanie.