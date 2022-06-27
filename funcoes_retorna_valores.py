def calcular_conta (consumo,taxa,desconto):
   servico=consumo  * taxa
   desconto=consumo * desconto
   valor = consumo + servico
   valor=valor-desconto
   return valor

valor= calcular_conta(consumo=90,taxa=0.1, desconto=0.05)
print("O valor a ser pago é:",valor)
