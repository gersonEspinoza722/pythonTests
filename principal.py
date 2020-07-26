#Hora de creación: 6:32 p.m., 10/10/2019
#Última hora de modificiación:
#Versión 3.7.2

#Librería
from tkinter import *
from functools import partial
from tkinter import messagebox
import random

#--------------------------------------------------------------Variables Globales------------------------------------------------------------#

matriz = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
          [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]

playing = "A"

archivo = []
fichas = []

jugador1 = []
jugador2 = []

puntos1 = 0
puntos2 = 0

config1 = []
config2 = []

actual = ""
palabra = ''
posicion = []

numeroTurno = 1

totalFichas = 0

proceso = 0
proceso2 = 0
proceso3 = 0

#--------------------------------------------------------------Funciones Generales------------------------------------------------------------#

def llamarVentana(abrir,cerrar):
    """
    Función: Abre y cierra ventanas.
    Entrada: La ventana que se cierra y la que ese abre.
    Salida: Cierra la ventana que esta abierta y abre la que se indicó.
    """
    cerrar.withdraw()
    abrir.deiconify()
    
    pegarUsu1 = cuadroJugador1.get()
    if len(pegarUsu1) >= 5:
        vNombre1.set(pegarUsu1[:5])
    if len(pegarUsu1) < 5:
        vNombre1.set(pegarUsu1+ "_"*(5 - len(pegarUsu1)))
    pegarUsu2 = cuadroJugador2.get()
    if len(pegarUsu2) >= 5:
        vNombre2.set(pegarUsu2[:5])
    if len(pegarUsu2) < 5:
        vNombre2.set(pegarUsu2+ "_"*(5 - len(pegarUsu2)))
    
    
#------------------------------------------------------------------Funciones------------------------------------------------------------------#

def leerArchivo():
    """
    Función: Lee el archivo de las letras.
    Entrada: Recibe el arcivo.
    Salida: Devuelve un mensaje si no encuentra el archivo y sino continua.
    """
    global archivo
    try:
        f = open("letras.txt", "r")
        archivo = f.read()
        archivo = archivo.splitlines()
        f.close()
    except:
        mensaje = "No se ha encontrado el archivo"
        messagebox.showinfo("Error", mensaje)

def letras():
    """
    Función: Lee LeerArchivo y modifica.
    Entrada: Recibe la funcion.
    Salida: Devuelve el archivo modificado. 
    """
    global archivo
    global fichas
    global totalFichas
    for i in range(len(archivo)):
        archivo[i] = archivo[i].split(",")
        archivo[i][2] = archivo[i][2][0]
    for j in archivo:
        fichas += [j[0]]*eval(j[1])
        totalFichas += int(j[1])

def listaPuntos():
    """
    Función: Modifica un poco más el archivo.
    Entrada: Recibe el archivo.
    Salida: Lo devuelve en forma correcta para colocarlo en la lista de Tkinter.
    """
    global archivos
    for j in archivo:
        lista.insert(END,str(j[0] + ' = ' + j[2][0]))

def segundos(contador=30):
    """
    Función: Reloj que determina el tiempo del jugador.
    Entrada: Recibe el contador que inicia en 30.
    Salida: Devuelve el tiempo.
    """
    global proceso, mostrarTi2
    mostrarTi2['text'] = contador
    proceso = mostrarTi2.after(1000, segundos, (contador-1))
    if contador == 0:
        mostrarTi2.after_cancel(proceso)
        segundos()
        ImaFunction()

def iniciar(contador=0,contador1=0):
    """
    Función: Reloj que determina el tiempo de la partida.
    Entrada: Recibe el contador que inicia 0.
    Salida: Devuelve el tiempo.
    """
    global proceso3
    global proceso2

    if contador == 60:
        contador = 0
        contador1 += 1

    if contador1 == 16:
        return ""

    mostrarTi1['text'] = str(contador1) + ":" + str(contador)
    proceso3 = mostrarTi1.after(1000, iniciar, (contador+1),(contador1))
        
def multiplicadores():
    """
    Función: Coloca los multiplicadores en forma ramdon.
    Entrada: Recibe la global de la matriz creada.
    Salida: Devuelve la matriz modificada con los multiplicadores.
    """
    #2 = multi por letra
    #3 = multi por palabra
    global matriz
    contador = 1
    while contador <= 10:
        random1 = random.randint(0,14)
        random2 = random.randint(0,14)
        if matriz[random1][random2][0] == 0:
            matriz[random1][random2][0] = 2
            contador += 1
    contador = 0
    num = random.randint(2,6)
    while contador < num:
        random1 = random.randint(0,14)
        random2 = random.randint(0,14)
        if matriz[random1][random2][0] == 0:
            matriz[random1][random2][0] = 3
            contador += 1
    return matriz

def cambiar (x,y,boton):
    """
    Función: Activa y desactiva los botones al cambiar de turno, con sus validaciones por si colocan la letra mal.
    Entrada: Recibe las letras en forma ramdon.
    Salida: Devuelve que se activen y desactiven los botones, junto con las validaciones.
    """
    global matriz
    global actual
    global posicion
    global numeroTurno
    if actual != '':
        if revisarJuego() == True:
            matriz[y][x][1] = actual
            boton.config(state = "disable", text = actual)
            posicion += [[y,x]]
            actual = ""
        elif numeroTurno >= 1 and matriz[y][x + 1][1] != 0:
            matriz[y][x][1] = actual
            boton.config(state = "disable",text = actual)
            posicion += [[y,x]]
            actual = ""
        elif numeroTurno >= 1 and matriz[y][x - 1][1] != 0:
            matriz[y][x][1] = actual
            boton.config(state = "disable",text = actual)
            posicion += [[y,x]]
            actual = ""
        elif numeroTurno >= 1 and matriz[y + 1][x][1] != 0:
            matriz[y][x][1] = actual
            boton.config(state = "disable",text = actual)
            posicion += [[y,x]]
            actual = ""
        elif numeroTurno >= 1 and matriz[y - 1][x][1] != 0:
            matriz[y][x][1] = actual
            boton.config(state = "disable",text = actual)
            posicion += [[y,x]]
            actual = ""
        else:
            mensaje = "Coloque la ficha en una posicición válida"
            messagebox.showinfo("Error", mensaje)      
    else:
        mensaje = "Seleccione una letra"
        messagebox.showinfo("Error", mensaje)

def revisarJuego():
    """
    Función: Verifica la matriz.
    Entrada: Recibe la matriz. 
    Salida: Devuelve la matriz.
    """
    global matriz
    for i in matriz:
        for j in i:
            if j[1] != 0:
                return False
    return True
        
def imprimirMatriz():
    """
    Función: Se encarga de imprimir la matriz de juego.
    Entrada: Recibe la matriz sin editar.
    Salida: Devuelve la matriz editada.
    """
    global matriz
    for i in matriz:
        print(i)

def fichasJugador1():
    """
    Función: Coloca de forma ramdon letras en los botones.
    Entrada: Recibe los botones y las letras.
    Salida: Devuelve los botones con las letras.
    """
    global jugador1
    global fichas
    for i in range(7 - len(jugador1)):
        num = random.randint(0, len(fichas)-1)
        jugador1 += [fichas[num]]
        fichas.remove(fichas[num])

def funcionJugador1(letra,boton):
    """
    Función: Borra la letra usada.
    Entrada: Recibe la letra junto con el boton.
    Salida: Devuelve el boton con otra letra.
    """
    global actual
    global palabra
    global jugador1
    palabra += letra
    actual = letra
    jugador1.remove(letra)
    boton.config(state = "disable")
     
def botonesJugador1():
    """
    Función: Crea los botones.
    Entrada: Nada.
    Salida: Los botones colocados en la interfaz.
    """
    global config1
    x = [100,130,160,190,220,250,280]
    for i in range(len(jugador1)):
        disponible1 = Button(scrabble3, width = "2", height = "1")
        disponible1.config(state = "normal", text = jugador1[i], command = partial(funcionJugador1, jugador1[i],disponible1))
        disponible1.place (x = x[i], y = 512)
        config1.append(disponible1)

def fichasJugador2():
    """
    Función: Coloca de forma ramdon letras en los botones.
    Entrada: Recibe los botones y las letras.
    Salida: Devuelve los botones con las letras.
    """
    global jugador2
    global fichas
    for i in range(7 - len(jugador2)):
        num = random.randint(0, len(fichas)-1)
        jugador2 += [fichas[num]]
        fichas.remove(fichas[num])

def funcionJugador2(letra,boton):
    """
    Función: Borra la letra usada.
    Entrada: Recibe la letra junto con el boton.
    Salida: Devuelve el boton con otra letra.
    """
    global actual
    global palabra
    global jugador2
    palabra += letra
    actual = letra
    jugador2.remove(letra)
    boton.config(state = "disable")
     
def botonesJugador2():
    """
    Función: Crea los botones.
    Entrada: Nada.
    Salida: Los botones colocados en la interfaz.
    """
    global config2
    x2 = [960, 990, 1020, 1050, 1080, 1110, 1140]
    for i in range(len(jugador2)):
        disponible2 = Button(scrabble3, width = "2", height = "1")
        disponible2.config(state = "normal", text = jugador2[i], command = partial(funcionJugador2, jugador2[i],disponible2))
        disponible2.place (x = x2[i], y = 512)
        config2.append(disponible2)

def contarPuntos():
    """
    Función: Cuenta los puntos de cada jugador.
    Entrada: Recibe todas las globales necesarias para poder realizar el proceso.
    Salida: Devuelve la cantidad de puntos que tiene cada jugador.
    """
    global palabra
    global archivo
    global posicion
    global matriz
    try:
        pos = [posicion[0]]
        coordenadas = pos
    except:
        return
    
    #   PARA ABAJO
    if type(matriz[pos[0][0]+1][pos[0][1]][1]) == str :
        for i in range(1, 15 - pos[0][0]):
            try:
                if type(matriz[i + pos[0][0]][pos[0][1]][1]) == str:
                    coordenadas += [[pos[0][0]+i,pos[0][1]]]
                else:
                    break
            except:
                pass
        for i in range(1, 15 - pos[0][0]):
            try:
                if type(matriz[pos[0][0]-i][pos[0][1]][1]) == str and pos[0][0]- 1 >= 0:
                    coordenadas += [[pos[0][0] - i,pos[0][1]]]
                else:
                    break
            except:
                pass
            
    #   PARA ARRIBA
    elif type(matriz[pos[0][0] - 1][pos[0][1]][1]) == str :
        for i in range(1, 15 - pos[0][0]):
            try:
                if type(matriz[pos[0][0]-i][pos[0][1]][1]) == str and pos[0][0]- 1 >= 0:
                    coordenadas += [[pos[0][0] - i,pos[0][1]]]
                else:
                    break
            except:
                pass
        for i in range(1, 15 - pos[0][0]):
            try:
                if type(matriz[i + pos[0][0]][pos[0][1]][1]) == str:
                    
                    coordenadas += [[pos[0][0]+i,pos[0][1]]]
                else:
                    break
            except:
                pass
    #  PARA IZQUIERDA
    elif type(matriz[pos[0][0]][pos[0][1] + 1][1]) == str :
        for i in range(1, 15 - pos[0][0]):
            try:
                if type(matriz[pos[0][0]][pos[0][1]+i][1]) == str:
                    coordenadas += [[pos[0][0],pos[0][1] + i]]
                else:
                    break
            except:
                pass
        for i in range(1, 15 - pos[0][0]):
            try:
                if type(matriz[pos[0][0]][pos[0][1]-i][1]) == str and pos[0][1] - i >= 0:
                    coordenadas += [[pos[0][0],pos[0][1] - i]]
                else:
                    break
            except:
                pass
    # PARA DERERECHA
    elif type(matriz[pos[0][0]][pos[0][1] - 1][1]) == str :
        for i in range(1, 15 - pos[0][0]):
            try:
                if type(matriz[pos[0][0]][pos[0][1]-i][1]) == str and pos[0][1] - i >= 0:
                    coordenadas += [[pos[0][0],pos[0][1] - i]]
                else:
                    break
            except:
                pass
        for i in range(1, 15 - pos[0][0]):
            try:
                if type(matriz[pos[0][0]][pos[0][1]+i][1]) == str:
                    
                    coordenadas += [[pos[0][0],pos[0][1] + i]]
                else:
                    break
            except:
                pass

    final = []
    for a in coordenadas:
        if a not in final:
            final += [a]
            
    total = [0, ""]
    # CONTAR LOS PUNTOS
    for j,k in final:
        total[1] += matriz[j][k][1]
        if matriz[j][k][0] == 2:
            total += ["Letra"]
            for l in archivo:
                if matriz[j][k][1] == l[0]:
                    total[0] += int(l[2])*2
        else:
            for l in archivo:
                if matriz[j][k][1] == l[0]:
                    total [0] += int(l[2])
    for m,n in final:
        if matriz[m][n][0] == 3:
            total[0] = total[0]*2
            total += ["Palabra"]
    posicion = []
    return total

def ImaFunction():
    """
    Función: Funcion principal que se combina con el boton de finalizar turno.
    Entrada: Recibe todo lo necesario para que la funcion continue.
    Salida: Devuelve una gran cantidad de procedimientos.
    """
    global config1
    global config2
    global numeroTurno
    global playing
    global posicion
    global puntos1
    global puntos2
    global proceso
    numeroTurno += 1
    total.config(text = numeroTurno)
    juego = contarPuntos()
    mostrarTi2.after_cancel(proceso)
    segundos()
    if playing == "A":
        cantidadFichas()
        minTurno()
        try:
            puntos1 += juego[0]
            texto(juego)
            verpuntosA = puntos1
            varPuntajeA.set(verpuntosA)
        except:
            pass
        numeJugador.config(text = playing)
        for i in config2:
            i.config(state = "normal")
        fichasJugador1()
        botonesJugador1()
        for j in config1:
            j.config(state = "disable")
        fichasJugador2()
        botonesJugador2()
        playing = "B"
        return
    if playing == "B":
        cantidadFichas()
        minTurno()
        try:
            puntos2 += juego[0]
            texto(juego)
            verpuntosB = puntos2
            varPuntajeB.set(verpuntosB)
        except:
            pass
        numeJugador.config(text = playing)
        for i in config1:
            i.config(state = "normal")
        fichasJugador2()
        botonesJugador2()
        for j in config2:
            j.config(state = "disable")
        fichasJugador1()
        botonesJugador1()
        playing = "A"
        return

def bitacora(n = "Comienzo del juego: \n"):
    """
    Función: Crea la bitacora.
    Entrada: Recibe nada
    Salida: Devuelve el archivo creado.
    """
    f = open("Bitácora.txt", "w")
    f.write(n)
    f.close()

def texto(dato):
    """
    Función: Añade texto a la bitacora.
    Entrada: Recibe nada.
    Salida: Devuelve nada.
    """
    x = open("Bitácora.txt", "r")
    argumento = x.read()
    x.close()
    return continuar(argumento, dato)

def continuar(argumento, dato):
    """
    Función: Ve las palabras que se forman.
    Entrada: Recibe el numero del turno.
    Salida: Devuelve la bitacora.
    """
    global numeroTurno
    global playing
    if "Palabra" in dato and "Letra" in dato:
        argumento += "Turno " + str(numeroTurno - 1) + " Jugador " + playing + " Usando: " + dato[1] + " - " + str(dato[0]) + " Multiplicador de palabra y letra\n"
    elif "Palabra" in dato:
        argumento += "Turno " + str(numeroTurno - 1)+ " Jugador " + playing + " Usando: " + dato[1] + " - " + str(dato[0]) + " Multiplicador de palabra\n"
    elif "Letra" in dato:
        argumento += "Turno " + str(numeroTurno - 1)+ " Jugador " + playing + " Usando: " + dato[1] + " - " + str(dato[0]) + " Multiplicador de letra\n"
    else: 
        argumento += "Turno " + str(numeroTurno - 1)+ " Jugador " + playing + " Usando: " + dato[1] + " - " + str(dato[0]) + "\n"
    return bitacora(argumento)

def cantidadFichas():
    """
    Función: Ve el total de ficas que quedan.
    Entrada: Las letras que se utilizan.
    Salida: Devuelve las fichas faltantes.
    """
    global totalFichas
    global fichas
    if (len(fichas)*100)/totalFichas <= 30:
        return ganador()
    
def ganador():
    """
    Función: Ve quien gano.
    Entrada: Recibe los puntos de cada jugador.
    Salida: Devuelve el ganador.
    """
    global puntos1
    global puntos2
    if puntos1 > puntos2:
        mensaje = "El jugador A ha ganado!"
        messagebox.showinfo("Felicidades", mensaje)
    elif puntos2>puntos1:
        mensaje = "El jugador B ha ganado!"
        messagebox.showinfo("Felicidades", mensaje)
    else:
        mensaje = "No hubo ganador"
        messagebox.showinfo("Lástima", mensaje)    
    
def minTurno():
    """
    Función: Ve la cantidad de turnos que se llevan.
    Entrada: Recibe la cantidad de turnos.
    Salida: Devuelve el ganador.
    """
    global numeroTurno
    if numeroTurno > 20:
        return ganador()

#-------------------------------------------------------------------Html-----------------------------------------------------------------------#

def crearHTML():
    """
    Funcion: Crea un archivo en html, sobre las reglas del juego
    Entrada:  Recibe la información
    Salida: Devuelve un html con todas las reglas
    """
    html = open("Create The Word.html","a")
    iniPag= "<!DOCTYPE html><html><head><meta charset= ""><title bgcolor =#FBFCFC  >Create The Word</title>"+\
            "</head><body bgcolor = #31A5ED><h1>Create The Word</h1><hr/><h2>Reglas a seguir:</h2>"+\
            "<p>Create The Word es un juego de palabras clásico y divertido. "+\
            "El objetivo del juego es obtener la mayor cantidad de puntos al formar palabras en un tablero que se conecten a las palabras creadas por los otros jugadores. "+\
            "Para jugar CTW, necesitas al menos otro jugador. También necesitarás un tablero de CTW oficial con todos sus componentes. "+\
            "Al jugar el juego, crearás palabras, acumularás puntos, desafiarás a tus oponentes. "+\
            "Al mismo tiempo, un anotador calculará los puntos de cada jugador para determinar quién ganará al final del juego. "+\
            "Si te conviertes en un fanático del juego, puedes considerar la posibilidad invitar a tus amigos a jugar regularmente.</p>"+\
            "<ol><li>Ingrese un nombre que no pase los 5 caracteres</li><li>Siempre inicia el jugador A</li><li>El juego en total dura 15 minutos </li>"+\
            "<li>El turno de cada jugador es de 30 segundos</li><li>La lista que se cuentra a la izquierda son los puntos que vale cada letra</li>"+\
            "<li>Se le dara a cada jugador 7 fichas ramdon para jugar</li><li>Abran multiplicadores de puntos escondidos por el tablero</li>"+\
            "<li>Cada vez que forme una palabra se sumaran puntos</li><li>Si cayo sobre un multiplicador te daran más puntos</li>"+\
            "<li>Siempre jugar de forma que las letras se encuntren unidas</li><li>Si se rinde un jugador gana automáticamente el otro jugador</li>"+\
            "<li>Si al final de las partida gana el jugador con más puntos</li></ol>"
    
    html.write(iniPag)
    final = "</body></head>"
    html.write(final)
    messagebox.showinfo("Buena Crack","El archivo se creo correctamente")
    html.close()
    return ""

#----------------------------------------------------------------Ventana #1--------------------------------------------------------------------#

scrabble1 = Tk()
scrabble1.title("Create The word")
scrabble1.geometry("1275x600")
scrabble1.resizable(FALSE,FALSE)
scrabble1.config(bg = 'dodgerblue2')
scrabble1.iconbitmap("control.ico")

miFrame1 = Frame(scrabble1)
miFrame1.pack(fill = "x")
miFrame1.config(bg = "white")
miFrame1.config(width = "300", height = "200")

imagenL1 = PhotoImage(file = "Logo.png")
iimagen1 = Label(scrabble1, image = imagenL1).place(x = 420, y = 70)


boton1Ventana1 = Button(scrabble1, text = "Jugar", font = ("Century Gothic", 20), command=lambda: llamarVentana(scrabble2,scrabble1))
boton1Ventana1.place(x = 580, y = 310)
boton1Ventana1.config(cursor = "hand2")

boton2Ventana1 = Button(scrabble1, text = "Como Jugar", font = ("Century Gothic", 20), command=lambda: crearHTML())
boton2Ventana1.place(x = 535, y = 440)
boton2Ventana1.config(cursor = "hand2")


#----------------------------------------------------------------Ventana #2--------------------------------------------------------------------#

scrabble2 = Tk()
scrabble2.title("Create The word")
scrabble2.geometry("1275x600")
scrabble2.resizable(FALSE,FALSE)
scrabble2.config(bg = 'dodgerblue2')
scrabble2.iconbitmap("control.ico")
scrabble2.withdraw()

miFrame2 = Frame(scrabble2)
miFrame2.pack(fill = "x")
miFrame2.config(bg = "white")
miFrame2.config(width = "300", height = "200")

miLabe21 = Label(miFrame2, text = "Crear dos Jugadores", fg = "dodgerblue2", font = ("Century Gothic", 45), bg = "white").place(x = 330, y = 54)

jugadorLabel = Label(scrabble2, text = "Ingrese el jugador A:", font = ("Century Gothic", 20), bg = "dodgerblue2")
jugadorLabel.place(x = 250, y = 280)

jugadorLabel = Label(scrabble2, text = "Ingrese el jugador B:", font = ("Century Gothic", 20), bg = "dodgerblue2")
jugadorLabel.place(x = 250, y = 380)

boton1Ventana2 = Button(scrabble2, text = "Continuar", font = ("Century Gothic", 20), command=lambda: llamarVentana(scrabble3,scrabble2))
boton1Ventana2.place(x = 580, y = 480)
boton1Ventana2.config(cursor = "hand2")

cuadroJugador1 = Entry(scrabble2, font = ("Century Gothic", 18))
cuadroJugador1.place(x = 800, y = 280)

cuadroJugador2 = Entry(scrabble2, font = ("Century Gothic", 18))
cuadroJugador2.place(x = 800, y = 380)

#----------------------------------------------------------------Ventana #3-------------------------------------------------------------------#

scrabble3 = Tk()
scrabble3.title("Create The word")
scrabble3.geometry("1275x600")
scrabble3.resizable(FALSE,FALSE)
scrabble3.config(bg = 'dodgerblue2')
scrabble3.iconbitmap("control.ico")
scrabble3.withdraw()

miFrame3 = Frame(scrabble3)
miFrame3.pack(fill = "x")
miFrame3.config(bg = "white")
miFrame3.config(width = "300", height = "30")

miLabe21 = Label(miFrame3, text = "Create The Word", fg = "dodgerblue2", font = ("Century Gothic", 10), bg = "white").place(x = 570, y = 2)

boton1Ventana3 = Button(scrabble3, text = "Finalizar Turno", font = ("Century Gothic", 10), command = lambda: ImaFunction())
boton1Ventana3.place(x = 580, y = 530)
boton1Ventana3.config(cursor = "hand2")

boton1Ventana3 = Button(scrabble3, text = "Terminar Partida", font = ("Century Gothic", 9), bg = "red", command = partial(ganador))
boton1Ventana3.place(x = 1070, y = 120)
boton1Ventana3.config(cursor = "hand2")

boton1Ventana3 = Button(scrabble3, text = "Imprimir Matriz", font = ("Century Gothic", 9),command = partial(imprimirMatriz))
boton1Ventana3.place(x = 950, y = 120)
boton1Ventana3.config(cursor = "hand2")

jugadorLetra1 = Label(scrabble3, text = "Jugador A:", font = ("Century Gothic", 20), bg = "dodgerblue2")
jugadorLetra1.place(x = 90, y = 450)

vNombre1 = StringVar(scrabble3)
vNombre1.set("Anónimo")
jugadorNombre1 = Label(scrabble3, font = ("Century Gothic", 20), bg = "dodgerblue2", textvariable = vNombre1)
jugadorNombre1.place(x = 240, y = 450)
labelLetras1 = Label(scrabble3, bg = "red", width = 31, height = 3)
labelLetras1.place(x = 92, y = 500)

jugadorLetra2 = Label(scrabble3, text = "Jugador B:", font = ("Century Gothic", 20), bg = "dodgerblue2")
jugadorLetra2.place(x = 950, y = 450)
vNombre2 = StringVar(scrabble3)
vNombre2.set("Anónimo")
jugadorNombre2 = Label(scrabble3, font = ("Century Gothic", 20), bg = "dodgerblue2", textvariable = vNombre2)
jugadorNombre2.place(x = 1100, y = 450)
labelLetras2 = Label(scrabble3, bg = "red", width = 31, height = 3)
labelLetras2.place(x = 952, y = 500)

turno = Label(scrabble3, text = "Turno:", font = ("Century Gothic", 15), bg = "dodgerblue2")
turno.place(x = 445, y = 65)
total = Label(scrabble3, text = numeroTurno , font = ("Century Gothic", 15), bg = "dodgerblue2")
total.place(x = 510, y = 65)

jugador = Label(scrabble3, text = "Jugador:", font = ("Century Gothic", 15), bg = "dodgerblue2")
jugador.place(x = 695, y = 65)
numeJugador = Label(scrabble3, text = playing, font = ("Century Gothic", 15), bg = "dodgerblue2")
numeJugador.place(x = 790, y = 65)

puntosJu1 = Label(scrabble3, text = "Puntos del jugador A:", font = ("Century Gothic", 13), bg = "dodgerblue2")
puntosJu1.place(x = 90, y = 190)
varPuntajeA=StringVar(scrabble3)
varPuntajeA.set(0)
lospuntos1 = Label(scrabble3, textvariable=varPuntajeA , font = ("Century Gothic", 16), bg = "dodgerblue2")
lospuntos1.place(x = 160, y = 240)

puntosJu2 = Label(scrabble3, text = "Puntos del jugador B:", font = ("Century Gothic", 13), bg = "dodgerblue2")
puntosJu2.place(x = 90, y = 290)
varPuntajeB=StringVar(scrabble3)
varPuntajeB.set(0)
lospuntos2 = Label(scrabble3, textvariable=varPuntajeB, font = ("Century Gothic", 16), bg = "dodgerblue2")
lospuntos2.place(x = 160, y = 340)

tiempoTotal = Label(scrabble3, text = "Tiempo de la partida:", font = ("Century Gothic", 15), bg = "dodgerblue2")
tiempoTotal.place(x = 950, y = 190)
mostrarTi1 = Label(scrabble3, text = "15:00", font = ("Century Gothic", 16), bg = "dodgerblue2")
mostrarTi1.place(x = 1035, y = 240)

tiempoTota2 = Label(scrabble3, text = "Tiempo para finalizar turno:", font = ("Century Gothic", 12), bg = "dodgerblue2")
tiempoTota2.place(x = 950, y = 290)
mostrarTi2 = Label(scrabble3, text = "000", font = ("Century Gothic", 16), bg = "dodgerblue2")
mostrarTi2.place(x = 1035, y = 340)

lista = Listbox(scrabble3, width = 5, height = 20)
lista.place(x = 280, y = 120)

x = [445, 470, 495, 520, 545, 570, 595, 620, 645, 670, 695, 720, 745, 770, 795]
y = [120, 145, 170, 195, 220, 245, 270, 295, 320, 345, 370, 395, 420, 445, 470]
for i in range(len(x)):
    for j in range(len(y)):
        ficha = Button(scrabble3, width = "2", height = "1")
        ficha.config(cursor = "hand2", command = partial(cambiar,i,j,ficha))
        ficha.place(x = x[i], y = y[j])

multiplicadores()
leerArchivo()
letras()
fichasJugador1()
fichasJugador2()
botonesJugador1()
botonesJugador2()
listaPuntos()
bitacora()
segundos()
iniciar()
if numeroTurno == 1:
    for i in config2:
        i.config(state = "disable")
        
mainloop()
