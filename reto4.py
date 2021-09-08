import os
import math

menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana",
"Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo",
"Elegir opción de menú favorita", "Cerrar sesión"]

coordenadas=[[],[],[]]

zonas_wifi=[[10.348, 10.171, 10.259, 10.350], [-73.051, -73.136, -73.069, -73.043], [0, 0, 67, 45]]

def iniciar_sesion():
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    usuario = 51656
    password = 65615

    usuario = int(input("Introduce el usuario: "))
    if usuario==51656:
        password = int(input("Introduce la contraseña: "))
        if password==65615:
            captcha1=656
            captcha2=6+6-5-1-1
            captchafinal=int(captcha1+captcha2)
            print("CAPTCHA", captcha1, "+", captcha2)
            captchain = int(input("Introduce el valor de la suma: "))
            if captchafinal==captchain:
                print("Sesión iniciada")
                cargar_menu(password)
                exit()
            else:
                print("Error")
                exit()
        else:
            print("Error")
            exit()
    else:
        print("Error")
        exit()

def cargar_menu(password):
    os.system('cls')
    print("",str("1."), menu[0], "\n",
    str("2."), menu[1], "\n",
    str("3."), menu[2], "\n",
    str("4."), menu[3], "\n",
    str("5."), menu[4], "\n",
    str("6."), menu[5], "\n",
    str("7."), menu[6], "\n",)
    print("Elija una opción")
    opcion = int(input())
    opciones_menu(password, opcion)

def opciones_menu(password, opcion):

    referencia = menu[opcion-1]

    if(referencia == "Cambiar contraseña"):
        cambio_de_contraseña(password)
    elif(referencia == "Ingresar coordenadas actuales"):
        ingresar_coordenadas(password)
    elif(referencia == "Ubicar zona wifi más cercana"):
        # print(f"Usted ha elegido la opción {opcion}")
        ubicar_zona_wifi_mas_cercana(password)
    elif(referencia == "Guardar archivo con ubicación cercana"):
        print(f"Usted ha elegido la opción {opcion}")
    elif(referencia == "Actualizar registros de zonas wifi desde archivo"):
        print(f"Usted ha elegido la opción {opcion}")
    elif(referencia == "Elegir opción de menú favorita"):
        opcion_favorita(password)
    elif(referencia == "Cerrar sesión"):
        os.system('cls')
        print("Hasta Pronto")
        exit()
    else:
        print("Error")
        contador = 0
        while (contador <= 1):
            print("Elija una opción")
            opcion = int(input())
            if(opcion > 7):
                contador = contador + 1
                print("Error")
            else:
                contador = 3

def opcion_favorita(password):
    print("Seleccione opción favorita")
    favorita = int(input())

    if (favorita <= 5):
        adivinanza(favorita,password)
    else:
        print("Error")
        exit()

def adivinanza(favorita,password):
    print("Para confirmar por favor responda: Los tienes en las manos y los tienes en los pies y en seguida sabrás qué número es.")
    adivinanza1 = int(input())

    if (adivinanza1 == 5):
        print("Para confirmar por favor responda: Si le sumas su hermano gemelo al tres, ya sabes cuál es.")
        adivinanza2 = int(input())
        if (adivinanza2 == 6):
            cambiar_menu(favorita,password)
        else:
            print("Error")
            cargar_menu(password)
    else:
        print("Error")
        cargar_menu(password)

def cambiar_menu(favorita,password):

    if(favorita <= 5):
        auxiliar = menu[favorita -1]
        menu[favorita -1] = menu[0]
        menu[0] = auxiliar
        cargar_menu(password)
    else:
        print("Error")
        exit()

def cambio_de_contraseña(password):

    print("Por favor ingrese su actual contraseña")
    contraseña = int(input())

    if(contraseña == password):
        print("Por favor ingrese la nueva contraseña")
        nueva_contraseña = int(input())
        if(nueva_contraseña != password):
            print("Por favor confirme la nueva contraseña")
            confirmar_contraseña = int(input())
            if(nueva_contraseña == confirmar_contraseña):
                password = nueva_contraseña
                cargar_menu(password)
            else:
                print("Error")
                exit()
        else:
            print("Error")
            exit()
    else:
        print("Error")
        exit()

def ingresar_coordenadas(password):
    os.system('cls')

    if len(coordenadas[0]) == 0:
        print("Ingresar coordenadas de los tres sitios que más frecuenta (Trabajo, Casa, Parque)")
        for x in range(3):
            latitud = float(input(f"Ingrese la Latitud {x+1}: "))
            if(latitud < 10.462 and latitud > 9.757):
                longitud = float(input(f"Ingrese longitud {x+1}: "))
                if(longitud > (-73.918) and longitud < (-72.987)):
                    coordenadas[x] = [latitud,longitud]
                else:
                    print("Error coordenada")
                    exit()
            else:
                print("Error coordenada")
                exit()
        cargar_menu(password)
    else:
        for x in range(3):
            print(f"Coordenadas [latitud,longitug] {x+1} : {coordenadas[x]}")

        latitudes  = [coordenadas[0][0],coordenadas[1][0],coordenadas[2][0]]
        longitudes = [coordenadas[0][1],coordenadas[1][1],coordenadas[2][1]]
        promedio_latitud, promedio_longitud = sum(latitudes)/3, sum(longitudes)/3

        norte, sur = latitudes.index(max(latitudes)), latitudes.index(min(latitudes))
        oriente, occidente = longitudes.index(max(longitudes)), longitudes.index(min(longitudes))
        # print(norte, sur, oriente, occidente)
        print(f"La coordenada {sur+1} es la que esta más al sur")
        print(f"La coordenada {occidente+1} es la que esta más al occidente")
        print(f"Coordenadas promedio de todos los puntos: latitud {promedio_latitud}, longitud {promedio_longitud}")
        print("Presione 1,2 o 3 para actualizar la respectiva coordenada")
        print("presione 0 para regresar al menu")

        numero_coordenada=int(input())
        if (numero_coordenada ==0 or numero_coordenada ==""):
            cargar_menu(password)
        else:
            if numero_coordenada == 1 or numero_coordenada == 2 or numero_coordenada == 3:
                latitud = float(input("Ingrese Latitud: "))
                if(latitud < 10.462 and latitud > 9.757):
                    longitud = float(input(f"Ingrese longitud: "))
                    if(longitud > (-73.918) and longitud < (-72.987)):
                        coordenadas[numero_coordenada-1][0] = latitud
                        coordenadas[numero_coordenada-1][1] = longitud
                        cargar_menu(password)
                    else:
                        print("Error coordenada")
                        exit()
                else:
                    print("Error coordenada")
                    exit()

            else:
                print("Error actualización")
                exit()

def ubicar_zona_wifi_mas_cercana(password):

    if (len(coordenadas[0]) == 0):
        print("Error sin registro de coordenadas")
        exit()
    else:
        for m in range(3):
            print(f"Coordenadas [latitud,longitug] {m+1} : {coordenadas[m]}")

        print("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión.")
        actual = int(input())

        if (actual > 0 and actual < 4):
            comparacion_lat1 = coordenadas[actual-1][0]
            comparacion_long1 = coordenadas[actual-1][1]
            calculos_distancia(comparacion_lat1, comparacion_long1, password)
        else:
            print("Error ubicación")
            exit()

def calculos_distancia(comparacion_lat1, comparacion_long1, password):
    radio = 6372
    distancias = []
    punto_actual =[]
    punto_actual.append(comparacion_lat1)
    punto_actual.append(comparacion_long1)

    for x in range(4):
        comparacion_lat2 = zonas_wifi[0][x]
        comparacion_long2 = zonas_wifi[1][x]
        tlat = math.radians((comparacion_lat2 - comparacion_lat1))
        tlong = math.radians((comparacion_long2 - comparacion_long1))
        antes = math.sin(tlat/2) * math.sin(tlat/2) + math.cos(math.radians(comparacion_lat1)) * math.cos(math.radians(comparacion_lat2)) * math.sin(tlong/2) * math.sin(tlong/2)
        despues = 2 * math.atan2(math.sqrt(antes), math.sqrt(1-antes))
        distancia = radio * despues
        distancias.append(distancia)


    #Busco inicialmente el indice de la menor distancia y luego asigno a menor distancia a una variable
    indice_menor_distancia = distancias.index(min(distancias))
    menor_distancia = distancias[indice_menor_distancia]
    # busco los datos de latitud, longitud y usuarios de la menor distancia
    zona_menor_latitud = zonas_wifi[0][indice_menor_distancia]
    zona_menor_longitud = zonas_wifi[1][indice_menor_distancia]
    zona_menor_usuarios = zonas_wifi[2][indice_menor_distancia]
    #Busco la mayor distancia y se la asigno a la menor para buscar la segunda menor
    indice_mayor_distancia = distancias.index(max(distancias))
    distancias[indice_menor_distancia] = distancias[indice_mayor_distancia]
    #Busco la segunda menor
    indice_2menor_distancia = distancias.index(min(distancias))
    menor_2_distancia = distancias[indice_2menor_distancia]
    # busco los datos de la segunda menor distancia, latitud, longitud y usuarios de la menor distancia
    zona_2_menor_latitud = zonas_wifi[0][indice_2menor_distancia]
    zona_2_menor_longitud = zonas_wifi[1][indice_2menor_distancia]
    zona_2_menor_usuarios = zonas_wifi[2][indice_2menor_distancia]
    # Finalmente borro los datos de la lista distancias
    distancias.clear()

    zonas_1_cercana = []
    zonas_2_cercana = []
    zonas_mas_cercanas = []
    if(zona_2_menor_usuarios > zona_menor_usuarios):
        # Agrego a la lista zonas_1_cercana los datos de la zona más cercana
        zonas_1_cercana.append(zona_menor_latitud)
        zonas_1_cercana.append(zona_menor_longitud)
        zonas_1_cercana.append(zona_menor_usuarios)
        zonas_1_cercana.append(menor_distancia)
        # Agrego a la lista zonas_2_cercana los datos de la segunda zona más cercana
        zonas_2_cercana.append(zona_2_menor_latitud)
        zonas_2_cercana.append(zona_2_menor_longitud)
        zonas_2_cercana.append(zona_2_menor_usuarios)
        zonas_2_cercana.append(menor_2_distancia)
        # Agrego a la variable zonas_mas_cercanas los datos de las 2 zonas más cercanas
        zonas_mas_cercanas.append(zonas_1_cercana)
        zonas_mas_cercanas.append(zonas_2_cercana)
        # print(zonas_mas_cercanas)
    else:
        # Agrego a la lista zonas_1_cercana los datos de la zona más cercana
        zonas_1_cercana.append(zona_2_menor_latitud)
        zonas_1_cercana.append(zona_2_menor_longitud)
        zonas_1_cercana.append(zona_2_menor_usuarios)
        zonas_1_cercana.append(menor_2_distancia)
        # Agrego a la lista zonas_2_cercana los datos de la segunda zona más cercana
        zonas_2_cercana.append(zona_menor_latitud)
        zonas_2_cercana.append(zona_menor_longitud)
        zonas_2_cercana.append(zona_menor_usuarios)
        zonas_2_cercana.append(menor_distancia)
        # Agrego a la variable zonas_mas_cercanas los datos de las 2 zonas más cercanas
        zonas_mas_cercanas.append(zonas_1_cercana)
        zonas_mas_cercanas.append(zonas_2_cercana)
        # print(zonas_mas_cercanas)

    print(f"La zona wifi 1: ubicada en ['{zonas_mas_cercanas[0][0]}', '{zonas_mas_cercanas[0][1]}'] a {zonas_mas_cercanas[0][3]} metros , tiene en promedio {zonas_mas_cercanas[0][2]}")
    print(f"La zona wifi 2: ubicada en ['{zonas_mas_cercanas[1][0]}', '{zonas_mas_cercanas[1][1]}'] a {zonas_mas_cercanas[1][3]} metros , tiene en promedio {zonas_mas_cercanas[1][2]}")

    print("Elija 1 o 2 para recibir indicaciones de llegada")
    opcion_indicaciones = int(input())

    ubicacion = []
    if(opcion_indicaciones < 3 and opcion_indicaciones > 0 ):
        if(opcion_indicaciones == 1):
            ubicacion.append(zonas_mas_cercanas[0][0])
            ubicacion.append(zonas_mas_cercanas[0][1])
            ubicacion.append(zonas_mas_cercanas[0][2])
            ubicacion.append(zonas_mas_cercanas[0][3])
            dar_direccion(ubicacion, punto_actual, password)
        elif(opcion_indicaciones == 2):
            ubicacion.append(zonas_mas_cercanas[1][0])
            ubicacion.append(zonas_mas_cercanas[1][1])
            ubicacion.append(zonas_mas_cercanas[1][2])
            ubicacion.append(zonas_mas_cercanas[1][3])
            dar_direccion(ubicacion, punto_actual, password)
    else:
        print("Error zona wifi")
        exit()

def dar_direccion(ubicacion, punto_actual, password):
    # Definimos el mensaje según la latitud y longitud
    if(punto_actual[0] < ubicacion[0]):
        if(punto_actual[1] < ubicacion[1]):
            print("Para llegar a la zona wifi dirigirse primero al norte y luego hacia el occidente")
        else:
            print("Para llegar a la zona wifi dirigirse primero al norte y luego hacia el oriente")
    else:
        if(punto_actual[1] < ubicacion[1]):
            print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente")
        else:
            print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el oriente")


    # Calculamos el tiempo que tardaria
    moto = 19.44
    carro = 20.83
    tiempo_moto = ubicacion[3] / moto
    tiempo_carro = ubicacion[3] / carro

    print(f"Tiempo en moto: {tiempo_moto}")
    print(f"Tiempo en auto: {tiempo_carro}")
    print()
    print("Presione 0 para salir")
    salida = int(input())

    if(salida == 0):
        cargar_menu(password)

# PROGRAMA PRINCIPAL
iniciar_sesion()