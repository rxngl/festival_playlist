nombres=[]
artistas=[]
duraciones=[]
popularidades=[]

def agregar_canciones():

    cantidad=int(input("\n¿Cuantas canciones deseas agregar? "))

    for i in range(cantidad):

        print(f"\n--- Cancion {i + 1} ---")

        nombre=input("Nombre de la cancion: ")
        artista=input("Nombre del artista: ")

        duracion=float(input("Duracion en minutos: "))

        while duracion<=0:
            print("La duracion debe ser mayor a cero.")
            duracion=float(input("Duracion en minutos: "))

        popularidad=int(input("Popularidad (1-100): "))

        while popularidad < 1 or popularidad > 100:
            print("La popularidad debe estar entre 1 y 100")
            popularidad=int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

        print("Cancion agregada correctamente")

    print("\nRegistro completado!")

def ver_reportes():

    if len(nombres)==0:
        print("\nNo hay canciones registradas")
        return

    total_canciones=len(nombres)

    duracion_total=sum(duraciones)

    promedio=sum(popularidades) / total_canciones

    mayor=max(popularidades)
    menor=min(popularidades)

    posicion_mayor=popularidades.index(mayor)
    posicion_menor=popularidades.index(menor)

    print("\n========== REPORTES ==========")

    print(f"Total de canciones: {total_canciones}")

    print(f"Duracion total: {duracion_total:.2f} minutos")

    print(f"Promedio de popularidad: {promedio:.2f}")

    print("\n--- Cancion mas popular ---")
    print(f"Nombre: {nombres[posicion_mayor]}")
    print(f"Artista: {artistas[posicion_mayor]}")
    print(f"Popularidad: {mayor}")

    print("\n--- Cancion menos popular ---")
    print(f"Nombre: {nombres[posicion_menor]}")
    print(f"Artista: {artistas[posicion_menor]}")
    print(f"Popularidad: {menor}")

def buscar_canciones():

    if len(nombres)==0:
        print("\nNo hay canciones registradas")
        return

    print("\n========== BUSCAR CANCIONES ==========")
    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")

    opcion=input("Selecciona una opcion: ")

    if opcion=="1":

        busqueda=input("Nombre del artista: ").lower()

        encontrado=False

        for i in range(len(nombres)):

            if busqueda in artistas[i].lower():

                print("\nCancion encontrada:")
                print(f"Nombre: {nombres[i]}")
                print(f"Artista: {artistas[i]}")
                print(f"Duracion: {duraciones[i]} minutos")
                print(f"Popularidad: {popularidades[i]}")

                encontrado=True

        if encontrado==False:
            print("No se encontraron canciones de ese artista")

    elif opcion=="2":

        minimo=int(input("Popularidad minima: "))
        maximo=int(input("Popularidad maxima: "))

        if minimo<1 or maximo>100 or minimo>maximo:
            print("Rango de popularidad no valido")
            return

        encontrado=False

        for i in range(len(nombres)):

            if popularidades[i]>=minimo and popularidades[i]<=maximo:

                print("\nCancion encontrada:")
                print(f"Nombre: {nombres[i]}")
                print(f"Artista: {artistas[i]}")
                print(f"Popularidad: {popularidades[i]}")

                encontrado=True

        if encontrado==False:
            print("No hay canciones en ese rango")

    else:
        print("Opcion no valida")

def playlist_recomendada():

    if len(nombres)==0:
        print("\nNo hay canciones registradas")
        return

    promedio=sum(popularidades)/len(popularidades)

    print("\n========== PLAYLIST RECOMENDADA ==========")

    print(f"Promedio de popularidad: {promedio:.2f}")

    encontrado=False

    for i in range(len(nombres)):

        if popularidades[i] > promedio:

            print("\nCancion recomendada:")
            print(f"Nombre: {nombres[i]}")
            print(f"Artista: {artistas[i]}")
            print(f"Duracion: {duraciones[i]} minutos")
            print(f"Popularidad: {popularidades[i]}")

            encontrado=True

    if encontrado==False:
        print("No hay canciones que superen el promedio")


while True:

    print("================================")
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")

    opcion=input("\nSelecciona una opcion: ")

    if opcion=="1":

        agregar_canciones()

    elif opcion=="2":

        ver_reportes()

    elif opcion=="3":

        buscar_canciones()

    elif opcion=="4":

        playlist_recomendada()

    elif opcion=="5":

        print("¡Hasta pronto!")
        break

    else:

        print("\nOpcion no valida. Intenta nuevamente.")