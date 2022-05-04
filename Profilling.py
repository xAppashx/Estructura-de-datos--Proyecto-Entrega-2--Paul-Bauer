import Main
import cProfile
import TreeFacturas
import CodigoTreeV4

def Tabla():
      print("Que profiling quiere hacer?")
      print("1) Main: Runner (todo el codigo)")
      print("2) CodigoTreeV4: Show (mostrar todo el inventario)")
      print("3) CodigoTreeV4: Insert (anadir un nuevo nodo)")
      print("4) CodigoTreeV4: Retrieve (obtener los datos de un nodo)")
      print("5) TreeFactura: Retrieve")
      print("6) TreeFactura: Insert")
      print("7) TreeFactura: Show")      
      Opcion = int(input())
      return Opcion
#Def Tabla

def Runner():
      #Ingreso unos valores a los arboles para que pueda funccionar el profiling.
            CodigoTreeV4.bplustree.insert('01F', 'Fresas', '5', '7', '15')
            CodigoTreeV4.bplustree.insert('02B', 'Bananos', '4', '7', '20')
            CodigoTreeV4.bplustree.insert('03M', 'Manzanas', '7', '7', '12')
            CodigoTreeV4.bplustree.insert('04J', 'Jocotes', '12', '7', '17')
   
            TreeFacturas.treefacturas.Insert('1', '0351', 'Pedro', 'Bananos', '6', '120')
            TreeFacturas.treefacturas.Insert('2', '8945', 'Jose', 'Manzanas', '2', '24')
      
      
            Opcion = Tabla()
      

            
            if (Opcion == 1):
                  print("")
                  #print("Profiling completo:")
                  cProfile.run('Main.Runner()')
                  #Opcion == Tabla
            #if Opcion == 1
            
            
            if (Opcion == 2):
                  print("")
                  print("Profiling del Show en CodigoTreeV4:")
                  cProfile.run('CodigoTreeV4.bplustree.show()')
                  Opcion == Tabla
            #if Opcion == 2
            
            
            if (Opcion == 3):
                  print("")
                  print("Profiling del Insert en CodigoTreeV4:")
                  cProfile.run('CodigoTreeV4.bplustree.insert("05M", "Mango", "7", "3", "5")')
                  Opcion == Tabla
            #if Opcion == 3
            
            
            if (Opcion == 4):
                  print("")
                  print("Profiling del Retrieve en CodigoTreeV4:")
                  cProfile.run('CodigoTreeV4.bplustree.retrieve("02B")')
                  Opcion == Tabla
            #if Opcion == 4
            
            
            if (Opcion == 5):
                  print("")
                  print("Profiling del Retrieve en TreeFacturas:")
                  cProfile.run('TreeFacturas.treefacturas.retrieve("1")')
                  Opcion == Tabla
            #if Opcion == 5
            
            
            if (Opcion == 6):
                  print("")
                  print("Profiling del Insert en TreeFacturas:")
                  cProfile.run('TreeFacturas.treefacturas.Insert("3", "66789", "Juan", "Jocotes", "1", "17")')
                  Opcion == Tabla
            #if Opcion == 6
            
            
            if (Opcion == 7):
                  print("")
                  print("Profiling del Show en TreeFacturas:")
                  cProfile.run('TreeFacturas.treefacturas.show()')
                  Opcion == Tabla
            #if Opcion == 7

            
            
            if (Opcion < 1 or Opcion > 7):
                  print("Ingreso no valido.")
            #if Opcion == 1

      
#def Runner

Runner()