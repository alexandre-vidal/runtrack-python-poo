class Operation:
    def __init__(self, nombre1, nombre2):
        self.__nombre1 = nombre1
        self.__nombre2 = nombre2
        
    def get_nombre1(self):
        return "Le nombre1 est", self.__nombre1
    
    def set_nombre1(self, nombre):
        self.__nombre1 = nombre
        
    def get_nombre2(self):
        return "Le nombre2 est", self.__nombre2
    
    def set_nombre2(self, nombre):
        self.__nombre2 = nombre
        
    def addition(self):
        return self.__nombre1 + self.__nombre2
        
        
operation = Operation(12, 3)
print(operation.get_nombre1())
print(operation.get_nombre2())
print(operation.addition())