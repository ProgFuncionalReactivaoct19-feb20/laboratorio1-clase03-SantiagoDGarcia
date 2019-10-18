"""
	Problemas practicos 1
	@SantiagoDGarcia
"""
frase = "No hay medicina que cure lo que no cura la felicidad"
frase2 = frase.split(" ") 
def palabras(x):
	funcion = lambda x: len(x)>=2 and len(x)<=3, frase2
	if x in funcion:
		return True 
	else:
		return False
funNot = filter(palabras, frase2)
print(list(funNot))
# hay un minimo problema de impresion, error x

