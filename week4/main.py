from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(50), unique=False)
    phone       = db.Column(db.String(120), unique=False)
    email       = db.Column(db.String(120), unique=True)
    birth       = db.Column(db.String(10), unique=False)
    gender      = db.Column(db.String(10), unique=False)
    hobby       = db.Column(db.String(120), unique=False)
    carNo       = db.Column(db.String(120), unique=False)
    description = db.Column(db.String(200), unique=False)

    def __init__(self, name=None, phone=None, email=None, birth=None, gender=None, hobby=None, carNo=None, description=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.birth = birth
        self.gender = gender
        self.hobby = hobby
        self.carNo = carNo
        self.description = description
        
    def __repr__(self):
        return '<User %r>' % (self.name)


@app.route('/insert')
def insert():
  db.create_all()
  db.session.add(
    User('John', '010-1234-1234', 'John@localhost', '02/03/2000', 'M',
         'Hunting', 'A3385', 'Sample Description'))
  db.session.add(
    User('Estell', '010-234-2345', 'Estell@localhost', '02/03/2001', 'F',
         'Hunting', 'A3325', '22 Description'))
  db.session.add(
    User('Mike', '010-432-321', 'Mike@localhost', '09/03/1997', 'M', 'Fishing',
         'A3326', '22 Description 22'))
  db.session.add(
    User('Dona', '123-345-9867', 'Dona@localhost', '09/05/1994', 'M', 'Boxing',
         'A1236', '22 Description 22'))
  db.session.commit()
  return 'test'


@app.route('/users')
def users():
  data = User.query.all()
  res = ''
  for dt in data:
    res += dt.name
    res += ' ' + dt.email
    res += ' ' + dt.gender
    res += '<br>'
  return render_template('list.html', data=data)

@app.route('/user/<id>')
def user(id):
  dt = User.query.filter(User.id==id).first()
  res = ''
  res += 'Name : ' + dt.name
  res += '<br>Phone : ' + dt.phone
  res += '<br>Email : ' + dt.email
  res += '<br>Birth : ' + dt.birth
  res += '<br>Gender : ' + dt.gender
  res += '<br>Hobby : ' + dt.hobby
  res += '<br>CarNo : ' + dt.carNo
  res += '<br>Description : ' + dt.description
  return res

app.run(host='0.0.0.0', port=81)