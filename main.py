from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from datetime import date
import os
import psycopg2


app = Flask(__name__)
db = SQLAlchemy()
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rsvp.sqlite3"
app.config['SECRET_KEY'] = "shutupandtakemymoney"
db.init_app(app)

def get_db_connection():
    conn = psycopg2.connect(
        host="ec2-3-232-218-211.compute-1.amazonaws.com",
        database="d39i5fkh1gbid",
        user="usyehuakcblsnj",
        password="418a91ad288ccecb68d02d9a745c92b022edfff5fae2890e1f4ed4e719477dbe",
        sslmode='require')
    
    return conn

class People(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    confirmation = db.Column(db.Boolean, nullable=True, default=False)
    confirmated_at = db.Column(db.String, nullable=True)

    def __init__(self, name, confirmation, confirmated_at):
        self.name = name
        self.confirmation = confirmation
        self.confirmated_at = confirmated_at


@app.route("/", methods=['GET', 'POST'])
def confirmation():
    search = request.args.get("search")
    print(search)
    query = db.session.query(
        People.name.label("name"),
        People.id.label("id")
    ).filter(
        People.confirmation!=True
    )
    if search:
        query = query.filter(People.name.like(f'%{search}%'))
    query = query.all()

    print(query)

    peoples = request.form.getlist('people_name')
    confirmations = request.form.getlist('confirmation')
    for people, confirmation in zip(peoples, confirmations):
        print(people, confirmation)
        if request.method == 'POST':
            confirm = People.query.filter(
                People.name==people
            ).first()
            confirm.confirmation = True if confirmation == 'on' else False
            confirm.confirmated_at = date.today().strftime('%d-%m-%Y')
            db.session.commit()
            return redirect(url_for('confirmation_success'))
        
    return render_template('index.html', query=query)


@app.route("/confirmation")
def confirmation_success():
    return render_template('confirmation.html')


@app.route("/<lista_presenca>", methods=['GET', 'POST'])
def confirmation_export(lista_presenca):
    if request.view_args['lista_presenca'] == 'confirmados':
        confirmations = db.session.query(
            People.name.label("Nome"),
            People.confirmated_at.label("Confirmado em")
        ).filter(
            People.confirmation==True
        ).all()
        df = pd.DataFrame(confirmations)
        df.to_csv('confirmados.csv', index=False)
    elif request.view_args['lista_presenca'] == 'naoconfirmados':
        confirmations = db.session.query(
            People.name.label("Nome")
        ).filter(
            People.confirmation==False
        ).all()
        df = pd.DataFrame(confirmations)
        df.to_csv('nao_confirmados.csv', index=False)
    else:
        return """URL NÃO EXISTE!!!!!!"""

    
    return """
        Relatório gerado com sucesso!!
    """


if __name__ == '__main__':
    # https://respondame-app.herokuapp.com/ | https://git.heroku.com/respondame-app.git
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5050)
