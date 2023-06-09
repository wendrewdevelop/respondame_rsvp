from flask import (
    Flask, 
    render_template, 
    request, 
    flash, 
    redirect, 
    url_for, 
    Response,
    make_response,
    send_file,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from datetime import date
import os
import psycopg2
from io import StringIO


app = Flask(__name__)
db = SQLAlchemy()
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rsvp.sqlite3"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hcddwknagsewew:0b9d74dd199f8820658a021e036f0bf6d3a2180718194ffb95ceb232b8ef12a6@ec2-52-21-233-246.compute-1.amazonaws.com/dbbf0e2lhbsq33"
app.config['SECRET_KEY'] = "shutupandtakemymoney"
db.init_app(app)

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

class Confirmed(db.Model):
    __tablename__ = 'confirmed'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    confirmated_at = db.Column(db.String, nullable=True)

    def __init__(self, name, confirmated_at):
        self.name = name
        self.confirmated_at = confirmated_at


@app.route("/", methods=['GET', 'POST'])
def confirmation():
    search = request.args.get("search")
    confirmated = db.session.query(
        Confirmed.name.label("name")
    )
    query = db.session.query(
        People.name.label("name"),
        People.id.label("id")
    ).filter(
        People.name.notin_(confirmated)
    )
    if search:
        query = query.filter(People.name.ilike(f'%{search}%'))
    query = query.all()

    if request.method == 'POST':
        db.session.add(Confirmed(
            name=request.form['people_name'],
            confirmated_at=date.today().strftime('%d-%m-%Y')
        ))
        db.session.commit()
        return redirect(url_for('confirmation_success'))
        
    return render_template('index.html', query=query)


@app.route("/confirmation")
def confirmation_success():
    return render_template('confirmation.html')


@app.route("/<lista_presenca>", methods=['GET', 'POST'])
def confirmation_export(lista_presenca):
    output = StringIO()
    if request.view_args['lista_presenca'] == 'confirmados':
        confirmations = db.session.query(
            People.name.label("Nome"),
            People.confirmated_at.label("Confirmadoem")
        ).filter(
            People.confirmation==True
        ).all()
        return render_template('confirmados.html', confirmations=confirmations)
    elif request.view_args['lista_presenca'] == 'naoconfirmados':
        notconfirmations = db.session.query(
            People.name.label("Nome")
        ).filter(
            People.confirmation==False
        ).all()
        return render_template('naoconfirmados.html', notconfirmations=notconfirmations)
    else:
        return """URL NÃO EXISTE!!!!!!"""

if __name__ == '__main__':
    # https://respondame-app.herokuapp.com/ | https://git.heroku.com/respondame-app.git
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5050)
