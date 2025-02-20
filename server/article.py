from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Article(Resource):
    TABLE_NAME = 'articles'

    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('Objet',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('Auteur',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('Date de publication',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('Contenu',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        article = self.find_by_name(name)
        if article:
            return article
        return {'message': 'Article not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        #Find an article by its name
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'article': {'name': row[0], 'objet': row[1], 'Auteur': row[2], 'Date de publication': row[3]}}

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An article with name '{}' already exists.".format(name)}

        data = Article.parser.parse_args()

        article = {'name': name, 'objet': data['objet'], 'Auteur': data['Auteur'], 'Date de publication': data['Date de publication'], 'Contenu': data['Contenu']}

        try:
            Article.insert(article)
        except:
            return {"message": "An error occurred inserting the article."}

        return article

    @classmethod
    def insert(cls, article):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?, ?)".format(table=cls.TABLE_NAME)
        cursor.execute(query, (article['name'], article['objet'], article['Auteur'], article['Date de publication'], article['Contenu']))

        connection.commit()
        connection.close()

    @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Article deleted'}

    @jwt_required()
    def put(self, name):
        data = Article.parser.parse_args()
        article = self.find_by_name(name)
        updated_article = {'name': name, 'price': data['price']}
        if article is None:
            try:
                Article.insert(updated_article)
            except:
                return {"message": "An error occurred inserting the article."}
        else:
            try:
                Article.update(updated_article)
            except:
                return {"message": "An error occurred updating the article."}
        return updated_article

    @classmethod
    def update(cls, article):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE {table} SET price=? WHERE name=?".format(table=cls.TABLE_NAME)
        cursor.execute(query, (article['price'], article['name']))

        connection.commit()
        connection.close()


class ArticleList(Resource):
    TABLE_NAME = 'articles'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        articles = []
        for row in result:
            articles.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'articles': articles}