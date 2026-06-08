# todas as definicoes basicas para o servidor

from flask import Flask
from src.main.routes.calculators import calc_route_bp

app = Flask(__name__) # obj de servidor de flask

app.register_blueprint(calc_route_bp)

