from flask import Flask,render_template

app = Flask(__name__)

class Player:
    def __init__(self,id,fn,ln):
        self.id=id
        self.first_name=fn
        self.last_name=ln
    def __str__(self):
        return str(self.__dict__)

def get_players_all():
    return [
        Player(1,'Andrzej','Klusiewicz'),
        Player(2,"Druga",'Osoba'),
        Player(3, "Trzecia","Osoba")

    ]

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/show_players')
def show_players():
    # for p in get_players_all():
    #     print(p)
    return render_template("show_players.html",players=get_players_all())
@app.route('/about')
def about():
    used_languages=['Python','HTML','CSS','JavaScript']
    return render_template("about.html",first_name="Andrzej",last_name="Klusiewicz",langs=used_languages)


if __name__ == '__main__':
    app.run(debug=True,port=80)

#60. Dodaj do aplikacji ekran /show_players który
#będzie wyświetlał jakiś tekst. Przetestuj działanie.

#61. Zadbaj o to by każdy ekran miał swój plik html i wyświetlał go przy
#wejściu na dany adres

#klusiewicz@jsystems.pl