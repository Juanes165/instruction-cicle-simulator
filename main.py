from parameters import *

# funcion set
def set_instruction(mem_dir, value):
    '''
    Almacena un valor en la direccion de memoria dada
    '''
    memory[mem_dir] = value


# funcion add
def add_instruction(value1, value2 = None):
    '''
    Suma dos valores, puede ser un valor dado con el acumulador o dos valores diferentes
    '''
    global accumulator
    if value2 == None:
        accumulator = accumulator + value1
    elif value2 != None:
        accumulator = value1 + value2


# funcion sub
def sub_instruction(value1, value2 = None):
    '''	
    Resta dos valores, puede ser un valor dado con el acumulador o dos valores diferentes
    '''
    global accumulator
    if value2 == None:
        accumulator = accumulator - value1
    elif value2 != None:
        accumulator = value1 - value2


# funcion mul
def mul_instruction(value1, value2 = None):
    '''
    Multiplica dos valores, puede ser un valor dado con el acumulador o dos valores diferentes
    '''
    global accumulator
    if value2 == None:
        accumulator = accumulator * value1
    elif value2 != None:
        accumulator = value1 * value2


# funcion div
def div_instruction(value1, value2 = None):
    '''
    Divide dos valores, puede ser un valor dado con el acumulador o dos valores diferentes
    Para la division se utilizan restas sucesivas
    '''
    global accumulator
    if value2 == None:
        dividend = accumulator
        divisor = value1
        quotient = 0
        while dividend >= divisor:
            dividend = dividend - divisor
            quotient = quotient + 1
        
    elif value2 != None:
        dividend = value1
        divisor = value2
        quotient = 0
        while dividend >= divisor:
            dividend = dividend - divisor
            quotient = quotient + 1

    accumulator = quotient


# funcion beq
def beq_instruction(value1, value2 = None):
    '''
    Compara dos valores, puede ser un valor dado con el acumulador o dos valores diferentes
    Si los valores son iguales, se carga el primer valor en el acumulador
    '''
    global accumulator
    if value2 == None:
        if value1 - accumulator == 0:
            accumulator = value1
    elif value2 != None:
        if value1 - value2 == 0:
            accumulator = value1


# function and
def and_instruction(value1, value2 = None):
    '''	
    Ejecuta la funcion AND nativa de python, 0 equivale a False y cualquier otro numero equivale a True
    '''
    global accumulator
    if value2 == None:
        accumulator = accumulator and value1
    elif value2 != None:
        accumulator = value1 and value2


# function or
def or_instruction(value1, value2 = None):
    '''
    Ejecuta la funcion OR nativa de python, 0 equivale a False y cualquier otro numero equivale a True
    '''
    global accumulator
    if value2 == None:
        accumulator = accumulator or value1
    elif value2 != None:
        accumulator = value1 or value2


#funcion ldr
def ldr_instruction(value):
    '''
    Carga el valor de la direccion de memoria dada en el acumulador
    '''
    global accumulator
    accumulator = value


# function str
def str_instruction(direction):
    '''
    Almacena el valor del acumulador en la direccion de memoria dada
    '''
    global accumulator
    memory[direction] = accumulator


# funcion shw
def shw_instruction(direction):
    '''
    Muestra el valor de la direccion de memoria dada en la pantalla
    '''
    print(memory[direction])
    print("")


# funcion delete
def delete(index):
    '''
    Elimina el valor de la direccion de memoria dada
    '''
    memory[index] = None


# funcion para retornar direccion de memoria
def get_memory_dir(direction):
    '''
    Retorna la direccion de memoria en valor numerico
    '''
    if direction == "NULL":
        return 0

    direction = direction.strip("D")
    direction = int(direction)
    return direction


#ejecucion del programa
for program_counter, line in enumerate(code):
    icr = line.split(" ")
    control_unit = icr[0]
    mar = get_memory_dir(icr[1])

    if(control_unit == "SET"):

        set_instruction(mar, int(icr[2]))

    elif(control_unit == "ADD"):

        mdr = memory[mar]

        if icr[2] == "NULL":
            add_instruction(mdr)
        else:
            add_instruction(mdr, get_memory_dir(icr[2]))
        if icr[3] != "NULL":
            set_instruction(get_memory_dir(icr[3]), accumulator)

    elif(control_unit == "SUB"):
    
        mdr = memory[mar]

        if icr[2] == "NULL":
            sub_instruction(mdr)
        else:
            sub_instruction(mdr, get_memory_dir(icr[2]))
        if icr[3] != "NULL":
            set_instruction(get_memory_dir(icr[3]), accumulator)

    elif(control_unit == "MUL"):
    
        mdr = memory[mar]

        if icr[2] == "NULL":
            mul_instruction(mdr)
        else:
            mul_instruction(mdr, get_memory_dir(icr[2]))
        if icr[3] != "NULL":
            set_instruction(get_memory_dir(icr[3]), accumulator)

    elif(control_unit == "DIV"):
    
        mdr = memory[mar]

        if icr[2] == "NULL":
            div_instruction(mdr)
        else:
            div_instruction(mdr, get_memory_dir(icr[2]))
        if icr[3] != "NULL":
            set_instruction(get_memory_dir(icr[3]), accumulator)

    elif(control_unit == "INC"):

        set_instruction(mar,  memory[mar] + 1)

    elif(control_unit == "DEC"):
            
        set_instruction(mar,  memory[mar] - 1)

    elif(control_unit == "MOV"):
        
        set_instruction(get_memory_dir(icr[2]), memory[mar])
        delete(mar)

    elif(control_unit == "LDR"):

        mdr = memory[mar]
        ldr_instruction(mdr)

    elif(control_unit == "STR"):
            
        str_instruction(mar)

    elif(control_unit == "BEQ"):

        mdr = memory[mar]

        if icr[2] == "NULL":
            beq_instruction(mdr)
        else:
            beq_instruction(mdr, get_memory_dir(icr[2]))
        if icr[3] != "NULL":
            set_instruction(get_memory_dir(icr[3]), accumulator)

    elif(control_unit == "AND"):
    
        mdr = memory[mar]

        if icr[2] == "NULL":
            and_instruction(mdr)
        else:
            and_instruction(mdr, get_memory_dir(icr[2]))
        if icr[3] != "NULL":
            set_instruction(get_memory_dir(icr[3]), accumulator)

    elif(control_unit == "OR"):

        mdr = memory[mar]

        if icr[2] == "NULL":
            or_instruction(mdr)
        else:
            or_instruction(mdr, get_memory_dir(icr[2]))
        if icr[3] != "NULL":
            set_instruction(get_memory_dir(icr[3]), accumulator)

    
    elif(control_unit == "SHW"):
            
        shw_instruction(mar)

    elif(control_unit == "END"):
        end = True
        break
