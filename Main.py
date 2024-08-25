
import OperacionesConjuntos as op

conjuntos= []
A=[4,2,8]
B=[4,5,6,2]
#C=[6,7,8,2]

conjuntos.append(A)
conjuntos.append(B)
#conjuntos.append(C)


print("Conjunto A",A)
print("Conjunto B",B)
#print("Conjunto C",C)

print("Unión de conjuntos",op.union(A,B))
print("Intersección de conjuntos",op.intersection(A,B))
print("Diferencia de conjuntos",op.difference(A,B))
print("Diferencia simétrica de conjuntos",op.symmetricDifference(A,B))
print("Subconjunto",op.subset(A,B))
print("Superconjunto",op.superset(A,B))



'''
print("Intersección de conjuntos",op.interseccion(conjuntos))

print("Diferencia de conjuntos",op.diferencia(conjuntos))

print("Diferencia simétrica de conjuntos",op.diferenciaSimetrica(conjuntos))

print("Subconjunto",op.subconjunto(conjuntos))

print("Superconjunto",op.superconjunto(conjuntos))
'''