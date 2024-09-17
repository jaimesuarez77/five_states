trP_total = 0  
Io = 0
porcI = 0
cantC1 = 0
cantC2 = 0
cantC3 = 0
cantIo1 = 0
cantIo2 = 0
cantIo3 = 0
tmP1 = 0
tmP2 = 0
tmP3 = 0
tmOut1 = 0
tmOut2 = 0
tmOut3 = 0
listo = []
cpu = []
lock = []

class Proceso:
    timeCpu = 0
    timeOut = 0
    estado = ""
    cantCpu = 0
    cantOut = 0
    cond = 0  # la condición =  0 nos dice que está activo el procedimiento

    def __init__(self,timeCpu,timeOut, estado, cantCpu, cantOut, cond):
        
        self.timeCpu = timeCpu
        self.timeOut = timeOut
        self.estado = estado
        self.cantCpu = cantCpu
        self.cantOut = cantOut
        self.cond = cond
        
    def setTimeCpu(self,timeCpu):
        self.timeCpu = timeCpu
        
    def setTimeOut(self,timeOut):
        self.timeOut = timeOut
        
    def setEstado(self, estado):
        self.estado = estado

    def setCantCpu(self, cantCpu):
        self.cantCpu = cantCpu

    def setCantOut(self, cantOut):
        self.cantOut = cantOut

    def setCond(self, cond):
        self.cond = cond


    def getTimeCpu(self):
        return self.timeCpu
    
    def getTimeOut(self):
        return self.timeOut
    
    def getEstado(self):
        return self.estado

    def getCantCpu(self):
        return self.cantCpu

    def getCantOut(self):
        return self.cantOut

    def getCond(self):
        return self.cond

    def serie(self):
        global trP_total, Io, porcI
        if self.cond == 1:
            trP = (int(self.cantCpu) * int(self.timeCpu)) + (int(self.cantOut) * int(self.timeOut))
            Io += int(self.timeOut) * int(self.cantOut)
            trP_total += trP
            porcI = round(Io * 100 / trP_total, 2)
        else:
            print("")
            
            
def Cinco():
    if listo:
        
        print("\nContenido de la lista `listo`:")
        for i, proceso in enumerate(listo):
            print(f"Posición {i + 1}:")
            print(f"  Proceso: {proceso.getEstado()}")
            print(f"  Tiempo de CPU restante: {proceso.getTimeCpu()}")
        print("__________________________________________________")              
        
        cpu.append(listo[0])
        
        
        for j in cpu:
            nuevo_time_cpu = j.getTimeCpu() - timeQ
            if nuevo_time_cpu <= 0:
                for i in cpu:
                    new_tm = i.getTimeCpu()-i.getTime()
                    i.setTimeCpu(new_tm)
                    lock.append(cpu[0])
            else:
                nuevo_time_cpu = j.getTimeCpu() - timeQ
                j.setTimeCpu(nuevo_time_cpu)    
            
            
              
        
        listo.pop(0)  
        
        
        print("\nContenido de la lista `listo`:")
        for i, proceso in enumerate(listo):
            print(f"Posición {i + 1}:")
            print(f"  Proceso: {proceso.getEstado()}")
            print(f"  Tiempo de CPU restante: {proceso.getTimeCpu()}")
            print()
        print("__________________________________________________")
        
        print("\nContenido de la lista `cpu`:")
        for i, proceso in enumerate(cpu):
            print(f"Posición {i + 1}:")
            print(f"  Proceso: {proceso.getEstado()}")
            print(f"  Tiempo de CPU restante: {proceso.getTimeCpu()}")
            print()
        print("__________________________________________________")
        
        print("\nContenido de la lista `lock`:")
        for i, proceso in enumerate(lock):
            print(f"Posición {i + 1}:")
            print(f"  Proceso: {proceso.getEstado()}")
            print(f"  Tiempo de CPU restante: {proceso.getTimeCpu()}")
        print("__________________________________________________")            
    else:
        print("La lista 'listo' está vacía.")
        
    Procedimiento()
        
        
def Procedimiento():
    if cpu:
        listo.append(cpu[0])
        cpu.pop(0)
        
    print("\nContenido de la lista `listo`:")
    for i, proceso in enumerate(listo):
        print(f"Posición {i + 1}:")
        print(f"  Proceso: {proceso.getEstado()}")
        print(f"  Tiempo de CPU restante: {proceso.getTimeCpu()}")
        print()
    print("__________________________________________________")
        
    print("\nContenido de la lista `cpu`:")
    for i, proceso in enumerate(cpu):
        print(f"Posición {i + 1}:")
        print(f"  Proceso: {proceso.getEstado()}")
        print(f"  Tiempo de CPU restante: {proceso.getTimeCpu()}")
        print()
    print("__________________________________________________")        
    print("\nContenido de la lista `lock`:")
    for i, proceso in enumerate(lock):
        print(f"Posición {i + 1}:")
        print(f"  Proceso: {proceso.getEstado()}")
        print(f"  Tiempo de CPU restante: {proceso.getTimeCpu()}")
    print("__________________________________________________")        
        
        

pUno = Proceso(0,0,'Uno', 0, 0, 1)
pDos = Proceso(0,0,'Dos', 0, 0, 0)
pTres = Proceso(0,0,'Tres', 0, 0, 0)

elegir = int(input("Ingrese el tipo de método a trabajar: 1 serie ; 2 cinco estados: "))
if elegir == 1:
    
    cantidadProceso = int(input("Ingrese la cantidad de procesos: "))
    if cantidadProceso == 2:
        pDos.setCond(1)
        cantC1 = int(input("Ingrese la cantidad de ejecuciones para el proceso 1: "))
        pUno.setCantCpu(cantC1)
        tmP1 = int(input("Ingrese el tiempo de ejecución del proceso 1: "))
        pUno.setTimeCpu(tmP1)
        cantIo1 = int(input("Ingrese la cantidad de I/O para el proceso 1: "))
        pUno.setCantOut(cantIo1)
        tmOut1 = int(input("Ingrese el tiempo de inactividad: "))
        pUno.setTimeOut(tmOut1)
        
        cantC2 = int(input("Ingrese la cantidad de ejecuciones para el proceso 2: "))
        pDos.setCantCpu(cantC2)
        tmP2 = int(input("Ingrese el tiempo de ejecución del proceso 2: "))
        pDos.setTimeCpu(tmP2)
        cantIo2 = int(input("Ingrese la cantidad de I/O para el proceso 2: "))
        pDos.setCantOut(cantIo2)
        tmOut2 = int(input("Ingrese el tiempo de inactividad: "))
        pDos.setTimeOut(tmOut2)
        
    else:
        pDos.setCond(1)
        pTres.setCond(1)
        cantC1 = int(input("Ingrese la cantidad de procesos para el proceso 1: "))
        pUno.setCantCpu(cantC1)
        tmP1 = int(input("Ingrese el tiempo de ejecución del proceso 1: "))
        pUno.setTimeCpu(tmP1)
        cantIo1 = int(input("Ingrese la cantidad de I/O para el proceso 1: "))
        pUno.setCantOut(cantIo1)
        tmOut1 = int(input("Ingrese el tiempo de inactividad: "))
        pUno.setTimeOut(tmOut1)
        
        cantC2 = int(input("Ingrese la cantidad de procesos para el proceso 2: "))
        pDos.setCantCpu(cantC2)
        tmP2 = int(input("Ingrese el tiempo de ejecución del proceso 2: "))
        pDos.setTimeCpu(tmP2)
        cantIo2 = int(input("Ingrese la cantidad de I/O para el proceso 2: "))
        pDos.setCantOut(cantIo2)
        tmOut2 = int(input("Ingrese el tiempo de inactividad: "))
        pDos.setTimeOut(tmOut2)
        
        cantC3 = int(input("Ingrese la cantidad de procesos para el proceso 3: "))
        pTres.setCantCpu(cantC3)
        tmP3 = int(input("Ingrese el tiempo de ejecución del proceso 3: "))
        pTres.setTimeCpu(tmP3)
        cantIo3 = int(input("Ingrese la cantidad de I/O para el proceso 3: "))
        pTres.setCantOut(cantIo3)
        tmOut3 = int(input("Ingrese el tiempo de inactividad: "))
        pTres.setTimeOut(tmOut3)   

    pUno.serie()
    pDos.serie()
    pTres.serie()

    print(f"Suma total del tiempo de respuesta: {trP_total} y el tiempo fuera {Io}")
    print(f"El porcentaje de inutilización es: {porcI} %")

elif elegir == 2:
    
    cantidadProceso = int(input("Ingrese la cantidad de procesos: "))
    timeQ = int(input("Ingrese el tiempo en CPU: "))
    if cantidadProceso == 2:
        pDos.setCond(1)
        cantC1 = int(input("Ingrese la candidad de ejecuciones para el proceso 1: "))
        pUno.setCantCpu(cantC1)
        tmP1 = int(input("Ingrese el tiempo de ejecición del proceso 1: "))
        pUno.setTimeCpu(tmP1)
        cantIo1 = int(input("Ingrese la candidad de I/O para el proceso 1: "))
        pUno.setCantOut(cantIo1)
        tmOut1 = int(input("Ingrese el tiempo de inactividad: "))
        pUno.setTimeOut(tmOut1)
        
        cantC2 = int(input("Ingrese la candidad de ejecuciones para el proceso 2: "))
        pDos.setCantCpu(cantC2)
        tmP2 = int(input("Ingrese el tiempo de ejecición del proceso 2: "))
        pDos.setTimeCpu(tmP2)
        cantIo2 = int(input("Ingrese la candidad de I/O para el proceso 2: "))
        pDos.setCantOut(cantIo2)
        tmOut2 = int(input("Ingrese el tiempo de inactividad: "))
        pDos.setTimeOut(tmOut2)

        listo.append(pUno)
        listo.append(pDos)
        
        
    else:
        pDos.setCond(1)
        pTres.setCond(1)
        cantC1 = int(input("Ingrese la candidad de procesos para el proceso 1: "))
        pUno.setCantCpu(cantC1)
        tmP1 = int(input("Ingrese el tiempo de ejecición del proceso 1: "))
        pUno.setTimeCpu(tmP1)
        cantIo1 = int(input("Ingrese la candidad de I/O para el proceso 1: "))
        pUno.setCantOut(cantIo1)
        tmOut1 = int(input("Ingrese el tiempo de inactividad: "))
        pUno.setTimeOut(tmOut1)
        
        cantC2 = int(input("Ingrese la candidad de procesos para el proceso 2: "))
        pDos.setCantCpu(cantC2)
        tmP2 = int(input("Ingrese el tiempo de ejecición del proceso 2: "))
        pDos.setTimeCpu(tmP2)
        cantIo2 = int(input("Ingrese la candidad de I/O para el proceso 2: "))
        pDos.setCantOut(cantIo2)
        tmOut2 = int(input("Ingrese el tiempo de inactividad: "))
        pDos.setTimeOut(tmOut2)
        
        cantC3 = int(input("Ingrese la candidad de procesos para el proceso 3: "))
        pTres.setCantCpu(cantC3)
        tmP3 = int(input("Ingrese el tiempo de ejecición del proceso 3: "))
        pTres.setTimeCpu(tmP3)
        cantIo3 = int(input("Ingrese la candidad de I/O para el proceso 3: "))
        pTres.setCantOut(cantIo3)
        tmOut3 = int(input("Ingrese el tiempo de inactividad: "))
        pTres.setTimeOut(tmOut3)
        
        listo.append(pUno)
        listo.append(pDos)
        listo.append(pTres)
        
        
    
    Cinco()
# Imprimir el contenido del array `listo`
 #   print("\nContenido de la lista `listo`:")

  #  for i, proceso in enumerate(listo):
   #     print(f"Proceso {i + 1}:")
    #    print(f"  Estado: {proceso.getEstado()}")
    #    print(f"  Cantidad de CPU: {proceso.getCantCpu()}")
    #    print(f"  Cantidad de I/O: {proceso.getCantOut()}")
    #    print(f"  Condición: {proceso.getCond()}")
    #    print()
