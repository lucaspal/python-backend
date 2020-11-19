"""
Description: Requests supported by the flask app.
"""
import logging

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
            allowed_fields = ['name', 'country', 'year_of_birth']
            extra_fields = {k:v for k,v in request.json.items() if k not in allowed_fields}
            if len(extra_fields) > 0:
                return make_response(jsonify(response="Only name, country and year_of_birth are allowed"), 400)
            author.create(name=request.json['name'],
                          country=request.json.get('country'),
                          year_of_birth=request.json.get('year_of_birth'))
            return make_response(jsonify(response='OK'), 201)
        except sqlalchemy.exc.InvalidRequestError as error:
            return make_response(jsonify(error_message=str(error)), 400)


def get_lucky_number(author):
    logging.info(f'author input to lucky number: {author}')
    year_of_birth = author.year_of_birth
    lucky_number = 0
    while year_of_birth > 0:
        lucky_number += year_of_birth % 100
        year_of_birth = int(year_of_birth / 10)
        logging.info(f'year of birth: {year_of_birth} lucky number: {lucky_number}')
    return lucky_number


@app.route('/author/<int:author_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def author_view(author_id):
    logging.info(f'User has given input author_id as: {author_id}')
    author_result = author.get(author_id)
    logging.info(f'Author from db is: {author_result}')
    if author_result is None:
        return make_response(jsonify(response=f'Author with id {author_id} not found'), 404)

    if request.method == 'GET':
        lucky_number = get_lucky_number(author_result)
        logging.info(f'lucky number: {lucky_number}')
        return jsonify({**author_result.serialize(), 'lucky_number': lucky_number})

    if request.method == 'DELETE':
        author.delete(author_result)
        return jsonify(response='OK')

    logging.info(f'request method is: {request.method}')
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
