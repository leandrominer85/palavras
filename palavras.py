#!/usr/bin/env python
# coding: utf-8

# # Programa que busca uma lista de palavras em um arquivo de acordo com os parâmetros fornecidos pelo usuário.

# In[ ]:


#Importação dos módulos
import re


# In[ ]:


def main(opcao,n):
    lista = open("palavras.txt", "r", encoding="utf-8")
    lista2 = [x for x in lista if len(x) < n+2]
    
    
    
    if opcao == 1:
        subs = input("Digite um termo: ")
        res = [x for x in lista2 if re.search(subs, x)]
        print ("As palavras que contém o termo são: \n")
        print(*res, sep = "\n")
             
        
    elif opcao == 2:
        subs = input("Digite um termo: ")
        res = [x for x in lista2 if x.startswith(subs)]
        print ("As palavras que contém o termo são: \n")
        print(*res, sep = "\n")
        
        
    elif opcao == 3:
        subs = input("Digite um termo: ")
        res = [x for x in lista2 if x.endswith(subs + "\n")]
        print ("As palavras que contém o termo são: \n")
        print(*res, sep = "\n")
        
        
    elif opcao == 4:
        subs = input("Digite um termo: ")
        res = [x for x in lista2 if re.search(subs, x)]
        
        lista3 = open("palavras.txt", "r", encoding="utf-8")
        inicio = [x for x in lista3 if x.startswith(subs)]
        lista3.close
        lista4 = open("palavras.txt", "r", encoding="utf-8")
        fim = [x for x in lista4 if x.endswith(subs + "\n")]
        lista4.close
        combinada = inicio+fim
        meio = [x for x in res if x not in combinada ]
        print ("As palavras que contém o termo são: \n")
        print(*meio, sep = "\n")
        
    else:
        print ("Até Logo")


# In[ ]:


def entrada():
    global opcao,n
    while True:
        opcao = int(input("Digite a opção desejada:\n        1 - Para pesquisa em palavra inteira\n        2 - Para pesquisa no início da palavra\n        3 - Para pesquisa no fim da palavra\n        4 - Para pesquisa no meio da palavra\n        0 - Para sair \n"))
        if opcao != 0:
            n = int(input("Digite o número de caracteres que deseja para a palavra (0 para infinito)\n"))
        return (opcao , n) 


# In[ ]:


entrada()
main(opcao,n)


# In[ ]:




