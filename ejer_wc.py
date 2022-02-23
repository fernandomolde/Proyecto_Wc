#Queremos un programa que dado un archivo nos devuelva los siguiente:
    #Número de líneas
    #Número de palabras
    #Ocurrencias de cada palabra
    #Hacer pruebas unitarias de todo

#Si el archivo es binario debe devolver un error indicándolo 
#Si el archivo está vacío debe devolver un resultado vacío      

# metodos : Abrir el archivo,leer el archivo,cuente el numero de lineas,cuente el numero de palabra,guardar en un diccionario



from logging import exception
import mimetypes
from attr import Attribute


class Wc():
    
    def __init__(self,archivo='') -> None:
        self.__archivo = archivo
        self.__cont_palabras = 0
        self.__cont_lineas = 0
        self.__ocurrencias = {}
        self.__contenido = ''
        self.__basura = '",;.:!¡¿?-_'

    
    def __validar_archivo(self): 
        mime = mimetypes.guess_type(self.__archivo)
        try:
            resp = mime[0].split('/')[0] == 'text'
            return resp
        except AttributeError:
            raise Exception('Archivo inexistente o inválido')

    def __abrir_archivo(self):
        try:
            if self.__validar_archivo():
                with open(self.__archivo,'r') as manejador:
                    texto = manejador.read()
                    if texto !='':
                        self.__contenido = texto
        
            else:
                raise Exception('El archivo no es de texto.')
        except Exception as e:
            raise e 

    def __contar_lineas(self):
        self.__cont_lineas = len(self.__contenido.split('\n'))

    def __contar_palabras(self):
        self.__cont_palabras = len(self.__contenido.split())

    def __limpiar_cadena(self):
        limpio = self.__contenido.lower()
        for c in self.__basura:
            limpio = limpio.replace(c,'')
        
        self.__contenido = limpio
    
    def __frecuencia(self):
        frec_palabras = {}
        lista = self.__contenido.split()
        for l in lista:
            if l in frec_palabras:
                frec_palabras[l] +=1
            else:
                frec_palabras = 1
        self.__ocurrencias = frec_palabras

    def estadisticas(self):
        #Abre el archivo, lo valida y lo lee
        self.__abrir_archivo()
        self.__limpiar_cadena()
        self.__contar_lineas()
        self.__contar_palabras()
        self.__frecuencia()

        salida = {
            'num_lineas': self.__cont_lineas,
            'num_palabras': self.__cont_palabras,
            'frecuencias': self.__ocurrencias

        }

        return salida
    


