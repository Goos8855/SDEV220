# M04 Case Study
# M04-API-CaseStudy-ElvisZheng.py
# This case study is meant to demonstrate the creation of an API. 
# Through this, we're meant to be able to store, get, add, and delete information about a book like name, id, publisher, and author.

from Flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__Name__)

app.config['SQLALCHEMY_DATABASE_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repi__(self):
        return f"{self.name} by {self.author}"
    
@app.route('/')
def index():
    return 'hi'

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'id':book.id, 'name':book.name, 'author': book.author}
        output.append(book_data)
    return{"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name":book.name, "author":book.author, "publisher": book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(name = request.json['name'], author = request.json['author'], publisher = request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route("/books/<id>", methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error":"book not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message" : "deleted"}
