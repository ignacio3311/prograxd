sw = 0
rut = []
edad = []
genero= []
tipo = []
correo = []
gens1 = ['M','m']
gens2 = ['F','f']
listasubs= ['PREMIUM','GOLD','SILVER','premium','gold','silver','Premium','Gold','Silver']
while sw == 0:
    print("BIENVENIDO A JUAN MAESTRO APP")
    print("INSERTE EL NUMERO DE LO QUE QUIERA ENTRAR:")
    print("1.Registrar Cliente")
    print("2.Suscripción")
    print("3.Consultar datos cliente")
    print("4.Salir")
    sw1 = 0
    sw2 = 0
    sw3 = 0
    sw4 = 0
    sw5 = 0
    numero= int(input(" "))
    if numero == 1:
        print("Eligio registrar cliente: ")
        while sw1 == 0:
            try:
                lrut=int(input("Inserte RUT sin puntos ni guion "))
                if lrut < 4000000 or lrut > 999999999:
                    print("Rut invalido, desea intentar nuevamente? 1 = SI / 2 = NO")
                    sn = int(input())
                    if sn == 1:
                        sw1 = 0
                    elif sn == 2:
                        sw1 = 1
                        sw2 = 1
                        sw3 = 1
                        sw4 = 1
                        sw5 = 1
                elif lrut >= 4000000 or lrut <= 999999999:
                    print("RUT VERIFICADO")
                    rut.append(lrut)
                    sw1 = 1
            except ValueError:
                print("Rut invalido, desea intentar nuevamente? 1 = SI / 2 = NO")
                sn = int(input())
                if sn == 1:
                    sw1 = 0
                elif sn == 2:
                    sw1 = 1
                    sw2 = 1
                    sw3 = 1
                    sw4 = 1
                    sw5 = 1
        while sw2 == 0:        
            try:    
                ledad = int(input("Inserte su edad"))
                if ledad < 0 or ledad > 110:
                    print("Edad invalida, desea intentar nuevamente? 1 = SI / 2 = NO")
                    sm = int(input())
                    if sm == 1:
                        sw2 = 0
                    elif sm == 2:
                        sw2 = 1
                elif ledad >= 0 or ledad <= 110:
                    print("EDAD VERIFICADA")
                    edad.append(ledad)
                    sw2 = 1                 
            except ValueError:
                print("Edad invalida, desea intentar nuevamente? 1 = SI / 2 = NO")
                sm = int(input())
                if sm == 1:
                    sw2 = 0
                elif sm == 2:
                    sw2 = 1
        while sw3 == 0:
            lgenero = input("Inserte su genero (M/F)")
            if lgenero in gens1 :
                print("Eligio genero masculino")
                sw3 = 1
                genero.append(lgenero)
            elif lgenero in gens2:
                print("Eligio genero femenino")
                sw3 = 1
                genero.append(lgenero)
            else:
                print("Error en su genero intente nuevamente")
        while sw4 == 0:
            ltipo = str(input("Inserte su subscripcion(PREMIUM/GOLD/SILVER)"))
            if ltipo not in listasubs:
                print("Error intente nuevamente")
            else:
                print("SUBSCRIPCION INSERTADA")
                tipo.append(ltipo)
                print(rut)
                print(edad)
                print(genero)
                print(tipo)
                
                sw4 = 1


            





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if numero == 4:
        print("Gracias por suscribirse a la app Juan Maestro")
        sw = 1
