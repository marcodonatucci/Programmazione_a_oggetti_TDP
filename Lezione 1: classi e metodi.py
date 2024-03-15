class Car:
    # class definisce una classe (lettera grande), gli attributi non sono definiti all'inizio
    def __init__(self, color, model, year):
        # il costruttore della classe si definisce con __init__, devi usare self al posto del "this"
        # self è il riferimento all'oggetto stesso, è sempre esplicito, è sempre il primo parametro di tutti i metodi
        # in python il costruttore crea un oggetto self senza proprietà e gliele assegna
        # non c'è modo di avere una variabile non inizializzata
        self.color = color
        self.model = model
        self.year = year

    def age(self):
        # sempre con def si possono definire i metodi, si usa sempre self, e il return è uguale
        return 2024 - self.year


my_car = Car("white", "Panda", 2010)
# posso creare un nuovo oggetto direttamente chiamando il costruttore (nome della classe) su una variabile
print(my_car.age())  # chiamo i metodi con il .
# il self non viene mai passato quando si chiama un metodo, il metodo assegna a self l'oggetto con il "." che lo ha
# chiamato, puoi anche scrivere Car.age(my_car) dove passi il self al metodo
