from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.users_model import User

bcrypt = Bcrypt(app)

# ===== LOGIN/REGISTER =====
@app.route('/login')
def login_view_page():
  return render_template('login.html')

# ===== REGISTER =====
@app.route('/user/register', methods=['post'])
def register():
  print(request.form)
  if not User.register_validate(request.form):
    return redirect('/login')
  hashed_pw = bcrypt.generate_password_hash(request.form['password'])
  data = {
    **request.form,
    'password': hashed_pw
    }
  user_id = User.register(data)
  session['user_id'] = user_id
  return redirect("/")

# ===== LOGIN =====
@app.route('/user/login', methods=['post'])
def login():
  data = {
    'email': request.form['email']
  }
  user_in_db = User.get_by_email(data)
  if not user_in_db:
    flash('Invalid credentials', 'log')
    return redirect("/login")
  if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    flash('Invalid credentials', 'log')
    return redirect('/login')
  session['user_id'] = user_in_db.id
  return redirect('/')

# ===== LOGOUT =====
@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')