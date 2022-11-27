from flask import Flask
from flask import render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import send_from_directory

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zosia.db'
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


with app.app_context():
    db.create_all()


@app.route('/static/<path:path>')
def send_report(path):
    print("co u diaska", path)
    return send_from_directory('static', path)


@app.route("/")
def home():
    my_projects = Project.query.all()
    return render_template('index.html', my_projects=my_projects)
   