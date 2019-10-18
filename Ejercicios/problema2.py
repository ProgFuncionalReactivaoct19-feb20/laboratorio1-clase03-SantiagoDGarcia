"""
	Problemas practicos 1
	@SantiagoDGarcia
"""
# Se ingresa n los valores
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
# se crea una funcion que vaya sumando los valores de la poscicion 0,1, y 2
funNot = lambda x: (x[0]+ x[1]+ x[2])
# se imprime los resultados en una lista
print(list(map(funNot, notas)))