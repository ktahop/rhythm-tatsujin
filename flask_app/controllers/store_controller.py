import os
import stripe
from flask import render_template, redirect, session
from flask_app import app, DOMAIN
from flask_app.models.users_model import User

stripe.api_key = os.environ.get('STRIPE_API_KEY')

# ===== STORE FRONT =====
@app.route('/')
def index():
  if "user_id" in session:
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template("index.html", logged_user = logged_user)
  return render_template("index.html")

# ===== ARCADE LOCATION =====
# @app.route('/location')
# def location():
#     return render_template("location.html", google_api = google_api_key)

# ===== CHECKOUT PAGE =====
@app.route('/taiko_checkout', methods=['POST'])
def taiko_checkout():
  if "user_id" not in session:
    return redirect('/login')
  try:
    checkout_session = stripe.checkout.Session.create(
      line_items=[
        {
          'price': 'price_1MWtsWEHhFeEezmsoggtfMG1',
          'quantity': 1,
        }],
      mode='payment',
      success_url=DOMAIN + '/success',
      cancel_url=DOMAIN + '/'
    )
  except Exception as e:
    return str(e)

  return redirect(checkout_session.url, code=303)

@app.route('/soundfx_checkout', methods=['POST'])
def soundfx_checkout():
  if "user_id" not in session:
    return redirect('/login')
  try:
    checkout_session = stripe.checkout.Session.create(
      line_items=[
        {
          'price': 'price_1MWttdEHhFeEezmsfuXLijkY',
          'quantity': 1,
        }],
        mode='payment',
        success_url=DOMAIN + '/success',
        cancel_url=DOMAIN + '/'
    )
  except Exception as e:
    return str(e)

  return redirect(checkout_session.url, code=303)

@app.route('/dj_checkout', methods=['POST'])
def dj_checkout():
  if "user_id" not in session:
    return redirect("/login")
  try:
    checkout_session = stripe.checkout.Session.create(
      line_items=[
        {
          'price': 'price_1MWw6qEHhFeEezmszYXyvJgH',
          'quantity': 1,
        }],
      mode='payment',
      success_url=DOMAIN + '/success',
      cancel_url=DOMAIN + '/'
      )
  except Exception as e:
    return str(e)

  return redirect(checkout_session.url, code=303)

# # ===== SUCCESS PAGE =====
@app.route('/success')
def success():
  if "user_id" not in session:
    return redirect('/login')
  return render_template('success.html')
