from base import Servicio

class AlquilerEquipo(Servicio):
    def __init__(self, dias: int, tarifa_dia: float, seguro: float = 0.0) -> None:
        self.dias = dias
        self.tarifa_dia = tarifa_dia
        self.seguro = seguro

    def calcular_costo(self) -> float:
        return (self.dias * self.tarifa_dia) + self.seguro

    def detallar(self) -> str:
        return f"Alquiler de equipo por {self.dias} días. Tarifa: {self.tarifa_dia}/día + Seguro: {self.seguro}"

class AsesoriaEspecializada(Servicio):
    def __init__(self, horas: int, tarifa_hora: float, descuento: float = 0.0) -> None:
        self.horas = horas
        self.tarifa_hora = tarifa_hora
        self.descuento = descuento

    def calcular_costo(self) -> float:
        costo = self.horas * self.tarifa_hora
        return costo - (costo * self.descuento)

    def detallar(self) -> str:
        return f"Asesoría especializada por {self.horas} horas. Tarifa: {self.tarifa_hora}/h con descuento {self.descuento*100}%"