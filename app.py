lst = []
lst1 = []
lst2 = []

"""
with open('tstest.txt', 'r') as archivo:
    for linea in archivo: 
        lst.append(linea.split(' '))

a = 0
for l in lst:
    #if l[9] == '2023':
    if l[a][10].endswith('wav'):
        lst2.append(l[10])
    a = a + 1

print(lst2)


"""
#CREAR EL ARCHIVO SALIDA TXT DESDE UN LS CON GREP

import subprocess

# Ejecutar el comando 'ls -l | grep "2023" > salida.txt'
comando = 'ls -l | grep "2023"'
with open('salida.txt', 'w') as salida_archivo:
    proceso = subprocess.run(comando, shell=True, stdout=salida_archivo, text=True)

# Verificar si el proceso terminó correctamente
if proceso.returncode == 0:
    print("Comando ejecutado correctamente.")
else:
    print("Hubo un error al ejecutar el comando.")


#ABRIR SALITA.TXT Y GENERAR UNA NUEVA LISTA CON LOS NOMBRES DE LOS ARCHIVOS A ELIMINAR
# Lista para almacenar las palabras que cumplen con los requisitos
nueva_lista = []

# Leer el contenido del archivo de texto
with open("tstest.txt", "r") as file:
    # Iterar sobre cada línea en el archivo
    for linea in file:
        # Dividir la línea en palabras usando el espacio como separador
        palabras = linea.split()
        # Iterar sobre cada palabra en la línea
        for palabra in palabras:
            # Verificar si la palabra comienza con "REC" y termina con ".wav"
            if palabra.startswith("REC") and palabra.endswith(".wav"):
                # Si cumple ambas condiciones, agregar la palabra a la nueva lista
                nueva_lista.append(palabra)

# Mostrar la nueva lista con las palabras que cumplen los requisitos
print(len(nueva_lista))