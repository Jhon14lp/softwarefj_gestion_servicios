import logging
from typing import List
from excepciones import ServicioError
from base import Servicio
from cliente import Cliente

# Configuración de Logs (Se queda aquí porque es parte de la gestión)
logging.basicConfig(
    filename="software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class SistemaGestion:
    def __init__(self) -> None:
        self.clientes: List[Cliente] = []
        self.servicios: List[Servicio] = []

    def registrar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)
        logging.info(f"Cliente registrado: {cliente.get_info()}")

    def procesar_servicio(self, servicio: Servicio) -> float:
        """Procesa el servicio y retorna el costo para la interfaz."""
        try:
            costo = servicio.calcular_costo()
            logging.info(f"Servicio procesado: {servicio.detallar()} | Costo: {costo}")
            return costo
        except Exception as e:
            logging.error(f"Error al calcular costo: {e}")
            raise ServicioError(f"Error en el cálculo: {e}")