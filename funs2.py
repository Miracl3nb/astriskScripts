import subprocess

#CREAR EL ARCHIVO SALIDA TXT DESDE UN LS CON GREP

def command(anio):
    comando = 'ls -l | grep' + ' ' + anio
    with open('salida.txt', 'w') as salida_archivo:
        proceso = subprocess.Popen(comando, shell=True, stdout=salida_archivo)
        proceso.communicate()
    if proceso.returncode == 0:
        print "Comando ejecutado correctamente."
    else:
        print "Hubo un error al ejecutar el comando."

#ABRIR SALITA.TXT Y GENERAR UNA NUEVA LISTA CON LOS NOMBRES DE LOS ARCHIVOS A ELIMINAR
def listdel():    
    delpen = []
    with open("salida.txt", "r") as file:
        for linea in file:
            palabras = linea.split()
            for palabra in palabras:
                if palabra.endswith(".wav"):
                    delpen.append(palabra)
    return delpen                

def delconf(delpen):
    cant = len(delpen)
    print "registros a eliminar: ", cant
    check = raw_input("¿Desea eliminar? si/no: ")
    if check.lower() == "si":
        delitems(delpen, cant)
    else:
        print "Error de tipeo"
        print "PROCESO ANULADO"
    return cant

def delitems(delpen, cant):
    for i in delpen:
        comando = 'rm' + ' ' + i
        subprocess.call(comando, shell=True)
    print "Se eliminaron", cant, "registros"

anio = "2024" # Aquí debes poner el año deseado
command(anio)
files_to_delete = listdel()
if files_to_delete:
    delconf(files_to_delete)
else:
    print "No hay archivos para eliminar."