# Utilizando diccionarios se asigna un valor incial a las 3 notas de cada estudiante
estudiante1 = {'Nota1': 5, 'Nota2': 5, 'Nota3': 5}
estudiante2 = {'Nota1': 5, 'Nota2': 5, 'Nota3': 5}
estudiante3 = {'Nota1': 5, 'Nota2': 5, 'Nota3': 5}
estudiante4 = {'Nota1': 5, 'Nota2': 5, 'Nota3': 5}
estudiante5 = {'Nota1': 5, 'Nota2': 5, 'Nota3': 5}

# Se crea un diccionario vacio donde estara los promedios de cada estudiante
estudiantes = {}

#Se asigna como variable los porcentajes de las notas 35% y 30%
porcentaje1 = 0.35
porcentaje2 = 0.30

#Se crean los valores de los promedios de los estudiantes tomando la suma de las 3 notas y diviendo entre 3
estudiantes['promedio1'] = sum(estudiante1.values()) / 3
estudiantes['promedio2'] = sum(estudiante1.values()) / 3
estudiantes['promedio3'] = sum(estudiante1.values()) / 3
estudiantes['promedio4'] = sum(estudiante1.values()) / 3
estudiantes['promedio5'] = sum(estudiante1.values()) / 3
print(estudiantes)
promediocurso = sum(estudiantes.values()) / 5
print("El promedio del curso es:")
print(promediocurso)


#
print("\nIngrese la primera nota")
Nota1 = input()
estudiante1['Nota1'] = float(Nota1) * porcentaje1
print(estudiante1)
print("Ingrese la segunda nota")
Nota2 = input()
estudiante1['Nota2'] = float(Nota2) * porcentaje1
print(estudiante1)
print("Ingrese la tercera nota")
Nota3 = input()
estudiante1['Nota3'] = float(Nota3) * porcentaje2
print(estudiante1)
print("El promedio del estudiante es:")
print(estudiantes['promedio1'])