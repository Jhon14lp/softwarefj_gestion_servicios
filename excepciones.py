class SoftwareFJError(Exception):
    """Excepción base para el sistema."""
    pass

class ClienteError(SoftwareFJError):
    """Errores relacionados con Cliente."""
    pass

class ServicioError(SoftwareFJError):
    """Errores relacionados con Servicios."""
    pass