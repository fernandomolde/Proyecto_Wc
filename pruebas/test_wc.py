
from logging import exception
import unittest
from ejer_wc import Wc

class Testwc(unittest.TestCase):
    maxDiff = None
    def test_existe_wc(self):
        w = Wc('/home/fer/codigo/Proyecto WC/README.md')
        self.assertIsNotNone(w)

    def test_validar_archivo_texto_es_correcto(self):
        w = Wc('/home/fer/codigo/Proyecto WC/uno.html')
        resp = w._Wc__validar_archivo()
        self.assertEqual(resp,True)

    def test_validar_archivo_texto_es_incorrecto(self):
        w = Wc('/home/fer/codigo/Proyecto WC/core-i7.jpg')
        resp = w._Wc__validar_archivo()
        self.assertEqual(resp,False)
        
    def test_validar_archivo_inexistente_es_incorrecto(self):
        w = Wc('/home/fer/codigo/Proyecto WC/core-i7.jpg')
        resp = w._Wc__validar_archivo()
        self.assertEqual(resp,False)

    def test_abrir_archivo_correcto(self):
        html = """hola 
caracola adasdasda"""
        w = Wc('/home/fer/codigo/Proyecto WC/uno.html')
        w._Wc__abrir_archivo()
        self.assertEqual(w._Wc__contenido,html)

    def test_abrir_archivo_inexistente_da_error(self):
        w = Wc('/home/fer/ggg')
        with self.assertRaises(Exception):
            w._Wc__abrir_archivo()
        
    def test_contar_lineas_correcto(self):
        html = """hola 
caracola adasdasda"""
        w = Wc('/home/fer/codigo/Proyecto WC/uno.html')
        w._Wc__abrir_archivo()
        w._Wc__contar_lineas()
        self.assertEqual(w._Wc__cont_lineas,2)
    
    def test_cadena_a_texto_limpio(self):
        w = Wc('/home/fer/codigo/Proyecto WC/uno.html')
        txt = """hola\ncaracola\nadasdasda\nadasdassd\nasdasdsdasdda\nEN"""
        w._Wc__abrir_archivo()
        resp = w._Wc__limpiar_cadena()
        self.assertEqual(w._Wc__contenido,txt)

    def test_texto_limpio_contar_palabras(self):
        w = Wc('/home/fer/codigo/Proyecto WC/uno.html')
        txt = """hola\ncaracola\nadasdasda\nadasdassd\nasdasdsdasdda\nEN"""
        w._Wc__abrir_archivo()
        w._Wc__limpiar_cadena()
        w._Wc__contar_palabras()
        self.assertEqual(w._Wc__contar_palabras,5)

    def test_texto_limpio_contar_palabras(self):
        w = Wc('/home/fer/codigo/Proyecto WC/dos.html')
        txt = """hola\ncaracola\nadasdasda\nadasdassd\nasdasdsdasdda\nEN"""
        w._Wc__abrir_archivo()
        w._Wc__limpiar_cadena()
        w._Wc__frecuencias()

        self.assertEqual(w._Wc__ocurrencias,{'uno':1, 'dos':2, 'tres':3})


    