nombre_alumno = input("anota un nombre de alumno: ")


alumno1 = "Victor"
alumno2 = "Bruno"
alumno3 = "Diana"
alumno4 = "Cira"

matricula_alumno1 = "s21122001"
matricula_alumno2 = "s21122002"
matricula_alumno3 = "s21122003"
matricula_alumno4 = "s21122004"

if nombre_alumno == alumno1 or nombre_alumno == alumno2 or nombre_alumno == alumno3 or nombre_alumno == alumno4:
    print("bienvenido al curso de python")
    matricula_alumno = input("anota la matricula: ")
    if matricula_alumno == matricula_alumno1 or matricula_alumno == matricula_alumno2 or matricula_alumno == matricula_alumno3 or matricula_alumno == matricula_alumno4:
        print(f"matricula asignada a{nombre_alumno}")
    else:
        print("matricula no asignada")
else:
    print("alumno no registrada")

