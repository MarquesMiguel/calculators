introduzir e definir explicitamente a tipagem das entradas, somente aconselhamento, nao define data, documentacao
type hints - basico

* curso https://www.youtube.com/watch?v=7id535KPHK8&list=PLbIBj8vQhvm04EuddtleOAoEmfU9vwQlN

tipagem python
-> tipagem dinamica, forte

type anotations -> tipagem de dado, mypy, documentar

    my py, checar typagem
        mypy local/arquivo

    


type hints
-> indicar quais tipos sao esperadoe em variaveis parametro e retornos de funcoes, para melhorar  a doc, 
-> checagem com o my py

    -> nome: type = valor
    ex:
        nome: str = "miguel"
        idade: int = 18


estruturas avancadas
-> modulo typing
-> Lists, Dict, etc
    ex: 
            valores: List[int] = [1, 2, 3]
            # Dicionário com chaves string e valores float
            taxas: Dict[str, float] = {"dolar": 5.15, "euro": 5.50}
            # Variável que pode ser int OU float (Union)
            resultado: Union[int, float] = 10.5 


