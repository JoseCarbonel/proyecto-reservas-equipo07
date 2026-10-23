# Módulo de Gestión de Clientes (RF-01, RF-02, RF-03)

clientes = []

def registrar_cliente(id_cliente, nombre, telefono):
    cliente = {"id": id_cliente, "nombre": nombre, "telefono": telefono}
    clientes.append(cliente)
    return cliente

def consultar_clientes():
    return clientes