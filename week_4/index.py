from flask import Flask
from flask_restplus import Api, Resource
import pandas as pd
import transform_data as t

df = pd.read_csv('./data/Books.csv')

df = t.transform(df)
app = Flask(__name__)
api = Api(app)


@api.route('/books/<int:id>')
class Books(Resource):
    def get(self, id):
        if id not in df.index:
            api.abort(404, f"Book {id} does not exist")
        book = dict(df.loc[id])
        return book


app.run(debug=True)
