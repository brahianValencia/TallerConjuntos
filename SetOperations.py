import random

def union(A, B):
    # Initialize an empty list for the union
    setUnion = []
    
    # Add elements from the first list if they are not already in the result list
    for item in A:
        if item not in setUnion:
            setUnion.append(item)
    
    # Add elements from the second list if they are not already in the result list
    for item in B:
        if item not in setUnion:
            setUnion.append(item)
    
    return setUnion


def intersection(A, B):
    # Initialize an empty list for the intersection
    setIntersection = []
    
    # Add elements from the first list if they are in B
    for item in A:
        if item  in B:
            setIntersection.append(item)

    
    return setIntersection


def difference(A, B):
    # Initialize an empty list for the difference
    setDifference = []
    
    # Add elements from the first list if they are not in the second one
    for item in A:
        if item  not in B:
            setDifference.append(item)

    return setDifference

def symmetricDifference(A, B,index,lastElement):
    # Initialize an empty list for the symmetric difference
    setSymmetricDifference = []
    
    if index<lastElement:
       setUnion=union(A,B) 
       return setUnion
    else:
     setUnion=union(A,B)
     setIntersection=intersection(A,B)
    
     setSymmetricDifference=difference(setUnion,setIntersection)
 
    return setSymmetricDifference


def subset(A, B):
    
    if len(B)==0:
        localA=set(A)
        
        localA.pop()
        
        return localA
    else:
        return "It's a subset - They're subsets." if A in B else "It's not a subset - They're not subsets."
    #return B
    #Ternary operator
   # return "It's a subset - They're subsets." if A in B else "It's not a subset - They're not subsets."

def superset(A, B):
   #Ternary operator
   if len(B)==0:
        localA=set(A)
        
        localA.add(str( (int(random.random()*100) )))
        
        return localA
   else:
     return "It's a superset - They're supersets." if A in B else "It's not a superset - They're not supersets."

