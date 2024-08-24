
import OperacionesConjuntos as op

conjuntos= []
A=[1,2,3]
B=[4,5,6,2]
#C=[6,7,8,2]

conjuntos.append(A)
conjuntos.append(B)
#conjuntos.append(C)


print("Conjunto A",A)
print("Conjunto B",B)
#print("Conjunto C",C)

print("Unión de conjuntos",op.union(conjuntos))

print("Intersección de conjuntos",op.interseccion(conjuntos))

print("Diferencia de conjuntos",op.diferencia(conjuntos))

print("Diferencia simétrica de conjuntos",op.diferenciaSimetrica(conjuntos))

print("Subconjunto",op.subconjunto(conjuntos))

print("Superconjunto",op.superconjunto(conjuntos))