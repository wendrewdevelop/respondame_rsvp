import sqlite3
import os
import psycopg2


list_ = [('Claudete', False),
	('Claudemir', False),
	('Kauê', False),
	('Yasmin', False),
	('Indaia', False),
	('Jaqueline (Prima Wendrew)', False),
	('Evandro', False),
	('Tia Fátima', False),
	('Tio Nei', False),
	('Bruna Patrícia', False),
	('Rildo', False),
	('Emília', False),
	('Vinicius Elias', False),
	('Tio Elias', False),
	('Tia Cila', False),
	('Lucia', False),
	('Rodrigo', False),
	('Nete', False),
	('Diva', False),
	('Celina', False),
	('Bruno Silva Souza', False),
	('Italo', False),
	('Carol', False),
	('Matheus Mendes', False),
	('Luan', False),
	('Vitória', False),
	('Jaqueline Leite de Oliveira', False),
	('Alan Buffalo Ferreira', False),
	('Gabriel (Sabão)', False),
    ('Cláudio', False),
    ('Denise', False),
    ('Madalena', False),
    ('Antônio', False),
    ('Tio Mateus', False),
    ('Tia Carol', False),
    ('Larissa', False),
    ('Thales', False),
    ('Angelia ', False),
    ('Tia Nim', False),
    ('Valdemar', False),
    ('Leonardo', False),
    ('Karen', False),
    ('Marcela', False),
    ('Julian', False),
    ('Isabelli', False),
    ('Katiane', False),
    ('Baltazar', False),
    ('Maryana', False),
    ('Tia Irani', False),
    ('Maria Eduarda', False),
    ('João Pedro', False),
    ('Natália Mariana', False),
    ('Samuel', False),
    ('Marcus Vinicius ', False),
    ('Ingrid', False),
    ('Tio Fernando', False),
    ('Alessandra', False),
    ('Brenda', False),
    ('Tio Cidão ', False),
    ('Tia Rosângela', False),
    ('Matheus Bernardino', False),
    ('Jenny', False),
    ('Jean Daniel', False),
    ('Isabel', False),
    ('Ana Júlia', False),
    ('Isabelly', False),
    ('Thiago Bernardino', False),
    ('Luciane', False),
    ('Gaby', False),
    ('Tia Isabel', False),
    ('Camila', False),
    ('Chaiane', False),
    ('Oscar ', False),
    ('Giovana Rotta', False),
    ('Bruno', False),
    ('Simone', False),
    ('Maria Isabella', False),
    ('Sandra', False),
    ('Ana Lúcia', False),
    ('Marisa Carvalho', False),
    ('Débora Barbosa', False),
    ('Daiane ', False),
    ('Neusa', False),
    ('Marcelo', False),
    ('Matheus ', False),
    ('Nicolas Duran', False),
    ('Raissa Barrado', False),
    ('Marcia Barrado', False),
    ('Renato Antonieti ', False),
    ('Carolina Fiales', False),
    ('Helen ', False),
    ('Bruna Malaspina ', False),
    ('Rodrigo Carone', False),
    ('Rafael Mendes', False),
    ('Mariana Azevedo', False),
    ('Tiago Eliezer ', False),
    ('Maria Eduarda Azevedo', False),
    ('Luan Valente', False),
    ('Tati Olin', False),
    ('Maria Estela', False),
    ('Ana Caroline', False),
    ('Giovanna Flausino', False),
    ('Jonathan Fernandes', False),
    ('Karina Baroni', False),
    ('Julia Costa', False),
    ('Sofia Medeiros', False),
    ('Luis Felipe Paes', False),
    ('Caíque Paneguti', False),
    ('Bianca Figueira', False),
    ('Alessandra Bernardes', False),
    ('Pedro Alonso', False),
    ('Gustavo Leal ', False),
    ('Priscila Santana', False),
    ('Isabella', False)]

#create a data structure
#conn = sqlite3.connect('instance/rsvp.sqlite3')
conn = psycopg2.connect(
    host="ec2-3-232-218-211.compute-1.amazonaws.com",
    database="d39i5fkh1gbid",
    user="usyehuakcblsnj",
    password="418a91ad288ccecb68d02d9a745c92b022edfff5fae2890e1f4ed4e719477dbe",
    sslmode='require'
)
cur = conn.cursor()

cur.execute(
    'CREATE TABLE people (id serial PRIMARY KEY,'
    'name varchar (250) NOT NULL,'
    'confirmation boolean,'
    'confirmated_at varchar (250);'  
)

#Insert links into table
def data_entry():
    for item in list_:
        cur.execute("INSERT INTO people (name, confirmation) VALUES(%s, %s)", (item,))
    conn.commit()

data_entry()  # ==> call the function

#query database
cur.execute("SELECT * FROM people")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.commit()
cur.close()
conn.close()