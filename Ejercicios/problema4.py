"""
	Problemas practicos 1
	@SantiagoDGarcia
"""
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
# se ingresa una funcion de ntipo filtro que nos evalue los estudiantes que tengan notas buenas y regulares
resultado = filter(lambda x: x[3]=="Regular" or x[3]=="Bueno", notas)
# Se imprimen en una lista los resultados verdaderos o requeridos
print(list(resultado))