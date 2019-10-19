from flask import Flask
from flask_restplus import Api, Resource
import pandas as pd
import transform_data as t
from flask_restplus import fields
from flask import request
df = pd.read_csv('./data/Books.csv')

df = t.transform(df)
app = Flask(__name__)
api = Api(app)

# The following is the schema of Book
book_model = api.model('Book', {
    'Flickr_URL': fields.String,
    'Publisher': fields.String,
    'Author': fields.String,
    'Title': fields.String,
    'Date_of_Publication': fields.Integer,
    'Identifier': fields.Integer,
    'Place_of_Publication': fields.String
})


@api.route('/books/<int:id>')
class Books(Resource):
    def get(self, id):
        if id not in df.index:
            api.abort(404, f"Book {id} does not exist")
        book = dict(df.loc[id])
        return book

    def delete(self, id):
        if id not in df.index:
            api.abort(404, f"Book {id} does not exist")
        df.drop(id, inplace=True)
        return {"message": f"Book {id} is removed"}, 200

    @api.expect(book_model)
    def put(self, id):
        if id not in df.index:
            api.abort(404, f"Book {id} does not exist")

        book = request.json

        # check for changing other book with their ID
        if 'Identifier' in book and id != int(book['Identifier']):
            print(id, int(book['Identifier']))
            return {"message": f"Identifier {id} can not be changed"}, 400

        # Update the values
        for key in book:
            if key not in book_model.keys():
                # unexpected column
                return {"message": f"Property {key} is invalid"}, 400
            df.loc[id, key] = book[key]

        return {"message": f"Book {id} had been successfully updated"}, 200




app.run(debug=True)
