from pprint import pprint
from ejer_wc import Wc

w = Wc('/home/fer/codigo/Proyecto WC/dos.html')
try:
    print(w.estadisticas())
except Exception as e:
    print(e)