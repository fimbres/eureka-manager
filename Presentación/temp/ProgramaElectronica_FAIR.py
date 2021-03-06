import time
print("Programa para diseño de amplificadores")
op = 1
def Limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def Caso1(vcc, icq, icm, beta):
    ibq = icq/beta
    ie = ibq + icq
    rb = (vcc - 0.7)/ibq
    vb = rb * ibq
    rc = (vcc - 0) / icq
    vc = icq * rc
    print("Corrientes:")
    print("  Ib:",ibq,"A")
    print("  Ic:",icq,"A")
    print("  Ie:",ie,"A")
    print("\nVoltajes:")
    print("  Vb:",vb,"V")
    print("  Vc:",vc,"V")
    print("\nResistencias:")
    print("  Rb:",rb,"Ohms")
    print("  Rc:",rc,"Ohms")
def Caso2(vcc, icq, icm, beta, ve):
    ibq = icq/beta
    ie = icq * (1 + 1/beta)
    rb = (vcc - 0.7 + ve) / ibq
    vb = rb * ibq
    vc = vcc / 2
    vce = vc - ve
    re = ve/ie
    rc = (vcc - vce - ve) / icq
    print("Corrientes:")
    print("  Ib:",ibq,"A")
    print("  Ic:",icq,"A")
    print("  Ie:",ie,"A")
    print("\nVoltajes:")
    print("  Vb:",vb,"V")
    print("  Vc:",vc,"V")
    print("  Ve:",ve,"V")
    print("\nResistencias:")
    print("  Rb:",rb,"Ohms")
    print("  Rc:",rc,"Ohms")
    print("  Re:",re,"Ohms")
def Caso3(vcc, icq, beta):
    ibq = icq/beta
    ie = icq * (1 + 1/beta)
    rb = beta * (0.025 / icq)
    re = (10 * rb) / beta
    rc = (vcc - (icq * re)) / 2 * icq
    vth = (ibq * rb) + 0.7 + (ie + re)
    r1 = (rb * vcc)/vth
    r2 = r1 / ((vcc/vth)-1)
    print("Corrientes:")
    print("  Ib:",ibq,"A")
    print("  Ic:",icq,"A")
    print("  Ie:",ie,"A")
    print("\nVoltajes:")
    print("  Vth:",vth,"V")
    print("\nResistencias:")
    print("  Rth o Rb:",rb,"Ohms")
    print("    R1:",r1,"Ohms")
    print("    R2:",r2,"Ohms")
    print("  Rc:",rc,"Ohms")
    print("  Re:",re,"Ohms")
while op != 0:
    print("1- Caso 1")
    print("2- Caso 2")
    print("3- Caso 3")
    print("0- Salir")
    op = int(input("Ingresa una opción: "))
    if op == 1:
        Limpiar()
        vcc = float(input("Ingresa el Voltaje Vcc: "))
        icq = float(input("Ingresa la corriente Icq: "))
        icm = float(input("Ingresa la corriente máxima Ic: "))
        beta = float(input("Ingresa a Beta: "))
        Caso1(vcc, icq, icm, beta)
        time.sleep(7)
        Limpiar()
    elif op == 2:
        Limpiar()
        vcc = float(input("Ingresa el Voltaje Vcc: "))
        icq = float(input("Ingresa la corriente Icq: "))
        icm = float(input("Ingresa la corriente máxima Ic: "))
        beta = float(input("Ingresa a Beta: "))
        ve = vcc/10
        Caso2(vcc, icq, icm, beta, ve)
        time.sleep(7)
        Limpiar()
    elif op == 3:
        Limpiar()
        vcc = float(input("Ingresa el Voltaje Vcc: "))
        icq = float(input("Ingresa la corriente Icq: "))
        beta = float(input("Ingresa a Beta: "))
        Caso3(vcc, icq, beta)
        time.sleep(7)
        Limpiar()
    elif op == 0:
        print("¡Hasta luego!")
        time.sleep(5)
        Limpiar()
    else:
        print("Ingresa un comando correcto")
        time.sleep(5)
        Limpiar()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 