# Módulo de Gestión de Servicios (RF-04, RF-05, RF-06)

servicios = []

def registrar_servicio(id_servicio, nombre, precio, duracion_minutos):
    servicio = {
        "id": id_servicio,
        "nombre": nombre,
        "precio": precio,
        "duracion": duracion_minutos
    }
    servicios.append(servicio)
    return servicio

def consultar_servicios():
    return servicios