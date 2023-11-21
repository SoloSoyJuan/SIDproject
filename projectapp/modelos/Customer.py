class Customer:

    def __init__(self, id):
        self.id = id
        self.descuento = 0.1
        self.hijos = []
        self.lugarN = None
        self.lugarUbi = None
        self.hobbies = []
        self.deportes = []
        self.categorias = []
        self.estadoCivil = None

    def agregarHijos(self, hijo):
        self.hijos.append(hijo)

    def lugarN(self, lugar):
        self.lugarN = lugar

    def lugarUbi(self, lugar):
        self.lugarUbi = lugar

    def hobbies(self, nombre):
        self.hobbies.append(nombre)

    def deportes(self, nombre):
        self.deportes.append(nombre)

    def estadiCivil(self, estadoCivil):
        self.estadoCivil = estadoCivil

    def categorias(self, nombre):
        self.categorias.append(nombre)