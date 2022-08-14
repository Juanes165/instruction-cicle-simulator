#tamaño de la memoria, se manejan las direcciones de 0 hasta X-1 donde X es el tamaño de la memoria
MEMORY_SIZE = 1000

#direccion del archivo de instrucciones
FILE_PATH = "instrucciones/ENTRADA1.txt"

control_unit = 0    #unidad de control (para decidir que instruccion ejecutar)
accumulator = 0     #acumulador
icr = 0             #ICR (carga las instrucciones de la memoria)
mar = 0             #MAR 
mdr = 0             #MDR (carga el valor de la memoria)


#creacion de la memoria
memory = []

for i in range(MEMORY_SIZE + 1):
    memory.append(None)


#cargando instrucciones
file = open(FILE_PATH, "r")

lines = file.readlines()

#el codigo del programa
code = []

for index, line in enumerate(lines):
    try:
        code.append(int(line.replace("\n", "")))
    except:
        code.append(line.replace("\n", ""))
