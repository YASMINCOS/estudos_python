valor_compra=input("Digite o valor de compra \n")
valor_compra=float(valor_compra)
valor_frete=input("Digite o valor do frete \n")
valor_frete=float(valor_frete)

cupom= valor_compra + valor_frete >=100
print("Prabéns, cupom liberado \n", cupom)


