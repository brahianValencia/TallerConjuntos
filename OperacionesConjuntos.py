

def union(conjuntos):
   unionConjuntos=[]

   cantidadConjuntos=len(conjuntos)

   for i in range(cantidadConjuntos):
      
      cantidadElementosConjunto=len(conjuntos[i])

      for j in range(cantidadElementosConjunto):

        if(conjuntos[i][j] not in unionConjuntos):
         
         unionConjuntos.append(conjuntos[i][j])

   return unionConjuntos 
           

def interseccion(conjuntos):
   interseccionConjuntos=[]

   cantidadConjuntos=len(conjuntos)
   
   for i in range(cantidadConjuntos):
      
      cantidadElementosConjunto=len(conjuntos[i])

      for j in range(cantidadElementosConjunto):
         interseccionConjuntos.append(conjuntos[i][j])

   #Toma únicamente los  elementos que estén en todos los conjuntos
   interseccionConjuntos=list(set([x for x in interseccionConjuntos if interseccionConjuntos.count(x) > len(conjuntos)-1]))

   return interseccionConjuntos 



def diferencia(conjuntos):
   diferenciaConjuntos=[]

   cantidadConjuntos=len(conjuntos)
   
   for i in range(cantidadConjuntos-1):
      cantidadElementosConjunto=len(conjuntos[i])

      for j in range(cantidadElementosConjunto):

        if conjuntos[i][j] not in conjuntos[i+1]:
         diferenciaConjuntos.append(conjuntos[i][j])

   return diferenciaConjuntos 


def diferenciaSimetrica(conjuntos):
    conjuntoUnion=[]
    conjuntoInterseccion=[]
    diferenciaSimetrica=[]
    conjuntoUnion=union(conjuntos)
    conjuntoInterseccion=interseccion(conjuntos)
    

    diferenciaSimetrica.append(conjuntoUnion)
    diferenciaSimetrica.append(conjuntoInterseccion)

    diferenciaSimetrica=diferencia(diferenciaSimetrica)

    return diferenciaSimetrica
   

def subconjunto(conjuntos):
    subconjunto=[]
    subconjunto=union(conjuntos)[:-1]
    return subconjunto

def superconjunto(conjuntos):
    superconjunto=[]

    if len(conjuntos)>2: 
        superconjunto=union(conjuntos)
    else:
       superconjunto = [x for x in conjuntos[-2] if x in conjuntos[-1]]
       #No funciona, falta hacerlo para 2
       
    return superconjunto
