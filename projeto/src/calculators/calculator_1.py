from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
    '''
    um numero e dividio em 3 partes

    aprimeira e dividida por 4 e seu resultado somado a 7
    apos isso o resultado e elevado ao quadrado e multiplicado por um valor de 0.257

    a segunda parte e elevada a potencia de 2.121, dividida por 5 e somado a 1
    
    
    '''

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)
        second_process_result = self.__second_process(splited_number)
        calc_result = first_process_result + second_process_result + splited_number
        response = self.__format_response(calc_result)
        return response
    
    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("body mal formatado")
        
        input_data = body["number"]
        return input_data
    
    # etapa responsavel pela primeira parte do processo, note que cada etapa esta sendo dividida em funcoes com responsavilidades unicas (srp)
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part

    def __second_process(self, second_number: float) -> float:
        first_part = second_number ** 2.121
        second_part = (first_part/5) + 1
        return second_part
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "calculator": 1,
                "result": calc_result
            }
        }