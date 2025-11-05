class Personas:
    def __init__(self, nombre,apellido, lugar_nacimiento=None, apellido_soltera=None):
        self.nombre = nombre
        self.apellido= apellido
        self.lugar_nacimiento = lugar_nacimiento
        self.apellido_soltera = apellido_soltera
        self.padre= None
        self.madre= None
        self.conyuge= None

    def casar(self, pareja):
        self.conyuge = pareja
        pareja.conyuge = self

    def __str__(self):
        texto = f'{self.nombre} {self.apellido}'
        if self.lugar_nacimiento:
            texto += f', nacido en {self.lugar_nacimiento}'
        if self.apellido_soltera:
            texto += f', apellido de soltera: {self.apellido_soltera}'


    