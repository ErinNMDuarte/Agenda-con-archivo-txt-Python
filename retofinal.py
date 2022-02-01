from os import remove


opcion = 0

def lectura():
    with open ('agenda.txt', 'r+') as f:
        datos = f.readlines()
    return datos

def lista():
    datos=lectura()
    print ("Listado de beneficiarios")
    for i in datos:
        dato = datos.index(i)
        print (datos[dato].strip())

def filtro():
    list=[]
    datos=lectura()
    letra = input("Digite la letra por la que empiezan los beneficiarios:")
    print ("Listado filtrado de beneficiarios:")
    for i in datos:
        if letra == i[0]:
            inom = datos.index(i)
            print (datos[inom].strip())
            print (datos[inom+1].strip())
            print (datos[inom+2].strip())

def escritura():
    cont = 0
    with open ('agenda.txt', 'a') as f:
        print ("Digite la información del beneficiario a agregar:")
        nom = input('Nombre: ')
        doc = input('Documento: ')
        tel = input('Celular: ')
        datos = lectura()
        for i in datos:
            if doc == i.strip():
                cont += 1
        if cont > 0:
            print ("El documento ya existe")
        else:
            f.write (f'{nom}\n{doc}\n{tel}\n')
            print("El beneficiario ha sido agregado")

def buscar():
    datos = lectura()
    nom = input ("Digite el nombre y apellido del beneficiario a buscar:")
    check = 0
    for i in datos:
        if nom == i.strip():
            inom = datos.index(nom+'\n')
            print (datos[inom].strip())
            print (datos[inom+1].strip())
            print (datos[inom+2].strip())
            check = 1
            break
    if check == 0:
        print("No se encuentra el beneficiario en la agenda")

def borrar():
    datos = lectura()
    doc=input("Digite la cedula del beneficiario a borrar:")
    for i in datos:
        if doc == i.strip():
            idoc = datos.index(doc+'\n')
            del datos[idoc-1:idoc+2]
    print ("El usuario ha sido eliminado del listado")
    return (datos)

def actualizar(datos):
    with open('agenda.txt', 'w') as f:
        for i in datos:
            f.write(i)

while (opcion != 6):
    print ("Menu Principal")
    print ("1. Ver listado")
    print ("2. Ver Listado filtrado")
    print ("3. Agregar beneficiario")
    print ("4. Buscar beneficiario")
    print ("5. Borrar beneficiario")
    print ("6. Salir")
    opcion = int(input())
    if opcion == 1:
        lista()
    elif opcion==2:
        filtro()
    elif opcion==3:
        escritura()
    elif opcion==4:
        buscar()
    elif opcion==5:
        dat= borrar()
        actualizar(dat)
    else:
        print("Hasta pronto")
