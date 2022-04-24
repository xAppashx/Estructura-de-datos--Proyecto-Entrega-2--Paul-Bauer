#Version 1 de la implementacion de un B+ Tree para un inventario
#Creador: Paul Bauer
#Carnet: 20210060

class Node(object):
      
      def __init__(self, orden):
            self.orden = orden
            self.codigos = []
            self.nombres = []
            self.leaf = True
      #Def __Init__
      
      
      
      # Añadimos un nuevo key(codigo)-Value(nombre) al nodo
      def add(self, codigo, nombre):
      
            if not self.codigos:
                  self.codigos.append(codigo)
                  self.nombres.append([nombre])
                  return None
            # if not self.codigos
            
            for Loop, item in enumerate(self.codigos):
                  
                  if codigo == item:
                           self.nombres[Loop].append(nombre)
                           break
                  #if codigo == item
                  
                  elif codigo < item:
                           self.codigos = self.codigos[:Loop] + [codigo] + self.codigos[i:]
                           self.nombres = self.nombres[:Loop] + [nombre] + self.nombres[i:]
                           break
                  #elif Codigo < item
                  
                  elif ( Loop + 1 == len(self.codigos) ):
                           self.codigos.append(codigo)
                           self.nombres.append([nombre])
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
            
            right.codigos = self.codigos[:medio]
            right.nombres =  self.nombres[:medio]
            
            #
            self.codigos = [right.codigos[0]]
            self.nombres = [left, right]
            self.leaf = False
            
      #def Split
      
      
      
      
      #Devolver True si el nodo esta lleno
      def is_full(self):
            return len(self.codigos) == self.orden
      #def Node Full
      
      
      
      
      #Imprimir los codigos de cada nivel
      def show(self, contador = 0):
            print(contador, str(self.codigos))
            
            if not sefl.leaf:
                  for item in self.nombres:
                        item.show(contador + 1)
                  #for item
            #if not self leaf
            
      #def show
      
      
#class Node





class BPlusTree(object):
      
      def __init__(self, orden = 8):
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
      
      
      
      
      def insert(self, codigo, nombre):
            
            padre = None
            hijo = self.root
            
            while not hijo.leaf:
                  padre = hijo
                  hijo, index = self._find(hijo, codigo)
            #while not hijo.leaf
            
            hijo.add(codigo, nombre)
            
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
                        return hijo.nombres[Loop]
                  #if codigo == item
            #for Loop, item in enumerate
            
            return None
            
      #def Retrieve
      
      
      def show(self):
            self.root.show()
      #def Show
      
      
      
      
#Class B+ Tree


bplustree = BPlusTree(orden = 15)

bplustree.insert('a', 'alpha')
bplustree.insert('b', 'bravo')
bplustree.insert('c', 'charlie')
bplustree.insert('d', 'delta')
bplustree.insert('e', 'echo')




print(bplustree.retrieve('a'))
































































#fin.