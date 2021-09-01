matriz=[[2,3,4],[5,6,7],[7,8,9]]
matriz2=[[10,5,6],[9,1,2],[6,4,3]]

for i in range(len(matriz)):
  print(matriz[i])
print()
for i in range(len(matriz2)):
  print(matriz2[i])
  
matriz_resultado=[]

for i in range(len(matriz)): #for por renglones
  #print("Fila: "+str(i))
  fila_matriz=[]
  for j in range(len(matriz[i])): #for por columna
    #print("Columna: "+str(j))
    #print(matriz[i][j])
    fila_matriz.append(matriz[i][j]+matriz2[i][j])
  matriz_resultado.append(fila_matriz)
print()

for i in range(len(matriz_resultado)):
  print(matriz_resultado[i])
  
