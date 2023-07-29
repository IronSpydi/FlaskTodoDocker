from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv
import time
import os


app = Flask(__name__)
load_dotenv()


db_user = os.environ['DB_USERNAME']
db_pass = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_database = os.environ['DB_NAME']

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL',f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_database}")

db = SQLAlchemy(app)



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    start_date_time = db.Column(db.DateTime)
    end_date_time = db.Column(db.DateTime)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'
    
    def validate(self):
        if self.start_time > self.end_date_time:
            raise ValueError("satrt date time should not grater than end date time")
    
    def before_insert(self):
        self.validate()

    def before_update(self):
        self.validate()


with app.app_context():
    db.create_all()
@app.route('/')
def home():
    return redirect('/api')

@app.route('/api', methods=['POST','GET'])
def task_manager():
    if request.method == 'POST':
        task_content = request.form['content']
        task_start_date_time = request.form['start_date_time']
        task_end_date_time = request.form['end_date_time']
        task_completed = request.form['completed']
        new_task = Todo(content = task_content,start_date_time = task_start_date_time, end_date_time=task_end_date_time,completed = task_completed)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/api')
        except Exception as error:
            return f"error occured while adding task: {error}"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks = tasks)

@app.route('/api/delete/<int:id>')
def delete_taks(id):
    try:
        task = Todo.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return redirect('/api')
    except Exception as error:
        return f"error occured while deleting task: {error}"
    
@app.route('/api/update/<int:id>',methods = ['GET','POST'])
def update_task(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        try:
            task.content = request.form['content']
            task.start_date_time = request.form['start_date_time']
            task.end_date_time = request.form['end_date_time']
            task.completed = request.form['completed']
            db.session.commit()
            return redirect('/api')
        except Exception as error:
            return f"error occured while updating task: {error}"
    else:
        return render_template('update.html',task = task)
    
@app.route('/api/completed/<int:id>')
def complete_task(id):
    task = Todo.query.get_or_404(id)
    task.completed = 100
    db.session.commit()
    return redirect('/api')
     
if __name__ == "__main__" :
    app.run(debug=True,host='0.0.0.0')

