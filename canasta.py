pin_correcto = "1234"
intentos_pin = 0
max_intentos = 3
#esp = 1 #agrega espacios despues de los mensajes
valpn = "1234567890" #para validar que pin sean numeros
valon = "1234567890" #para validar que opciones sean numeros
saldo = 5000
sesion_activa = False
menu_activo = False
retiro_maximo = 1000
deposito_maximo = 5000
historial = []
sesion = False

def espacios():
    for r in range(2):  #numero de lineas vacias despues de los mensajes
        print()

def ingresar_opcion(): #valon
    o = 0
    while o >= 0:
        c = 0
        espacios()
        print("Ingrese una opción (1 - 6):")
        opc = str(input())
        for i in range(len(opc)):
            for n in range(10):
                if opc[i] == valon[n]:
                    c += 1
        if c != len(opc):
            print("¡ERROR! Ingrese solo numeros")
        else:
            opc =int(opc)
            return fuera_de_rango(opc)

def fuera_de_rango(opc):   #opc, valon
    while opc >= 7 or opc < 1:  #puedo poner un if
        print("¡ERROR! Fuera de rango")
        opc = ingresar_opcion() #valon
    return opc     #si elimino la funcion puedo poner un else y un break?
    
def validar_pin_numero(num): # valpn
    c = 0
    for i in range(4):
        for n in range(10):
            if num[i] == valpn[n]:
                c += 1
    return c

def bucle(): #valpn
    n = 0
    print("¡Máximo número de intentos permitido!")
    while n >= 0:
        c = 0
        if n == 0:
            print("¡Usuario bloqueado!")
            n = 1
        if n == 1:
            espacios()
            print("Ingrese su número de PIN:")
            pin = str(input())
            if len(pin) != 4:
                print("¡ERROR! El PIN debe tener solo 4 dígitos")
            else:
                c = validar_pin_numero(pin) #, valpn
                if c != 4:
                    print("¡ERROR! El PIN solo debe tener números")
                    n = 1
                else:
                    n = 0

def validar_pin(pin_correcto, intentos_pin): #pin_correcto, , max_intentos, valpn
    pin = ""
    while pin != pin_correcto:
        c = 0
        espacios()
        print("Ingrese su número de PIN:")
        pin = str(input())
        if len(pin) != 4:
            print("¡ERROR! El PIN debe tener 4 dígitos")
        elif pin != pin_correcto:
            c = validar_pin_numero(pin) #, valpn
            if c != 4:
                print("¡ERROR! El PIN solo debe tener números")           
        if pin != pin_correcto and c == 4:                
            intentos_pin += 1
            v = max_intentos - intentos_pin
            if v == 1:
                s = ""
                n = ""
            else:
                s = "s"
                n = "n"
            if v == 0: 
                bucle()  #valpn
            print(f"¡PIN INCORRECTO! Le queda{n} {v} intento{s}.")
        if pin == pin_correcto:
            print("¡Bienvenido, Carlos!")
            return True, pin_correcto
        
def consultar(historial, saldo): #saldo, historial
    espacios()
    print("+++++++++++++ Menú de Consulta de Saldos +++++++++++++")
    espacios()
    print(f"Su saldo actual es: ${saldo}")
    historial.append("Consulta de saldo")
    espacios()
    print("Enter para ir al Menú Principal")                               #debe se función
    ent = input()
    while ent != "":
        print("¡No se admiten caracteres, presione ENTER por favor!")
        ent = input()
    else:
        return historial, saldo                                                   # hasta aqui

def depositar(historial, saldo):
    espacios()
    print("+++++++++++++ Menú de Depósito de Dinero +++++++++++++")  #deposito_maximo, historial, saldo
    deposito = 0
    while deposito == 0:
        c = 0
        espacios()
        print("Ingrese el monto a depositar:")
        print("$", end = "")
        monto_d = str(input())            #hay que validar que sea numero
        for i in range(len(monto_d)):
            for n in range(10):
                if monto_d[i] == valon[n]:
                    c += 1
        if len(monto_d) != c:
            print("¡ERROR! Ingrese valores en números") 
            continue      
        monto_d = int(monto_d)               #y luego cast
        if monto_d > deposito_maximo:
            print("¡Los valores ingresados superan el máximo permitido ($5000)!")
            continue
        elif monto_d < 1:
            print("¡ERROR! No se aceptan valores negativos")
            continue
        else:
            saldo = saldo + monto_d
            espacios()
            print("¡Depósito completado!")
            historial.append(f"Depósito ---- Monto: +${monto_d} ---- Saldo: ${saldo}")
            espacios()        
            print("Enter para ir al Menú Principal")                               #debe se función
            ent = input()
            while ent != "":
                print("¡No se admiten caracteres, presione ENTER por favor!")
                ent = input()
            else:
                return historial, saldo                                           # hasta aqui

def retirar(historial, saldo):
    espacios()
    print("++++++++++++++ Menú de Retiro de Dinero ++++++++++++++")
    retiro = 0
    while retiro == 0:
        c = 0
        espacios()
        print("Ingrese el monto a retirar:")
        monto_d = str(input("$"))            #hay que validar que sea numero
        for i in range(len(monto_d)):
            for n in range(10):
                if monto_d[i] == valon[n]:
                    c += 1
        if len(monto_d) != c:
            print("¡ERROR! Ingrese valores en números") 
            continue        
        monto_d = int(monto_d)               #y luego cast
        if monto_d > retiro_maximo:
            print("¡Los valores ingresados superan el máximo permitido ($1000)!")
            continue
        elif monto_d < 1:
            print("¡ERROR! No se aceptan valores negativos")
            continue
        elif monto_d > saldo:
            print("¡Fondos insuficientes para completar el retiro!")
            continue
        else:
            saldo = saldo - monto_d
            espacios()
            print("¡Retiro de dinero completado!")
            historial.append(f"Retiro   ---- Monto: -${monto_d} ---- Saldo: ${saldo}")
            espacios()        
            print("Enter para ir al Menú Principal")                               #
            ent = input()
            while ent != "":
                print("¡No se admiten caracteres, presione ENTER por favor!")
                ent = input()
            else:                
                return historial, saldo                                           #     

def act_pin(pin_correcto):
    espacios()
    print("+++++++++++++ Menú para cambio de clave ++++++++++++++")
    espacios()
    print("Ingrese su PIN actual:")
    a_pin = str(input())
    while a_pin != pin_correcto:
        print("¡ERROR! Escriba correctamente el pin")
        espacios()
        print("Ingrese su PIN actual:")
        a_pin = str(input())
    while a_pin == pin_correcto:
        espacios()
        print("Ingrese su nuevo pin:")
        n_pin = str(input())
        if len(n_pin) != 4:
            print("¡ERROR! El PIN debe tener 4 dígitos")
            continue
        c = validar_pin_numero(n_pin) #, valpn
        if c != 4:
            print("¡ERROR! El PIN solo debe tener números")
            continue
        elif n_pin == pin_correcto:
            print("¡ERROR! El nuevo PIN no debe ser igual al anterior")
            continue
        else:
            print("PIN guardado correctamente")
            historial.append("Cambio de PIN")
            espacios()
            print("Enter para ir al Menú Principal")                               #debe se función
            ent = input()
            while ent != "":
                print("¡No se admiten caracteres, presione ENTER por favor!")
                ent = input()
            else:                
                return n_pin

def historia(historial):
    c = 0
    espacios()
    print("++++ Menú para ver el Historial de Transacciones +++++")
    espacios()
    historial = historial[::-1]
    for history in historial:
        c += 1
        print(f"{c}.", history)
    espacios()
    print("Enter para ir al Menú Principal")                               #debe se función
    ent = input()
    while ent != "":
        print("¡No se admiten caracteres, presione ENTER por favor!")
        ent = input()
    else:
        espacios()                
        return


def menu(pin_correcto, sesion_activa, historial, saldo): #sesion_activa, valon, historial, deposito_maximo, saldo
    while sesion_activa == True:
        espacios()
        print("++++++++++++++++++++++++++++++++++++++++++ Menú principal ++++++++++++++++++++++++++++++++++++++++++")
        espacios()
        print("1. Consultar saldo", end = "")
        for e in range(60):
            print(end = " ")
        print("4. Actualizar PIN de seguridad")
        print("2. Depositar dinero", end = "")
        for e in range(59):
            print(end = " ")
        print("5. Ver Historial")
        print("3. Retirar dinero", end = "")
        for e in range(61):
            print(end = " ")
        print("6. Salir del sistema")
        espacios()

        opc = ingresar_opcion() #valon
        # opc = fuera_de_rango() #opc, valon

        if opc == 1:
           historial, saldo = consultar(historial, saldo) #saldo, historial

        if opc == 2:
            historial, saldo = depositar(historial, saldo) #deposito_maximo, historial, saldo

        if opc == 3:
            historial, saldo = retirar(historial, saldo)

        if opc == 4:
            pin_correcto = act_pin(pin_correcto)

        if opc == 5:
            historia(historial)

        if opc == 6:
            print("¡Hasta luego, Carlos!")
            espacios()
            espacios()
            return False, pin_correcto
    else:
        return False

def s_activa(pin_correcto, intentos_pin, historial, saldo):
    sesion_activa, pin_correcto = validar_pin(pin_correcto, intentos_pin)                   #pin_correcto, intentos_pin, max_intentos, valpn
    sesion, pin_correcto = menu(pin_correcto, sesion_activa, historial, saldo)                                    #sesion_activa, valon, historial, deposito_maximo, saldo
    if sesion == False:
        return False, pin_correcto

while sesion == False:
    ing = input("Ingresar al sistema:")
    if ing == "":
        for a in range(1):
            espacios()
        sesion = True
        sesion, pin_correcto = s_activa(pin_correcto, intentos_pin, historial, saldo) # falta valon sesion_activa, pin_correcto, intentos_pin, max_intentos, valpn, historial, deposito_maximo, saldo