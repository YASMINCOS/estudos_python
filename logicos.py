#not

idade=16
maior_de_idade= idade >=18
menor_de_idade= not maior_de_idade

print("Idade da pessoa:",idade)
print("Maior de idade:",maior_de_idade)
print("Menor de idade:",menor_de_idade)

#and

usuario_correto=True
senha_correta= True
sucesso=usuario_correto and senha_correta
print("Login bem sucedido:",sucesso)

#or
idade=14
idade_min=16
acompanhada_pais= True
pode_assistir=idade >= idade_min or acompanhada_pais
print("Permissão para assistir o filme:",pode_assistir)