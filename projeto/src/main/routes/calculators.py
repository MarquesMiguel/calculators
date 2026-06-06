from flask import Blueprint, jsonify, request

#nomear todasd as rotas relacionadas as calculadoras apartir dessa variavel, saber quais rotas sao associadas a calculadoras
calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    print(request.json)
    return jsonify({ "success": True}), 200