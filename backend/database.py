from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database configs

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///e_kirana.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
app.app_context()

class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200), nullable=False)
    unit_id = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Double, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.product_id} - {self.product_name} - {self.unit_id} - {self.rate}"

"""
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method=="POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()

    allTodo=Todo.query.all()
    return render_template("index.html", allTodo=allTodo)


@app.route('/update/<int:sno>', methods=["GET", "POST"])
def update(sno):
    if request.method=="POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo=Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
"""        
        
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=False, host="0.0.0.0", port=5000)