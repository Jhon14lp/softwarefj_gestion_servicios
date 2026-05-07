import logging
from typing import List
from excepciones import SoftwareFJError, ServicioError
from base import Servicio
from cliente import Cliente
from servicios import AlquilerEquipo, AsesoriaEspecializada
from reserva import ReservaSala

# Configuración de Logs
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

    def procesar_servicio(self, servicio: Servicio) -> None:
        try:
            costo = servicio.calcular_costo()
        except Exception as e:
            logging.error(f"Error al calcular costo: {e}")
            raise ServicioError("Error en el cálculo del servicio.") from e
        else:
            logging.info(f"Servicio procesado correctamente. Costo: {costo}")
            print(f"✅ {servicio.detallar()} | Costo: {costo}")
        finally:
            print("Operación finalizada.\n")

if __name__ == "__main__":
    sistema = SistemaGestion()

    # Operaciones válidas
    try:
        c1 = Cliente(1, "Ana Pérez", "ana@correo.com")
        sistema.registrar_cliente(c1)
        sistema.procesar_servicio(ReservaSala(3, 50))
        sistema.procesar_servicio(AlquilerEquipo(2, 100, seguro=20))
    except SoftwareFJError as e:
        print(f"❌ Error: {e}")

    # Ejemplo de error controlado
    try:
        sistema.procesar_servicio(AlquilerEquipo("error", 100))
    except Exception as e:
        print(f"❌ Error detectado: {e}")