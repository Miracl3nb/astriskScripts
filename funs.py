import subprocess

#CREAR EL ARCHIVO SALIDA TXT DESDE UN LS CON GREP

def command(anio):
    comando = 'ls -l | grep' + ' ' + anio
    with open('salida.txt', 'w') as salida_archivo:
        proceso = subprocess.run(comando, shell=True, stdout=salida_archivo, text=True)
    if proceso.returncode == 0:
        print("Comando ejecutado correctamente.")
    else:
        print("Hubo un error al ejecutar el comando.")



#ABRIR SALITA.TXT Y GENERAR UNA NUEVA LISTA CON LOS NOMBRES DE LOS ARCHIVOS A ELIMINAR
def listdel():    
    delpen = []
    with open("salida.txt", "r") as file:
        for linea in file:
            palabras = linea.split()
            for palabra in palabras:
                if  palabra.endswith(".wav"):
                    delpen.append(palabra)
    return delpen                


def delconf(delpen):
    cant = len(delpen)
    print("registros a eliminar, ") + cant
    check =input("desea eliminar si/no")
    if check == "si" or "SI":
        delitems(delepn)
    else:
        print("Error de tipeo")
        print("PROCESO ANULADO")
    return cant
        

def delitems(delpen, cant):
    comando = 'rm' + ' ' + i
    for i delpen:
        subprocess.run(comando, shell=True)
    print("Se eliminaron "+ cant + "registros")
        


