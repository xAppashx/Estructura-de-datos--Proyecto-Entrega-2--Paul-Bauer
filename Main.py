""" 
      Proyecto Estructura de Datos
      Paul Bauer 
      20210060

      Entrega 2

"""

import CodigoTreeV4
import TreeFacturas


def Runner():
  
   CodigosFacturas = 3
   
   UtilidadEmpresa = 0
   
   Corriendo = Tabla()
   while (Corriendo != 6):
         
         
         # Creando / anadiendo un producto
         if (Corriendo == 1):
               print("Ingrese el codigo del articulo: ")
               
               Codigo = input()
               Nombre, Cantidad, PrecioCompra, PrecioVenta = CodigoTreeV4.bplustree.retrieve(Codigo)
               
               
               if Nombre is not None:
                  print("Usted se refiere al producto:", Nombre[0])
                  print("Ingrese la cantidad ingresante en el inventario:")
                  CantidadIngresante = int(input())
                  IntCantidad = int(Cantidad[0])
                  
                  TotalCantidad = CantidadIngresante + IntCantidad
                  StringCantidad = str(TotalCantidad)
                  
                  CodigoTreeV4.bplustree.CantidadModif(Codigo, StringCantidad)
                  print("Se anado la cantidad exitosamente !")
                  
                  IntPrecioCompra = int(PrecioCompra)
                  UtilidadEmpresa =  UtilidadEmpresa - (IntCantidad * IntPrecioCompra)
                  
               #If nombre is not none
               
               
               if Nombre is None:
                  print("Esta creando un nuevo producto!")
                  
                  print("Cual es el nombre del producto?")
                  Nombre = input()
                  
                  print("Cual es su cantidad ?")
                  Cantidad = input()
                  
                  print("Cual es el precio de compra ?")
                  PrecioCompra = input()
                  
                  print("Cual es el precio de venta ?")
                  PrecioVenta = input()
                  
                  CodigoTreeV4.bplustree.insert(Codigo, Nombre, Cantidad, PrecioCompra, PrecioVenta)
                  
                  IntPrecioCompra = int(PrecioCompra)
                  IntCantidad = int(Cantidad)
                  UtilidadEmpresa =  UtilidadEmpresa - (IntCantidad * IntPrecioCompra)
               # if Nombre is none
               
               
               
               Corriendo = Tabla()
         #if Corriendo == 1
         
         
         
         
         if (Corriendo == 2):
               print("Cual es el nombre del cliente ?")
               ClienteNombre = input()
               
               print("Cual es su nit ?")
               ClienteNit = input()
               
               print("Cual es el codigo del articulo que desea comprar el cliente ?")
               Codigo = input()
               
               Nombre, Cantidad, PrecioCompra, PrecioVenta = CodigoTreeV4.bplustree.retrieve(Codigo)
               
               if (Nombre is None):
                     print("No se encontro el producto. Proceso abortado.")
               #if nombre is None
               
               if (Nombre is not None):
                     print("El cliente desea comprar", Nombre[0])
                     print("Hay un total de", Cantidad, "disponible en el inventario")
                     print("Cuanto desea comprar el cliente?")
                     print("La unidad cuesta", PrecioVenta[0])
                     ClienteCompra = 0
                     CantidadRestante = -1
                     while (CantidadRestante < 0):
                           ClienteCompra = int(input())
                           IntCantidad = int(Cantidad[0])
                           CantidadRestante = IntCantidad - ClienteCompra
                           
                           if (CantidadRestante < 0):
                                 print("No puede comprar esa cantidad el cliente")
                                 print("No hay sufisamiente en el inventario")
                                 print("Que desea hacer?")
                                 print("1) Volver a ingresar una cantidad")
                                 print("2) Abortar proceso")
                                 Opcion = int(input())
                                 
                                 if Opcion == 1:
                                       print("Vuelve a ingresar la cantidad que desea comprar el cliente:")
                                 #if opcion == 1
                                 
                                 if Opcion == 2:
                                       print("Proceso abortado.")
                                       break
                                 #if opcion == 2
                                 
                           #if Cantidad restante < 0
                           
                     #While CantidadRestante < 0
                    
                     
                     if (CantidadRestante >= 0):
                           StringClienteCompra = str(ClienteCompra)
                           StringCantidad = str(CantidadRestante)
                           CodigoTreeV4.bplustree.CantidadModif(Codigo, StringCantidad)
                           
                           CodigosFacturas = CodigosFacturas + 1
                           StringCodigosFacturas = str(CodigosFacturas)
                           
                           IntPrecioVenta = int(PrecioVenta[0])
                           ClienteDebePagar = IntPrecioVenta * ClienteCompra
                           StringClienteDebePagar = str(ClienteDebePagar)
                           
                           TreeFacturas.treefacturas.Insert(StringCodigosFacturas, ClienteNit, ClienteNombre, Nombre, StringClienteCompra, StringClienteDebePagar)
                           print("Se genero la factura exitosamente!")
                           
                           
                           UtilidadEmpresa = UtilidadEmpresa + (ClienteCompra * IntPrecioVenta)
                           
                     #if Cantidad Restante >= 0
                     
               #if nombre is not None
               
               Corriendo = Tabla()
         #if Corriendo == 2
         
         
         
         if (Corriendo == 3):
               
               print("La utilidad acutal de la empresa es de:", UtilidadEmpresa)
               
               
               Corriendo = Tabla()
         #if Corriendo == 3
         
         
         
         if (Corriendo == 4):
               
               #Imprimo todo el arbol
               CodigoTreeV4.bplustree.show()
               
               
               Corriendo = Tabla()
         #if Corriendo == 4
         
         
         
         
         if (Corriendo == 5):
               TreeFacturas.treefacturas.show()
               Corriendo = Tabla()
         #if Corriendo == 5
         
         
         #        Entrada invalilda
         if (Corriendo < 1 or Corriendo > 6):
            print("Entrada invalida.")
            Corriendo = Tabla()
         #If Corriendo < 1 or Corriendo > 6
   #While Corriendo != 6
   
   
   if (Corriendo == 6):
         print("Ok, adios!")
   #if Corriendo == 6

#def Runner



def Tabla():
   print(" ")
   print("Que es lo que quiere hacer?")
   print("1) Entrada de articulos.")
   print("2) Salida / Venta de articulos.")
   print("3) Calculo de la utilidad total de la empresa.")
   print("4) Mostrar todo el inventario.")
   print("5) Mostrar todas las ventas.")
   print("6) Salir.")
   
   Seleccionado = int(input())
   
   return(Seleccionado)
# def Tabla





























































#fin.