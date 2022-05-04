#Version 1 de la implementacion de un B+ Tree para almacenar facturas
#Creador: Paul Bauer
#Carnet: 20210060


class Node(object):
      
      def __init__(self, order):
            self.order = order
            self.codigos = []
            self.nits = []
            self.nombres = []
            self.articulos = []
            self.cantidades = []
            self.pagostotales = []
            self.leaf = True
      #def __init__
      
      
      def add(self, codigo, nit, nombre, articulo, cantidad, pagototal):
            
            if not self.codigos:
                  self.codigos.append(codigo)
                  self.nits.append([nit])
                  self.nombres.append([nombre])
                  self.articulos.append([articulo])
                  self.cantidades.append([cantidad])
                  self.pagostotales.append([pagototal])
                  return None
            #if not self.nits
            
            
            for Loop, item in enumerate(self.codigos.copy()):
                  
                  if codigo == item:
                        self.nits[Loop].append(nit)
                        self.nombres[Loop].append(nombre)
                        self.articulos[Loop].append(articulo)
                        self.cantidades[Loop].append(cantidad)
                        self.pagostotales[Loop].append(pagototal)
                  #if nit == item
                  
                  
                  elif codigo < item:
                        self.codigos = self.codigos[:Loop] + [codigo] + self.codigos[Loop:]
                        self.nits = self.nits[:Loop] + [[nit]] + self.nits[Loop:]
                        self.nombres = self.nombres[:Loop] + [[nombre]] + self.nombres[Loop:]
                        self.articulos = self.articulos[:Loop] + [[articulo]] + self.articulos[Loop:]
                        self.cantidades = self.cantidades[:Loop] + [[cantidad]] + self.cantidades[Loop:]
                        self.pagostotales = self.pagostotales[:Loop] + [[pagototal]] + self.pagostotales[Loop:]
                        break
                  #elif nit < item
                  
                  
                  elif Loop + 1 == len(self.codigos):
                        self.codigos.append(codigo)
                        self.nits.append([nit])
                        self.nombres.append([nombre])
                        self.articulos.append([articulo])
                        self.cantidades.append([cantidad])
                        self.pagostotales.append([pagototal])
                  #elif Loop + 1 == len(self.nits)
                  
            #for Loop, item in enumerate
            
      #def add
      
      
      
      def split(self):
            
            left = Node(self.order)
            right = Node(self.order)
            mid = self.order // 2
            
            left.codigos = self.codigos[:mid]
            left.nits = self.nits[:mid]
            left.nombres = self.nombres[:mid]
            left.articulos = self.articulos[:mid]
            left.cantidades = self.cantidades[:mid]
            left.pagostotales = self.pagostotales[:mid]
            
            right.codigos = self.codigos[mid:]
            right.nits = self.nits[mid:]
            right.nombres = self.nombres[mid:]
            right.articulos = self.articulos[mid:]
            right.cantidades = self.cantidades[mid:]
            right.pagostotales = self.pagostotales[mid:]
            
            self.codigos = [right.codigos[0]]
            self.nits = [left, right]
            self.nombres = [left, right]
            self.articulos = [left, right]
            self.cantidades = [left, right]
            self.pagostotales = [left, right]
            self.leaf = False
            
      #def split
      
      
      
      def is_full(self):
            return len(self.codigos) == self.order
      # def is_full
      
      
      
      
      def show(self):
            
            NumElementos = len(self.codigos)
            
            for Loop in range(NumElementos):
                  if (self.leaf == True):
                        NitDevuelto, NombreDevuelto, ArticuloDevuelto, CantidadDevuelta, PagoTotalDevuelto = treefacturas.retrieve(self.codigos[Loop])
                        print()
                        print("Nombre del cliente:", NombreDevuelto[0])
                        print("Nit:", NitDevuelto[0])
                        print("Articulo que compro:", ArticuloDevuelto[0])
                        print("Cantidad comprada:", CantidadDevuelta[0])
                        print("Total pagado:", PagoTotalDevuelto[0])
                  #if self.leaf == True
            #For Loop in range
            
            if not self.leaf:
                  for item in self.nombres:
                        item.show()
                  #for item in self.nombres
            #if not self.leaf
            
      #def show
      
      
#Class Node





class FacturaTree(object):
      
      def __init__(self, order = 8):
            self.root = Node(order)
      #def __init__
      
      
      def _find(self, node, codigo):
            
            for Loop, item in enumerate(node.codigos):
                  if codigo < item:
                        return node.nombres[Loop], Loop
                  #if codigo < item
            #for Loop, item in enumerate
            
            return node.nombres[Loop + 1], Loop + 1
            
      #def _find
      
      
      
      def _merge(self, parent, child, index):
            
            parent.nombres.pop(index)
            pivot = child.codigos[0]
            
            for Loop, item in enumerate(parent.codigos):
                  
                  if pivot < item:
                        parent.codigos = parent.codigos[:Loop] + [pivot] + parent.codigos[Loop:]
                        parent.nombres = parent.nombres[:Loop] + child.nombres + parent.nombres[Loop:]
                        parent.nits = parent.nits[:Loop] + child.nits + parent.nits[Loop:]
                        parent.articulos = parent.articulos[:Loop] + child.articulos + parent.articulos[Loop:]
                        parent.cantidades = parent.cantidades[:Loop] + child.cantidades + parent.cantidades[Loop:]
                        parent.pagostotales = parent.pagostotales[:Loop] + child.pagostotales + parent.pagostotales[Loop:]
                        break
                  #if pivot < item
                  
                  
                  elif Loop + 1 == len(parent.codigos):
                        parent.codigos += [pivot]
                        parent.nombres += child.nombres
                        parent.articulos += child.articulos
                        parent.cantidades += child.cantidades
                        parent.pagostotales += child.pagostotales
                        break
                  #elif
                  
            #for Loop, item in enumerate
            
      #def Merge
      
      
      
      def Insert(self, codigo, nit, nombre, articulo, cantidad, pagototal):
            
            parent = None
            child = self.root
            
            while not child.leaf:
                  parent = child
                  child, index = self._find(child, codigo)
            #while not
            
            child.add(codigo, nit, nombre, articulo, cantidad, pagototal)
            
            if child.is_full():
                  child.split()
                  
                  if parent and not parent.is_full():
                        self._merge(parent, child, index)
                  # if parent
            #if child is full
            
            
      #def Insert
      
      
      
      def retrieve(self, codigo):
            
            child = self.root
            
            while not child.leaf:
                  child, index = self._find(child, codigo)
            #while not
            
            
            for Loop, item in enumerate(child.codigos):
                  if codigo == item:
                        return child.nits[Loop], child.nombres[Loop], child.articulos[Loop], child.cantidades[Loop], child.pagostotales[Loop]
                  #if key == item
                  
            #for Loop, item in enumerate
            
            return None, None, None, None, None
            
      #def retrieve
      
      
      def show(self):
            self.root.show()
      #def show
      
      
#Class FacturaTree



global treefacturas
treefacturas = FacturaTree(order = 4)

























































#fin.