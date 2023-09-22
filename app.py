from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hello World!'

@app.route('/show_players')
def show_players():
    return "<h1><font color='red'><b>Tu będzie lista wszystkich zawodników</b></font></h1>"
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True,port=80)

#60. Dodaj do aplikacji ekran /show_players który
#będzie wyświetlał jakiś tekst. Przetestuj działanie.

#61. Zadbaj o to by każdy ekran miał swój plik html i wyświetlał go przy
#wejściu na dany adres