from flask_restful import marshal_with, fields, Resource, reqparse, Api
from flask import g, Blueprint
from demo_api.db import get_db
from werkzeug.exceptions import abort

res_def = {'me': fields.String}

api_bp = Blueprint('book_api', __name__)
api = Api(api_bp)


class Book(Resource):
    def __init__(self):
        super(Book, self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True)
        self.parser.add_argument('ISBN', type=str, required=True)

    def post(self):
        args = self.parser.parse_args()
        db = get_db()
        ISBN = args['ISBN']
        name = args['name']
        book = db.execute(
            'SELECT * FROM book AS b \
            WHERE b.id = ?', (ISBN,)
        ).fetchone()
        if book is not None:
            abort(400, f'Book with ISBN={ISBN} is already in the database')
        else:
            db.execute(
                'INSERT INTO book VALUES(?, ?)', (ISBN, name)
            )
            db.commit()
            return 'Success', 200


class BookList(Resource):
    def __init__(self):
        super(BookList, self).__init__()

    def get(self):
        db = get_db()
        books = db.execute('SELECT * FROM book').fetchall()
        return [(b['id'], b['bookname']) for b in books]


api.add_resource(Book, '/book')
api.add_resource(BookList, '/booklist')
