from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/akyildiz/Desktop/TodoApp/todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    TITLE = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

@app.route("/")
def mainpage():
    todos = Todo.query.all()
    return render_template("mainpage.html",todo = todos)

@app.route("/add", methods = ["POST"])
def addTodo():
    add = request.form.get("inp")
    newTodo = Todo(TITLE=add,complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("mainpage"))

@app.route("/update/<string:id>")
def update(id):
    tod = Todo.query.filter_by(ID=id).first()
    """if tod.complete:
        tod.complete = False
    else: 
        tod.complete = True"""
    tod.complete = not tod.complete
    db.session.commit()
    return redirect(url_for("mainpage"))
@app.route("/delete/<string:id>")
def delete(id):
    tod = Todo.query.filter_by(ID=id).first()
    db.session.delete(tod)
    db.session.commit()
    return redirect(url_for("mainpage"))
        
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


