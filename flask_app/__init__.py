from flask import Flask

app = Flask(__name__)
app.secret_key = 'X"ayS8Ct72o^s~j'

DATABASE = 'rhythm_tatsujin_schema'
DOMAIN = 'http://localhost:5000'