usuarios= {"alice","bob","Maria"}
usuarios_2= set(["alice","bob","Lucas"])

print(usuarios== usuarios_2)

print(usuarios)
#sem elementos repetidos
usuarios.add("bob")
print(usuarios)
#adicionando 
usuarios.add("carlos")
print(usuarios)

print(usuarios.union(usuarios_2))
print(usuarios.intersection(usuarios_2))
print(usuarios.difference(usuarios_2))


e_igual=usuarios.union(usuarios_2)== usuarios | usuarios_2
e_igual=usuarios.intersection(usuarios_2)== usuarios &  usuarios_2
e_igual=usuarios.difference(usuarios_2)== usuarios -  usuarios_2
