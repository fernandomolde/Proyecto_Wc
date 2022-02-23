
def cambia(cadena,basura):
 for c in basura:
    cadena.replace(c,'')
    return cadena





vacio = ' paco'
basura = '",;.:!¡¿?-_'
cadena = 'hola,.:paco'

print(cambia(cadena,basura))
print(vacio.replace('hola','paco')   