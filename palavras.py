#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re


# In[4]:


while True:
    subs = input("Digite um termo (ou 0 para sair): ")
    if subs != "0":
        lista = open("palavras.txt", "r", encoding="utf-8")
        res = [x for x in lista if re.search(subs, x)]
        print ("As palavras que contém o termo são: \n")
        print(*res, sep = "\n")
        lista.close()
    else:
        print ("Até Logo")
        break


# In[ ]:




