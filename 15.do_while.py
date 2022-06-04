while True:
    nombre_alumno = input("anota el nombre del alumno:")
    apellidos_alumnos = input("anota el apellido paterno:")
    edad_alumno = input("anota la edad:")
    print(f"Alumno:{nombre_alumno},{apellidos_alumnos},{edad_alumno}registrado correctamente")
    condicion = input("¿desea hacer otro registro?(S=si N=no):")
    if condicion == "n" or condicion == "N":
        break
print("alumnos registrados correctamente")
