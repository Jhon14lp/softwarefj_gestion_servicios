import re
from base import EntidadSistema
from excepciones import ClienteError

class Cliente(EntidadSistema):
    def __init__(self, id_cliente: int, nombre: str, email: str) -> None:
        self.__set_id(id_cliente)
        self.__set_nombre(nombre)
        self.__set_email(email)

    def __set_id(self, id_cliente: int) -> None:
        if not isinstance(id_cliente, int):
            raise ClienteError("El ID debe ser numérico.")
        self.__id_cliente = id_cliente

    def __set_nombre(self, nombre: str) -> None:
        if not nombre.strip():
            raise ClienteError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    def __set_email(self, email: str) -> None:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ClienteError("Formato de email inválido.")
        self.__email = email

    def get_info(self) -> str:
        return f"Cliente {self.__id_cliente}: {self.__nombre} ({self.__email})"