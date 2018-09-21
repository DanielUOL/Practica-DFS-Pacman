def readFileretList(file):
    archivo = open(input_file,'r') 
    return [[ch for ch in line.strip()] for line in archivo.readlines()]

def genVertices(list_):
    return [(i,j) for i in range(len(list_)) for j in range(len(list_[0]))
    if list_[i][j] != '%']


def retAristas(list_):
    A = []
    for i in range(len(list_)):
        for j in range(len(list_[0])):

            if j == (len(list_[0]) - 1):
                if list_[i][j] != '%' and list_[i][0] != '%':
                    A.append([(i,j),(i,0)])
            elif list_[i][j] != '%' and list_[i][j + 1] != '%':
                A.append([(i,j),(i,j + 1)])

            if i == (len(list_) - 1):
                if list_[i][j] != '%' and list_[0][j] != '%': 
                    A.append([(i,j),(0,j)])
            elif list_[i][j] != '%' and list_[i + 1][j] != '%': 
                A.append([(i,j),(i + 1,j)])
    return A

def GenerarHijos(pacman,aristas,visitados):
    hijos = []
    #Verificamos si se puede mover hacia arriba
    if (pacman[0]-1,pacman[1]) not in visitados:
        if [(pacman[0]-1,pacman[1]),(pacman[0],pacman[1])] in aristas:
            hijos.append((pacman[0]-1,pacman[1]))
            
    #Verificamos si se puede mover hacia izquierda
    if (pacman[0],pacman[1]-1) not in visitados:
        if [(pacman[0],pacman[1]-1),(pacman[0],pacman[1])] in aristas:
            hijos.append((pacman[0],pacman[1]-1))
            
    #Verificamos si se puede mover hacia derecha
    if (pacman[0],pacman[1]+1) not in visitados:
        if [(pacman[0],pacman[1]),(pacman[0],pacman[1]+1)] in aristas:
            hijos.append((pacman[0],pacman[1]+1))
            
    #Verificamos si se puede mover hacia abajo
    if (pacman[0]+1,pacman[1]) not in visitados:
        if [(pacman[0],pacman[1]),(pacman[0]+1,pacman[1])] in aristas:
            hijos.append((pacman[0]+1,pacman[1]))
            
    return hijos
	
def DFS(grafo, pacman, fruta):
    aristas = grafo[0]
    visitados = [] # Lista para los nodos que ya se visitaron
    padres = {} # Diccionario para guardar la relación de Hijo-Padre de cada nodo
    ruta = []
    frontera = [] # Pila para los nodos disponibles para moverse
    hijos = []
    frontera.append(pacman)
    # Mientras haya nodos en la frontera se iterará el algoritmo
    while ( frontera ):
        # Se extrae el tope de la frontera (pila)
        nodo = frontera.pop()
        visitados.append(nodo)
        # Se verifica si el nodo actual es la posición de la fruta
        if nodo == fruta:
            # Se imprime el total de nodos visitados y la lista
            print(len(visitados))
            for n in visitados:
                print(n[0], n[1])
            # Se obtiene la ruta buscando los padres desde el nodo final hasta el inicial
            while ( nodo in padres ):
                ruta.append(padres[nodo])
                nodo = padres[nodo]
            ruta.reverse()
            # Se imprime la longitud de la ruta y los nodos que la componen
            print(len(ruta))
            for r in ruta:
                print(r[0], r[1])
            print(fruta[0], fruta[1])
            break
        # Se generan los hijos del nodo actual,
        # con la condición de que no se encuentren en visitados.
        hijos = GenerarHijos(nodo,aristas,visitados)
        for h in hijos:
            # Si el hijo no está en el diccionario Hijo-Padre, se agrega
            if h not in padres:
                padres[h] = nodo
            # Si el hijo no está en la frontera, se agrega
            if h not in frontera:
                frontera.append(h)
				
input_file = 'tablero2.txt' # Nombre del archvio de texto que contiene los datos de entrada para el programa
archivo = open(input_file,'r')

# Se leen las posiciones de Pacman y la fruta
pacmanlst = ((archivo.readline()).strip()).split(' ')
frutalst = ((archivo.readline()).strip()).split(' ')

# Se guardan todas líneas del archivo de texto en una lista,
# eliminando las primeras 3 líneas, para dejar sólo el tablero
lista1 = readFileretList(input_file)
lista1.pop(0)
lista1.pop(0)
lista1.pop(0)

# Se crean tuplas de números enteros para representar las posiciones de pacman y fruta
pacman = (int(pacmanlst[0]),int(pacmanlst[1]))
fruta = (int(frutalst[0]),int(frutalst[1]))

# Se generan los vértices y aristas para el grafo
vertices = genVertices(lista1)
aristas = retAristas(lista1)

# Se crea un grafo con los vertices y aristas obtenidos
grafo = (aristas,vertices)

# Se llama la función de DFS enviando el grafo,
# la posición de pacman y la posición de la fruta
BFS(grafo,(pacman[0],pacman[1]),(fruta[0],fruta[1]))