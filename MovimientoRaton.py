laberinto= [
    0, 0, 0, 0, 
    0, 1, 1, 0,
    0, 1, 0, 0,
    0, 0, 0, 1,
]
#ubicacion inicial del raton y el queso
columna, fila  = raton
raton = (0,2)
queso = (1,3)


def derecha():
    global raton
    if columna < 3 and laberinto[(columna + 1)] != 1:
        raton = (columna + 1, fila)
        
def izquierda():
    global raton
    if columna > 0 and laberinto[(columna - 1)] != 1:
        raton = (columna - 1, fila)
        
def arriba():
    global raton
    if fila > 0 and laberinto[(fila - 1)] != 1:
        raton = (columna, fila - 1)
        
def abajo():
    global raton
    if fila < 3 and laberinto[(fila + 1)] != 1:
        raton = (columna, fila + 1)
