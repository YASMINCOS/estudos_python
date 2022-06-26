
notas=[8,10,8.5]

notas.append(9)
print(notas)
print(notas)

x= notas.pop()
print(notas)
print("x",x)

notas.insert(0,8)
print("após a inserção")
print(notas)


pessoa=["Luiza",23,"9999999"]
print("O nome é", pessoa[0])

valores=[8,9,10,7.5,4]

i=0
total=0

qtd= len(valores)
while i<qtd:
    total=total+valores[i]
    i=i+1
print("Total das notas:",total)

media=total/5
print("A média das notas é:",media)
