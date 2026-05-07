from base import Servicio

class ReservaSala(Servicio):
    def __init__(self, horas: int, tarifa_hora: float) -> None:
        self.horas = horas
        self.tarifa_hora = tarifa_hora

    def calcular_costo(self) -> float:
        return self.horas * self.tarifa_hora * 1.19  # IVA 19%

    def detallar(self) -> str:
        return f"Reserva de sala por {self.horas} horas. Tarifa: {self.tarifa_hora}/h"