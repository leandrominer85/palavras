#!/usr/bin/env python
# coding: utf-8

# In[12]:


import re

while True:
    entrada = input("Digite a opção desejada: \n 1 - Para pesquisa em palavra inteira \n 2 - Para pesquisa no início da palavra \n 3 - Para pesquisa no fim da palavra \n 0 - Para sair \n")
    
    if entrada == "1":
        subs = input("Digite um termo: ")
        lista = open("palavras.txt", "r", encoding="utf-8")
        res = [x for x in lista if re.search(subs, x)]
        print ("As palavras que contém o termo são: \n")
        print(*res, sep = "\n")
        lista.close()        
        
    elif entrada == "2":
        subs = input("Digite um termo: ")
        lista = open("palavras.txt", "r", encoding="utf-8")
        res = [x for x in lista if x.startswith(subs)]
        print ("As palavras que contém o termo são: \n")
        print(*res, sep = "\n")
        lista.close()
        
    elif entrada == "3":
        subs = input("Digite um termo: ")
        lista = open("palavras.txt", "r", encoding="utf-8")
        res = [x for x in lista if x.endswith(subs + "\n")]
        print ("As palavras que contém o termo são: \n")
        print(*res, sep = "\n")
        lista.close()
        
    else:
        print ("Até Logo")
        break

