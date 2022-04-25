#Version 2 de la implementacion de un B+ Tree para un inventario
#Creador: Paul Bauer
#Carnet: 20210060

class Node(object):
      
      def __init__(self, orden):
            self.orden = orden
            self.codigos = []
            self.nombres = []
            self.cantidades = []
            self.precioscompras= []
            self.preciosventas = []
            self.leaf = True
      #Def __Init__
      
      
      
      # Añadimos un nuevo codigo al nodo
      def add(self, codigo, nombre, cantidad, preciocompra, precioventa):
      
            if not self.codigos:
                  self.codigos.append(codigo)
                  self.nombres.append([nombre])
                  self.cantidades.append([cantidad])
                  self.precioscompras.append([preciocompra])
                  self.preciosventas.append([precioventa])
                  return None
            # if not self.codigos
            
            for Loop, item in enumerate(self.codigos):
                  
                  if codigo == item:
                           self.nombres[Loop].append(nombre)
                           self.cantidades[Loop].append(cantidad)
                           self.precioscompras[Loop].append(preciocompra)
                           self.preciosventas[Loop].append(precioventa)
                           break
                  #if codigo == item
                  
                  elif codigo < item:
                           self.codigos = self.codigos[:Loop] + [codigo] + self.codigos[i:]
                           self.nombres = self.nombres[:Loop] + [nombre] + self.nombres[i:]
                           self.cantidades = self.cantidades[:Loop] + [cantidad] + self.cantidades[i:]
                           self.precioscompras = self.precioscompras[:Loop] + [preciocompra] + self.precioscompras[i:]
                           self.preciosventas = self.preciosventas[:Loop] + [precioventa] + self.preciosventas[i:]
                           break
                  #elif Codigo < item
                  
                  elif ( Loop + 1 == len(self.codigos) ):
                           self.codigos.append(codigo)
                           self.nombres.append([nombre])
                           self.cantidades.append([cantidad])
                           self.precioscompras.append([preciocompra])
                           self.preciosventas.append([precioventa])
                  #elif 
                  
            #for i, item in enumerate
            
      #def add
      
      
      
      
      # Separamos al nodo en 2 para salvarlos como hijos
      def split(self): 
            
            left = Node(self.orden)
            right = Node(self.orden)
            medio = self.orden // 2
            
            left.codigos = self.codigos[:medio]
            left.nombres = self.nombres[:medio]
            left.catidades = self.cantidades[:medio]
            left.precioscompras = self.precioscompras[:medio]
            left.preciosventas = self.preciosventas[:medio]
            
            right.codigos = self.codigos[:medio]
            right.nombres =  self.nombres[:medio]
            right.catidades = self.cantidades[:medio]
            right.precioscompras =  self.precioscompras[:medio]
            right.preciosventas = self.preciosventas[:medio]
            
            #
            self.codigos = [right.codigos[0]]
            self.nombres = [left, right]
            self.cantidades = [left, right]
            self.precioscompras = [left, right]
            self.preciosventas = [left, right]
            self.leaf = False
            
      #def Split
      
      
      
      
      #Devolver True si el nodo esta lleno
      def is_full(self):
            return len(self.codigos) == self.orden
      #def Node Full
      
      
      
      
      #Imprimir todo el arbol
      def show(self, contador = 0):
            
            NumElementos = len(self.codigos)
            
            if NumElementos != 0:
               
            
                  for Loop in range(NumElementos):
                        CodeOfElement = self.codigos[Loop]
                        NombreDevuelto, CantidadDevuelto, PrecioCDevuelto, PrecioVDevuelto = bplustree.retrieve(CodeOfElement)
                        print()
                        print("Codigo:", self.codigos[Loop])
                        print("Nombre:", NombreDevuelto[0])
                        print("Cantidad disponible: ", CantidadDevuelto[0])
                        print("Precio de compra:", PrecioCDevuelto[0])
                        print("Precio de compra:", PrecioVDevuelto[0])
                  #for Loop in NumElementos
            #if Num Elementos != 0
            
            else:
                  print("No existen elementos!")
            # else
            
            """
            print(contador, str(self.codigos))
            
            if not self.leaf:
                  for item in self.nombres:
                        item.show(contador + 1)
            """
      #def show
      
      
#class Node





class BPlusTree(object):
      
      def __init__(self, orden = 20):
            self.root = Node(orden)
      # Def __init__
      
      
      def _find(self, node, codigo):
      
            for Loop, item in enumerate(node.codigos):
                  if codigo < item:
                        return node.nombres[Loop], Loop
                  #if Codigo < item
            #for Loop in enumerate
            
            return node.nombres[Loop + 1], Loop + 1
            
      #def _find
      
      
      
      def _merge(self, padre, hijo, index):
            
            padre.nombres.pop(index)
            pivote = hijo.codigos[0]
            
            
            for Loop, item in enumerate(padre.codigos):
                  
                  if pivote < item:
                        padre.codigos = padre.codigos[:Loop] + [pivote] + padre.codigos[Loop:]
                        padre.nombres = padre.nombres[:Loop] + hijo.nombres + padre.nombres[Loop:]
                        break
                  #if pivote < item
                  
                  elif Loop + 1 == len(padre.codigos):
                        padre.codigos += [pivote]
                        padre.nombres =+ hijo.nombres
                        break
                  #elif
                  
            #For Loop, item in enumetare
            
      #def _Merge
      
      
      
      
      def insert(self, codigo, nombre, cantidad, preciocompra, precioventa):
            
            padre = None
            hijo = self.root
            
            while not hijo.leaf:
                  padre = hijo
                  hijo, index = self._find(hijo, codigo)
            #while not hijo.leaf
            
            hijo.add(codigo, nombre, cantidad, preciocompra, precioventa)
            
            #Si el nodo hoja esta lleno, separamos la hoja en 2
            if hijo.is_full():
                  hijo.split()
                  
                  if padre and not padre.is_full():
                        self._merge(padre, hijo, index)
                  #if padre
                  
            #if hijo is full
            
      #def insert
      
      
      
      
      def retrieve(self, codigo):
            
            hijo = self.root
            
            
            while not hijo.leaf:
                  hijo, index = self._find(hijo, codigo)
            #while not
            
            for Loop, item in enumerate(hijo.codigos):
                  
                  if codigo == item:
                        return hijo.nombres[Loop], hijo.cantidades[Loop], hijo.precioscompras[Loop], hijo.preciosventas[Loop]
                  #if codigo == item
            #for Loop, item in enumerate
            
            return None, None, None, None
            
      #def Retrieve
      
      
      def showing(self):
            self.root.show()
      #def Show
      
      
      
      
#Class B+ Tree



#node = Node(orden = 4)
bplustree = BPlusTree(orden = 999)



bplustree.insert('a', 'alpha', '5', '0751', '15')
bplustree.insert('b', 'bravo', '4', '7', '15')
bplustree.insert('c', 'charlie', '7', '7', '15')
bplustree.insert('d', 'delta', '12', '7', '15')
bplustree.insert('e', 'echo', '0', '7', '15')

bplustree.showing()

NombreDevuelto, Cantidad, PrecioDevuelto, PrecioVenta = bplustree.retrieve('a')
#print(bplustree.retrieve('a'))
print()
print(NombreDevuelto[0])
print(PrecioDevuelto[0])



#bplustree.showing()



"""

Aunque asta alli mi codigo parece funccionar bien, lleva un gran error.
Basicamente, estoy poniendo todos los nodos en el root del tree,
por lo tanto no estoy creando un arbol. Obviamente no es lo que busco. 
Esa version alli se queda y empezare una completamente
nueva en donde si creo un arbol como se debe.

"""



























































#fin.