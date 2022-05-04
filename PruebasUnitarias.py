import Main
import TreeFacturas
import CodigoTreeV4

def Tabla():
      print("")
      print("Que prueba unitaria quiere hacer?")
      print("1) CodigoTreeV4: Show (mostrar todo el inventario)")
      print("2) CodigoTreeV4: Insert (anadir un nuevo nodo)")
      print("3) CodigoTreeV4: Retrieve (obtener los datos de un nodo)")
      print("4) TreeFactura: Retrieve")
      print("5) TreeFactura: Insert")
      print("6) TreeFactura: Show")   
      print("7) Salir.")
      Opcion = int(input())
      return Opcion
#Def Tabla


def Runner():

      CodigoTreeV4.bplustree.insert('01F', 'Fresas', '5', '7', '15')
      CodigoTreeV4.bplustree.insert('02B', 'Bananos', '4', '7', '20')
      CodigoTreeV4.bplustree.insert('03M', 'Manzanas', '7', '7', '12')
      CodigoTreeV4.bplustree.insert('04J', 'Jocotes', '12', '7', '17')
   
      TreeFacturas.treefacturas.Insert('1', '0351', 'Pedro', 'Bananos', '6', '120')
      TreeFacturas.treefacturas.Insert('2', '8945', 'Jose', 'Manzanas', '2', '24')
      
      Opcion = Tabla()
      
      while (Opcion != 7):
            
            
            if (Opcion == 1):
                  CodigoTreeV4.bplustree.show()
                  print("")
                  print("")
                  print("Sucess!")
                  Opcion = Tabla()
            #if Opcion == 1
            
            
            if (Opcion == 2):
                  CodigoTreeV4.bplustree.insert("05M", "Mango", "7", "3", "5")
                  Nombre, Cantidad, PrecioCompra, PrecioVenta = CodigoTreeV4.bplustree.retrieve("05M")
                  if Nombre is not None:
                        print("Success!")
                  else:
                        print("Fail.")
                  Opcion = Tabla()
            #if Opcion == 1
            
            
            if (Opcion == 3):
                  Nombre, Cantidad, PrecioCompra, PrecioVenta = CodigoTreeV4.bplustree.retrieve("02B")
                  if Nombre[0] == "Bananos":
                        print("Success!")
                  else:
                        print("Fail.")
                  Opcion = Tabla()
            #if Opcion == 1
            
            
            if (Opcion == 4):
                  NitDevuelto, NombreDevuelto, ArticuloDevuelto, CantidadDevuelta, PagoTotalDevuelto = TreeFacturas.treefacturas.retrieve("1")
                  if NombreDevuelto[0] == "Pedro":
                        print("Sucess!")
                  else:
                        print("Fail.")
                  Opcion = Tabla()
            #if Opcion == 1
            
            
            if (Opcion == 5):
                  TreeFacturas.treefacturas.Insert("3", "66789", "Juan", "Jocotes", "1", "17")
                  NitDevuelto, NombreDevuelto, ArticuloDevuelto, CantidadDevuelta, PagoTotalDevuelto = TreeFacturas.treefacturas.retrieve("3")
                  if NombreDevuelto[0] == "Juan":
                        print("Sucess!")
                  else:
                        print("Fail.")
                  Opcion = Tabla()
            #if Opcion == 1
            
            
            if (Opcion == 6):
                  TreeFacturas.treefacturas.show()
                  print("")
                  print("")
                  print("Sucess!")
                  Opcion = Tabla()
            #if Opcion == 1
            
            
            if (Opcion < 1 or Opcion > 7):
                  print("Entrada no valida.")
                  Opcion = Tabla()
            #if Opcion == 1
            
      #while Opcion != 7
      
      if (Opcion == 7):
            print("Ok, adios!")
      #if Opcion == 7
      
#Def Runner

Runner()

