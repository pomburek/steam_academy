from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        'index.html'
    )

from datetime import datetime

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Project(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False)
   categories = db.Column(db.String(100), nullable=False)
   link = db.Column(db.String(100), nullable=True)
   created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
   finished = db.Column(db.Boolean)

   def __repr__(self):
       return '<Project %r>' % self.title


@app.route("/")
def home():
    my_projects = Project.query.all()
    return render_template('index.html' ,my_projects=my_projects)