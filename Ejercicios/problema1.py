"""
	Problemas practicos 1
	@SantiagoDGarcia
"""
#import promedios.txt
#from promedios.txt import *

notas = [10,20,18,19,20,17,18,16,16,11,12,13]
#datos = promedios.txt
#print(datos)
#datos = int
aprobados = filter(lambda x: x>=16.5, datos)
print (list(aprobados))

# El programa funciona correctamente, epro existe un error al importar el archivo de texto
# Mencionando que no se reconoce el modulo