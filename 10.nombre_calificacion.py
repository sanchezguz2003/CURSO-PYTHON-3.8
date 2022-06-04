nombre_alumno = input("anotar el nombre del alumno: ")
calificacion = int(input("anota la calificacion: "))
mensaje = None

if 0 <= calificacion <= 69:
    mensaje = "insuficiente(N/A)"
elif 70 <= calificacion <= 74:
    mensaje = "suficiente"
elif 75 <= calificacion <= 84:
    mensaje = "bueno"
elif 85 <= calificacion <= 94:
    mensaje = "notable"
elif 95 <= calificacion <= 100:
    mensaje = "excelente"
else:
    mensaje = "calificacion no valida"
print(f"tienes {calificacion} y eso es", mensaje)
