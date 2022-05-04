#Version 4 de la implementacion de un B+ Tree para un inventario
#Creador: Paul Bauer
#Carnet: 20210060




class Node(object):
      
      
      def __init__(self, order):
            self.order = order
            self.keys = []
            self.nombres = []
            self.cantidades = []
            self.precioscompras = []
            self.preciosventas = []
            self.leaf = True
      #def __init__
      
      
      # Anadir un nuevo nodo
      def add(self, key, nombre, cantidad, preciocompra, precioventa):
            
            if not self.keys:
                  self.keys.append(key)
                  self.nombres.append([nombre])
                  self.cantidades.append([cantidad])
                  self.precioscompras.append([preciocompra])
                  self.preciosventas.append([precioventa])
                  return None
            #if not self.keys
            
            for Loop, item in enumerate(self.keys.copy()):
            
                  if key == item:
                        self.nombres[Loop].append(nombre)
                        self.cantidades[Loop].append(cantidad)
                        self.precioscompras[Loop].append(preciocompra)
                        self.preciosventas[Loop].append(precioventa)
                  #if key == item
                  
                  elif key < item:
                        self.keys = self.keys[:Loop] + [key] + self.keys[Loop:]
                        self.nombres = self.nombres[:Loop] + [[nombre]] + self.nombres[Loop:]
                        self.cantidades = self.cantidades[:Loop] + [[cantidad]] + self.cantidades[Loop:]
                        self.precioscompras = self.precioscompras[:Loop] + [[preciocompra]] + self.precioscompras[Loop:]
                        self.preciosventas = self.preciosventas[:Loop] + [[precioventa]] + self.preciosventas[Loop:]
                        break
                  #elif key < item
                  
                  elif Loop +1 == len(self.keys):
                        self.keys.append(key)
                        self.nombres.append([nombre])
                        self.cantidades.append([cantidad])
                        self.precioscompras.append([preciocompra])
                        self.preciosventas.append([precioventa])
                  #elif Loop + 1 == len(self.keys)
                  
            # for Loop, item in enumerate
            
            
      #def Add
      
      
      #Separa al nodo en 2 y lo salva como padre
      def split(self):
            
            left = Node(self.order)
            right = Node(self.order)
            mid = self.order // 2
            
            left.keys = self.keys[:mid]
            left.nombres = self.nombres[:mid]
            left.cantidades = self.cantidades[:mid]
            left.precioscompras = self.precioscompras[:mid]
            left.preciosventas = self.preciosventas[:mid]
            
            right.keys = self.keys[mid:]
            right.nombres = self.nombres[mid:]
            right.cantidades = self.cantidades[mid:]
            right.precioscompras = self.precioscompras[:mid]
            right.preciosventas = self.preciosventas[:mid]
            
            self.keys = [right.keys[0]]
            self.nombres = [left, right]
            self.cantidades = [left, right]
            self.precioscompras = [left, right]
            self.precioscompras = [left, right]
            self.leaf = False
      #def split
      
      
      #Retorna True si el nodo esta lleno
      def is_full(self):
            return len(self.keys) == self.order
      #Def is full
      
      
      #Imprimir todas las hojas del arbol
      def show(self):
                  
            NumElementos = len(self.keys)
            
            for Loop in range(NumElementos):
            
                  if (self.leaf == True):
                     
                           NombreDevuelto, CantidadDevuelto, PrecioCDevuelto, PrecioVDevuelto = bplustree.retrieve(self.keys[Loop])
                           print()
                           print("Codigo:", self.keys[Loop])
                           print("Nombre:", NombreDevuelto[0])
                           print("Cantidad disponible:", CantidadDevuelto)
                           print("Precio de compra:", PrecioCDevuelto[0])
                           print("Precio de venta:", PrecioVDevuelto[0])
                     
                  #if self.leaf == True
                  
            #for Loop in range(NumElementos)
            
            if not self.leaf:
                  for item in self.nombres:
                        item.show()
                  #for item in self.Nombres
            #if not self.leaf
            
      #def Show
      
      
      # Modificar la cantidad de un producto
      def CantidadModif(self, key, Cantidad):
      
            NumElementos = len(self.keys)
            
            for Loop in range(NumElementos):
            
                  if (self.leaf == True):
                        if self.keys[Loop] == key:
                              self.cantidades[Loop] = Cantidad
                        #if self.keys
                  #if self.leaf == True
                  
            #for Loop in range(NumElementos)
            
            if not self.leaf:
                  for item in self.nombres:
                        item.CantidadModif(key, Cantidad)
                  #for item in self.Nombres
            #if not self.leaf
            
      #def Cantidad Modif
      

#Class Node




class BPlusTree(object):
      
      def __init__(self, order = 8):
            self.root = Node(order)
      #def __init__
      
      
      # Con un key dado, devuelve el index donde esta ese key
      def _find(self, node, key):
            
            for Loop, item in enumerate(node.keys):
                  if key < item:
                        return node.nombres[Loop], Loop
                  #if key < item
            #for Loop, item in enumerate
            
            return node.nombres[Loop + 1], Loop + 1
            
      #def find
      
      
      #Agara los valores del child para copiarlos al padre
      def _merge(self, parent, child, index):
            
            parent.nombres.pop(index)
            pivot = child.keys[0]
            
            for Loop, item in enumerate(parent.keys):
                  
                  if pivot < item:
                        parent.keys = parent.keys[:Loop] + [pivot] + parent.keys[Loop:]
                        parent.nombres = parent.nombres[:Loop] + child.nombres + parent.nombres[Loop:]
                        parent.cantidades = parent.cantidades[:Loop] + child.cantidades + parent.cantidades[Loop:]
                        parent.precioscompras = parent.precioscompras[:Loop] + child.precioscompras + parent.precioscompras[Loop:]
                        parent.preciosventas = parent.preciosventas[:Loop] + child.preciosventas + parent.preciosventas[Loop:]
                        break
                  #if pivot < item
                  
                  elif Loop + 1 == len(parent.keys):
                        parent.keys += [pivot]
                        parent.nombres += child.nombres
                        parent.cantidades += child.cantidades
                        parent.precioscompras += child.precioscompras
                        parent.preciosventas += child.preciosventas
                        break
                  #Elif
                  
            #for Loop, item in enumerate
            
      #def merge
      
      
      
      #inserta un key-nombre pair despues de traversar hacia un leaf node
      def insert(self, key, nombre, cantidad, preciocompra, precioventa):
            
            parent = None
            child = self.root
            
            while not child.leaf:
                  parent = child
                  child, index = self._find(child, key)
            #while not
            
            child.add(key, nombre, cantidad, preciocompra, precioventa)
            
            
            if child.is_full():
                  child.split()
                  
                  if parent and not parent.is_full():
                        self._merge(parent, child, index)
                  # if parent
            #if child is full
            
            
      #def insert
      
      
      
      
      
      #Devuleve el nombre correspondiente a un key conocido
      def retrieve(self, key):
            
            child = self.root
            
            while not child.leaf:
                  child, index = self._find(child, key)
            #while not
            
            
            for Loop, item in enumerate(child.keys):
                  if key == item:
                        #return child.nombres[Loop], child.cantidades[Loop]
                        #print("Found!!", Loop)
                        return child.nombres[Loop], child.cantidades[Loop], child.precioscompras[Loop], child.preciosventas[Loop]
                  #if key == item
                  
            #for Loop, item in enumerate
            
            return None, None, None, None
            
      #def retrieve
      
      
      #Irse a la funccion en Nodo para mostrar todo el arbol
      def show(self):
            self.root.show()
      #def show
      
      #Irse a la funccion en Nodo para anadir una cantidad
      def CantidadModif(self, key, Cantidad):
            child = self.root
            child.CantidadModif(key, Cantidad)
      #def ingreso cantidad
      
      
      
#class BPlusTree





global bplustree
bplustree = BPlusTree(order = 4)




























































#fin.