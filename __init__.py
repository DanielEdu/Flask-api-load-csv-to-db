from flask import render_template, request, redirect
import pandas as pd
from flask_app.config import init_app
from flask_app.sql.queries import sql
from flask_app.models.Hired_employees import Hired_employees
from flask_app.models.Jobs import Jobs


app, db, conn = init_app()


class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50))
    insert_date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        seleccion = request.form['mi_combobox']
        print(seleccion)
        if file:
            df = pd.read_csv(file)
            for index, row in df.iterrows():
                if seleccion == 'hired_employees':
                    new_row = Hired_employees(
                        id=row['id'], 
                        name=row['name'], 
                        datetime=row['datetime'], 
                        department_id=row['department_id'], 
                        job_id=row['job_id']
                        )
                elif seleccion == 'departments':
                    new_row = Departments(id=row['id'], department=row['department'])
                elif seleccion == 'jobs': 
                    new_row = Jobs(id=row['id'], job=row['job'])
                db.session.add(new_row)
            db.session.commit()
        return f'Archivo cargado correctamente el la tabla {seleccion}'
    
    return render_template('upload.html')


@app.route('/query1')
def query1():

    cur = conn.cursor()
    cur.execute(sql["q1"])
    result = cur.fetchall()
    conn.close()

    return render_template('query1.html', result=result)


@app.route('/query2')
def query2():
    cur = conn.cursor()
    cur.execute(sql["q2"])
    result = cur.fetchall()
    conn.close()
    
    return render_template('query2.html', result=result)