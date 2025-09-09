# Start your project below

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# DB config (for now use SQLite in a file so migrations are persistent)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///procrm.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)   # ← this wires Alembic into Flask

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route("/")
def hello():
    return "Pro-CRM with migrations is alive!"


if __name__ == "__main__":
    app.run(debug=True)


