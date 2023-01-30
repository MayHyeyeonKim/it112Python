from flask import Flask, request, render_template
from database import init_db, db_session
from models import User

app = Flask(__name__)

init_db()
#createData()


@app.route('/insert')
def insert():
  from models import User
  db_session.add(
    User('John', '010-1234-1234', 'John@localhost', '02/03/2000', 'M',
         'Hunting', 'A3385', 'Sample Description'))
  db_session.add(
    User('Estell', '010-234-2345', 'Estell@localhost', '02/03/2001', 'F',
         'Hunting', 'A3325', '22 Description'))
  db_session.add(
    User('Mike', '010-432-321', 'Mike@localhost', '09/03/1997', 'M', 'Fishing',
         'A3326', '22 Description 22'))
  db_session.add(
    User('Dona', '123-345-9867', 'Dona@localhost', '09/05/1994', 'M', 'Boxing',
         'A1236', '22 Description 22'))
  db_session.commit()
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