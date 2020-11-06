"""
Description: Requests supported by the flask app.
"""
import sqlalchemy
from flask import jsonify, request, make_response

from library_app import app, author, utils
from library_app.models import Author


@app.route('/')
def index():
    return "Welcome to Library app"


@app.route('/site-map')
def site_map():
    urls = {utils.werkzeug_rule_endpoint(url): str(url.methods) for url in app.url_map.iter_rules()}
    return jsonify(urls)


@app.route('/author', methods=['GET', 'POST'])
def authors_view():
    if request.method == 'GET':
        authors = author.get_all(filters=request.args)
        return jsonify(data=Author.serialize_list(authors))

    if request.method == 'POST':
        try:
            author.create(name=request.json['name'],
                          country=request.json.get('country'),
                          year_of_birth=request.json.get('year_of_birth'))
            return make_response(jsonify(response='OK'), 201)
        except sqlalchemy.exc.InvalidRequestError:
            return make_response(jsonify(error='Bad request'), 400)


@app.route('/author/<int:author_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def author_view(author_id):
    author_result = author.get(author_id)
    if author_result is None:
        return make_response(jsonify(response=f'Author with id {author_id} not found'), 404)

    if request.method == 'GET':
        return jsonify(author_result.serialize())

    if request.method == 'DELETE':
        author.delete(author_result)
        return jsonify(response='OK')

    if request.method in ['PUT', 'PATCH']:
        try:
            if request.method == 'PATCH':
                fields = request.json
            else:  # for PUT request, use default values for empty fields
                fields = {'name': request.json['name'],
                          'country': request.json.get('country'),
                          'year_of_birth': request.json.get('year_of_birth')}
            author.update(author_id, fields)
            return jsonify(response='OK')

        except (sqlalchemy.exc.InvalidRequestError, KeyError):
            return make_response(jsonify(error='Bad request'), 400)
