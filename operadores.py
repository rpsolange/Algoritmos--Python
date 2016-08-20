a= input("Primer numero: ")
b=input("Segundo numero: ")
print( "Suma de cadenas: ", a+b+str(0)) # si aca le pongo un +0 sale error porque el 0 es cadena y a y b aun son cadenas no nùmeros

a= int(a) #aca a y b ya son numero 
b= int(b)

suma= a+b
resta= a-b
multiplicacion= a*b
divReal= a/b
divEntera= a//b
resto= a%b
print( "Suma: ", suma)
print( "Resta: ", resta)
print( "Multiplicacion: ", multiplicacion)
print( "divReal: ", divReal)
print( "divEntera: ", divEntera)
print( "Resto: ", resto)