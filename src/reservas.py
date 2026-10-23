# Módulo de Gestión de Reservas (RF-07 al RF-11)

reservas = []

def registrar_reserva(id_reserva, cliente_id, servicio_id, fecha, hora):
    if not hora:
        return "Error: La hora es obligatoria"
    reserva = {"id": id_reserva, "fecha": fecha, "hora": hora, "estado": "ACTIVA"}
    reservas.append(reserva)
    return reserva

def cancelar_reserva(id_reserva):
    for reserva in reservas:
        if reserva["id"] == id_reserva:
            reserva["estado"] = "CANCELADA"
            return True
    return False