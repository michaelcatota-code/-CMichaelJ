# Clase base Robot
class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bateria = 100
        self.x = 0  # posición horizontal

    def saludar(self):
        # Devuelve un saludo con el nombre del robot
        return f"Hola, soy {self.nombre}"

    def mover(self, distancia):
        # Mueve al robot en el eje X y reduce batería
        self.x += distancia
        self.bateria -= abs(distancia)

    def status(self):
        # Devuelve estado del robot
        return f"batería={self.bateria}, x={self.x}"


# Clase RobotVolador heredando de Robot
class RobotVolador(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.z = 0  # altura inicial

    def volar(self, altura):
        # Cambia la altura y reduce batería
        self.z += altura
        self.bateria -= abs(altura) * 2  # batería baja más al volar

    def status(self):
        # Estado extendido con altura
        return f"batería={self.bateria}, x={self.x}, z={self.z}"


# --- Simulación obligatoria ---
r = RobotVolador("Atlas")
print(r.saludar())

r.mover(10)      # x=10, batería=90
r.volar(5)       # z=5, batería=80
print(r.status())

r.volar(-3)      # z=2, batería=74
print(r.status())
