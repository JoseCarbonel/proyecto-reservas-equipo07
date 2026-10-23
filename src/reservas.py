# Módulo de Gestión de Reservas (RF-07 al RF-11)

reservas = []

def registrar_reserva(id_reserva, cliente_id, servicio_id, fecha, hora):
    reserva = {"id": id_reserva, "estado": "PENDIENTE_CONFIRMACION"}
    reservas.append(reserva)
    return reserva

def cancelar_reserva(id_reserva):
    for reserva in reservas:
        if reserva["id"] == id_reserva:
            reserva["estado"] = "CANCELADA"
            return True
    return False