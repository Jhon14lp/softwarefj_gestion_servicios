from cliente import Cliente
from reserva import ReservaSala
from servicios import AlquilerEquipo, AsesoriaEspecializada
from sistema import SistemaGestion

def ejecutar_pruebas():
    sistema = SistemaGestion()
    print("--- INICIANDO LÍNEAS DE PRUEBA ---")
    
    # Datos de prueba del sistema original
    try:
        c1 = Cliente(1, "Ana Pérez", "ana@correo.com")
        sistema.registrar_cliente(c1)
        
        # Servicios de prueba
        servicios_test = [
            ReservaSala(3, 50),
            AlquilerEquipo(2, 100, seguro=20),
            AsesoriaEspecializada(5, 80, descuento=0.1)
        ]
        
        for s in servicios_test:
            sistema.procesar_servicio(s)
            
    except Exception as e:
        print(f"Error en pruebas: {e}")

if __name__ == "__main__":
    ejecutar_pruebas()