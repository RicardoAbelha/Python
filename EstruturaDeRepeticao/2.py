#Faça um programa que leia um nome de usuário e a sua senha e não aceite
#  a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
print("faça já seu cadastro: ")
nome = str(input("usuário: "))
senha = str(input("senha: "))
while nome == senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	nome = str(input("usuário: "))
	senha = str(input("senha: "))
else:
	print("cadastrado efetuado com sucesso")
 
print(nome)
print(senha)    
    
    