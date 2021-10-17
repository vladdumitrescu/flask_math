"""Main application module"""

import os
import logging

from flask import request, Response, jsonify
from flask_jwt_extended import create_access_token, jwt_required

from models import Factorial, Fibonacci, Power
from helpers import factorial, fibonacci, power
from config import *

logger = logging.getLogger('werkzeug')
logFormatter = logging.Formatter("[%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s")
handler = logging.FileHandler('app.log')
handler.setFormatter(logFormatter)
logger.addHandler(handler)


# Create a route to authenticate the users and return JWTs. 
# The create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    request_data = request.get_json()
    username = request_data["username"]
    password = request_data["password"]
    if username != "test" or password != "test":
        return jsonify({"msg": "Invalid username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route('/v1/factorials', methods=['GET'])
@cache.cached(timeout=50)
@jwt_required()
def get_factorials():
    return jsonify({'Factorials': Factorial.read_all_factorials()})


@app.route('/v1/factorials/<int:id_>', methods=['GET'])
@cache.cached(timeout=50)
@jwt_required()
def get_factorial_by_id(id_):
    try:
        return_value = Factorial.read_factorial(id_)
    except AttributeError as e:
        logger.error(f"Error: {e}")
        response = Response(f"Cannot find factorial with id {id_}.", status=404, mimetype='application/json')
        return response
    else:
        return jsonify(return_value)


@app.route('/v1/factorials', methods=['POST'])
@jwt_required()
def post_factorial():
    request_data = request.get_json()
    try:
        result = factorial(request_data['number'])
    except (TypeError, ValueError) as e:
        logger.error(f"Error: {e}")
        response = Response(f"The provided number must be a positive integer. Received: {request_data['number']}", 400,
                            mimetype='application/json')
    else:
        Factorial.create_factorial(request_data["number"], result)
        response = Response(f"Factorial result for {request_data['number']} is {result}.", 201,
                            mimetype='application/json')
    return response


@app.route('/v1/factorials/<int:id_>', methods=['PUT'])
@jwt_required()
def put_factorial(id_):
    request_data = request.get_json()
    try:
        Factorial.update_factorial(id_, request_data['number'], request_data['factorial'])
    except AttributeError as e:
        logger.error(f"Error: {e}")
        response = Response(f"Factorial result with id {id_} was not found.", status=404, mimetype='application/json')
    else:
        logger.info(f"Factorial result with id {id_} was updated.")
        response = Response(f"Factorial result with id {id_} was updated.", status=200, mimetype='application/json')
    return response


@app.route('/v1/factorials/<int:id_>', methods=['DELETE'])
@jwt_required()
def delete_factorial(id_):
    result = Factorial.delete_factorial(id_)
    if result:
        logger.info(f"Factorial result with id {id_} was deleted.")
        response = Response(f"Factorial result with id {id_} was deleted.", status=200, mimetype='application/json')
    else:
        logger.info(f"Cannot find factorial with id {id_} to delete.")
        response = Response(f"Cannot find factorial with id {id_} to delete.", status=404, mimetype='application/json')
    return response


@app.route('/v1/fibonacci', methods=['GET'])
@cache.cached(timeout=50)
@jwt_required()
def get_fibonacci():
    return jsonify({'Fibonacci': Fibonacci.read_all_fibonacci()})


@app.route('/v1/fibonacci/<int:id_>', methods=['GET'])
@cache.cached(timeout=50)
@jwt_required()
def get_fibonacci_by_id(id_):
    try:
        return_value = Fibonacci.read_fibonacci(id_)
    except AttributeError as e:
        logger.error(f"Error: {e}")
        response = Response(f"Cannot find fibonacci with id {id_}.", status=404, mimetype='application/json')
        return response
    else:
        return jsonify(return_value)


@app.route('/v1/fibonacci', methods=['POST'])
@jwt_required()
def post_fibonacci():
    request_data = request.get_json()
    try:
        result = fibonacci(request_data['number'])
    except (TypeError, ValueError) as e:
        logger.error(f"Error: {e}")
        response = Response(f"The provided number must be a positive integer. Received: {request_data['number']}", 400,
                            mimetype='application/json')
    else:
        Fibonacci.create_fibonacci(request_data["number"], result)
        response = Response(f"Fibonacci result for {request_data['number']} is {result}.", 201,
                            mimetype='application/json')
    return response


@app.route('/v1/fibonacci/<int:id_>', methods=['PUT'])
@jwt_required()
def put_fibonacci(id_):
    request_data = request.get_json()
    try:
        Fibonacci.update_fibonacci(id_, request_data['number'], request_data['fibonacci'])
    except AttributeError as e:
        logger.error(f"Error: {e}")
        response = Response(f"Fibonacci result with id {id_} was not found.", status=404, mimetype='application/json')
    else:
        logger.info(f"Fibonacci result with id {id_} was updated.")
        response = Response(f"Fibonacci result with id {id_} was updated.", status=200, mimetype='application/json')
    return response


@app.route('/v1/fibonacci/<int:id_>', methods=['DELETE'])
@jwt_required()
def delete_fibonacci(id_):
    result = Fibonacci.delete_fibonacci(id_)
    if result:
        logger.info(f"Fibonacci result with id {id_} was deleted.")
        response = Response(f"Fibonacci result with id {id_} was deleted.", status=200, mimetype='application/json')
    else:
        logger.info(f"Cannot find fibonacci with id {id_} to delete.")
        response = Response(f"Cannot find fibonacci with id {id_} to delete.", status=404, mimetype='application/json')
    return response


@app.route('/v1/powers', methods=['GET'])
@cache.cached(timeout=50)
@jwt_required()
def get_powers():
    return jsonify({'Powers': Power.read_all_powers()})


@app.route('/v1/powers/<int:id_>', methods=['GET'])
@cache.cached(timeout=50)
@jwt_required()
def get_power_by_id(id_):
    try:
        return_value = Power.read_power(id_)
    except AttributeError as e:
        logger.error(f"Error: {e}")
        response = Response(f"Cannot find power with id {id_}.", status=404, mimetype='application/json')
        return response
    else:
        return jsonify(return_value)


@app.route('/v1/powers', methods=['POST'])
@jwt_required()
def post_power():
    request_data = request.get_json()
    try:
        result = power(request_data['base'], request_data['exponent'])
    except (TypeError, ValueError) as e:
        logger.error(f"Error: {e}")
        response = Response(
            f"The provided base and exponent must be a positive integer. "
            f"Received base: {request_data['base']}, exponent: {request_data['exponent']}",
            400,
            mimetype='application/json')
    else:
        Power.create_power(request_data['base'], request_data['exponent'], result)
        response = Response(f"Power result for {request_data['base']} and {request_data['exponent']} is {result}.", 201,
                            mimetype='application/json')
    return response


@app.route('/v1/powers/<int:id_>', methods=['PUT'])
@jwt_required()
def put_power(id_):
    request_data = request.get_json()
    try:
        Power.update_power(id_, request_data['base'], request_data['exponent'],
                           request_data['power'])
    except AttributeError as e:
        logger.error(f"Error: {e}")
        response = Response(f"Power result with id {id_} was not found.", status=404, mimetype='application/json')
    else:
        logger.info(f"Power result with id {id_} was updated.")
        response = Response(f"Power result with id {id_} was updated.", status=200, mimetype='application/json')
    return response


@app.route('/v1/powers/<int:id_>', methods=['DELETE'])
@jwt_required()
def delete_power(id_):
    result = Power.delete_power(id_)
    if result:
        logger.info(f"Power result with id {id_} was deleted.")
        response = Response(f"Power result with id {id_} was deleted.", status=200, mimetype='application/json')
    else:
        logger.info(f"Cannot find power with id {id_} to delete.")
        response = Response(f"Cannot find power with id {id_} to delete.", status=404, mimetype='application/json')
    return response


if __name__ == '__main__':
    if os.path.exists('database.db'):
        os.remove('database.db')
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)  # remove debug=True
