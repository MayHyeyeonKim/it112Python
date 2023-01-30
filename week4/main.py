from flask import Flask, jsonify, request, Response, render_template, make_response
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


@app.route('/users', methods=["GET"])
def users():
  data = User.query.all()
  res = []
  for dt in data:
    row = {'id' : dt.id,
           'name' : dt.name
           , 'phone' : dt.phone
           , 'email' : dt.email
           , 'gender' : dt.gender
           , 'birth' : dt.birth
           , 'carNo' : dt.carNo
           , 'description' : dt.description
           , 'hobby' : dt.hobby}
    res.append(row)
  resp = make_response(jsonify(res))
  resp.headers['content-type'] = 'application/json'
  return resp

@app.route('/user', methods=["POST"])
def createUser():
  try:
    user = request.get_json()
    db_session.add(
    User(user['name'], user['phone'],  user['email'], user['birth']
         , user['gender'],
         user['hobby'], user['carNo'], user['description']))
    db_session.commit()
    return users()
  except Exception as e:
    return Response("{'message':'fail'}", status=500, mimetype='application/json')

app.run(host='0.0.0.0', port=81)