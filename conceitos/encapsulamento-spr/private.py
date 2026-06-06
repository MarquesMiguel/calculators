# encapsulamento e Single Responsability Principle

class MyClass():

    def __init__(self, data) -> None:
        # sem o setter
        # self._data = data

        # com o setter desde o inicio

        self.data = data

    #GETTER: ler o dado com obj.data

    @property
    def data(self):
        return self._data
    
    #SETTER: setta o valor

    @data.setter
    def data(self, value):
        if value == True:
            self._data = value

    def registry(self) -> None:
        print('Start process...')
        self.__verify()
        self.__verify_registry()
        self.__insert_data()
        
    def __verify(self) -> None: 
        print('verify data')
    
    def __verify_registry(self) -> None:
        print('verify registry')
    
    def __insert_data(self) -> None:
        print('insert in DB')
    

obj = MyClass(data="data")

obj.registry()
