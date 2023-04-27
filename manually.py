import sqlite3

list_ = [('Claudete'),
	('Claudemir'),
	('Kauê'),
	('Yasmin'),
	('Indaia'),
	('Jaqueline (Prima Wendrew)'),
	('Evandro'),
	('Tia Fátima'),
	('Tio Nei'),
	('Bruna Patrícia'),
	('Rildo'),
	('Emília'),
	('Vinicius Elias'),
	('Tio Elias'),
	('Tia Cila'),
	('Lucia'),
	('Rodrigo'),
	('Nete'),
	('Diva'),
	('Celina'),
	('Bruno Silva Souza'),
	('Italo'),
	('Carol'),
	('Matheus Mendes'),
	('Luan'),
	('Vitória'),
	('Jaqueline Leite de Oliveira'),
	('Alan Buffalo Ferreira'),
	('Gabriel (Sabão)'),
    ('Cláudio'),
    ('Denise'),
    ('Madalena'),
    ('Antônio'),
    ('Tio Mateus'),
    ('Tia Carol'),
    ('Larissa'),
    ('Thales'),
    ('Angelia '),
    ('Tia Nim'),
    ('Valdemar'),
    ('Leonardo'),
    ('Karen'),
    ('Marcela'),
    ('Julian'),
    ('Isabelli'),
    ('Katiane'),
    ('Baltazar'),
    ('Maryana'),
    ('Tia Irani'),
    ('Maria Eduarda'),
    ('João Pedro'),
    ('Natália Mariana'),
    ('Samuel'),
    ('Marcus Vinicius '),
    ('Ingrid'),
    ('Tio Fernando'),
    ('Alessandra'),
    ('Brenda'),
    ('Tio Cidão '),
    ('Tia Rosângela'),
    ('Matheus Bernardino'),
    ('Jenny'),
    ('Jean Daniel'),
    ('Isabel'),
    ('Ana Júlia'),
    ('Isabelly'),
    ('Thiago Bernardino'),
    ('Luciane'),
    ('Gaby'),
    ('Tia Isabel'),
    ('Camila'),
    ('Chaiane'),
    ('Oscar '),
    ('Giovana Rotta'),
    ('Bruno'),
    ('Simone'),
    ('Maria Isabella'),
    ('Sandra'),
    ('Ana Lúcia'),
    ('Marisa Carvalho'),
    ('Débora Barbosa'),
    ('Daiane '),
    ('Neusa'),
    ('Marcelo'),
    ('Matheus '),
    ('Nicolas Duran'),
    ('Raissa Barrado'),
    ('Marcia Barrado'),
    ('Renato Antonieti '),
    ('Carolina Fiales'),
    ('Helen '),
    ('Bruna Malaspina '),
    ('Rodrigo Carone'),
    ('Rafael Mendes'),
    ('Mariana Azevedo'),
    ('Tiago Eliezer '),
    ('Maria Eduarda Azevedo'),
    ('Luan Valente'),
    ('Tati Olin'),
    ('Maria Estela'),
    ('Ana Caroline'),
    ('Giovanna Flausino'),
    ('Jonathan Fernandes'),
    ('Karina Baroni'),
    ('Julia Costa'),
    ('Sofia Medeiros'),
    ('Luis Felipe Paes'),
    ('Caíque Paneguti'),
    ('Bianca Figueira'),
    ('Alessandra Bernardes'),
    ('Pedro Alonso'),
    ('Gustavo Leal '),
    ('Priscila Santana'),
    ('Isabella')]

#create a data structure
conn = sqlite3.connect('instance/rsvp.sqlite3')
c = conn.cursor()

#Insert links into table
def data_entry():
    for item in list_:
        c.execute("INSERT INTO people (name) VALUES(?)", (item,))
    conn.commit()

data_entry()  # ==> call the function

#query database
c.execute("SELECT * FROM people")
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()