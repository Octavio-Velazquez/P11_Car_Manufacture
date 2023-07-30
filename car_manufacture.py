
class CarManufacture():
    """Creamos las bases para la creación de un coche."""

    def __init__(self, fabricante, modelo, año):
        """Indicamos los atributos iniciales que pueden tener todos los coches en común."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        self.odometro = 150
        self.slogan = ""
        self.ruedas = 5
        self.baterias = 1
        self.tanque = "gasolina"

    def datos_descriptivos(self):
        """Devuelve los datos descriptivos del coche."""
        long_name = f"{self.año} {self.fabricante} {self.modelo}"
        return long_name.title()

    def lectura_odometro(self):
        """Lectura del odómetro."""
        print(f"La lectura del coche es de {self.odometro} kms.")

    def actualizando_odometro(self, kilometros):
        """Actualizo el odómetro."""
        if kilometros >= self.odometro:
            self.odometro = kilometros
        else:
            print("No se puede retroceder el kilometraje del coche.")

    def lema(self):
        """Lema de la empresa de coches."""
        self.slogan = input("Indica un slogan: ")
        print(f"{self.slogan.upper()}")

    def ruedas_coche(self):
        """Ruedas standard de cada coche."""
        return self.ruedas
        # print(f"Por defecto, los coches vienen con {self.ruedas} ruedas. {self.ruedas - 1} instaladas y {self.ruedas - 4} de repuesto.")

    def bateria(self):
        """Indico la batería de mi coche."""
        print(f"Viene con {self.baterias} batería de litio. Y tienen {self.ruedas_coche()} ruedas.")

    def tanque_coche(self):
        """Indica el tipo de combustible que tiene el tanque del coche."""
        print(f"El tanque de mi coche utiliza {self.tanque}.")


class ElectricCar(CarManufacture):
    """Modelamos un coche eléctrico."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos de la clase base."""
        super().__init__(fabricante, modelo, año)


class WaterCar(CarManufacture):
    """Modelamos un coche de agua."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos de la clase base."""
        super().__init__(fabricante, modelo, año)


class FireCar(CarManufacture):
    """Modelamos un coche de fuego."""

    def __init__(self, fabricante, modelo, año):
        """Inicializa los atributos de la clase base."""
        super().__init__(fabricante, modelo, año)
        self.tamaño_bateria = 75

    def tipo_bateria(self):
        """Muestra el tamaño de la bateira."""
        print(f"Este coche tiene una bateria de {self.tamaño_bateria}-kWh.")


"""
mi_coche = CarManufacture("toyota", "corolla", 2020)
print(mi_coche.datos_descriptivos())
mi_coche.lectura_odometro()
mi_coche.lema()
mi_coche.ruedas_coche()
mi_coche.bateria()
mi_coche.tanque_coche()
mi_coche.actualizando_odometro(20)
print(mi_coche.odometro)
print(mi_coche.fabricante)
"""

"""
mi_coche_pikachu = ElectricCar("Nintendo", "Pikachu 2508", 1998)
print(mi_coche_pikachu.datos_descriptivos())
print(f"Mi coche eléctrico tiene {mi_coche_pikachu.ruedas_coche()} ruedas.")
"""

"""
charizard_coche = FireCar("Nintendo", "Charizard09", 1996)
print(charizard_coche.datos_descriptivos())
charizard_coche.tipo_bateria()
"""

