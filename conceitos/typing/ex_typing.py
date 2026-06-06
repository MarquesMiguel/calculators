from typing import Dict # importar modulo para types mais complexos

# certo ✅
# def add(elem1: int ,elem2: float) -> float: #retorno
#     return elem1 + elem2

# errado ❌
# def add(elem1,elem2): 
#     return elem1 + elem2




#int floart str boool
#dict list tuple

# certo ✅
def add(elem1: int ,elem2: float) -> Dict: #retorno
    response = elem1 + elem2
    return {"sum": response}