# All'interno della sottoclasse è presente un algoritmo di ricerca che va a cercare nella classe madre le
# informazioni che non trova nella sottoclasse stessa
# quando ho un metodo con lo stesso nome viene usato quello della sottoclasse
# prima di specializzare vado a richiamare il comportamento della classe padre con super().
# definizione sottoclasse: class NomeClasse(ClassePadre):

class Car:
    wheels = 4  # attributo di classe, tipo static in java

    def __init__(self, color, model, year):
        self.color = color  # questi sono attributi di istanza
        self.model = model
        self.year = year

    def age(self):
        return 2024 - self.year


class SportCar(Car):

    def __init__(self, color, model, year):
        super().__init__(color, model, year)
        self.speed = 'high'  # definisco attributi specifici nel self


my_car = Car("white", "Panda", 2010)
boss_car = SportCar('Black', 'Ferrari', 2022)  # quello che vedo sull'oggetto è l'unione delle proprietà
# e degli attributi di classe e superclass
print(my_car.age())

# una classe può ereditare da più classi, quindi usare attributi e metodi di più classi padre (no interfacce come java)
# class SportsCar(Car, ExpensiveGadget): eredita da due superclass diverse
# non posso usare super(), sono obbligato a chiamare le classi per nome (Car.__init__())

# POLIMORFISMO: chiamare lo stesso metodo/funzione/operazione con modi diversi a seconda del tipo di oggetto
# quando passi una funzione non interessa a python il tipo di oggetto che stai usando ma basta che abbia la funzione
# che stai usando definita! (Duck typing), esempio: print() qualsiasi cosa gli passi la processa a prescindere dal tipo
# di dato perché è un metodo definito in Object
# il set di metodi richiesti da oggetti di classi ereditarie è chiamato 'protocollo', così si implementa il polimorfismo
# definendo i Dunder nelle classi puoi chiamare le funzioni built-in
# __iter__() definisce la modalità di iterazione (ciclo for)
# __getitem__() le parentesi quadre con gli indici []
# __enter__() e __exit__() lo statement 'with' che crea un contesto (apre e chiude un file)
# __lt__ ordina gli oggetti e si occupa di definire il comportamento degli operatori di confronto <>...
# __eq__ compara gli oggetti tra di loro, viene usato in == != e sort, ci sono lt ed eq già definiti per alcuni elementi
