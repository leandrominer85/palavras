#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import sqlite3
import re


# In[2]:


#Criação do BD se ele não existir
def banco():
    conn= sqlite3.connect("Palavras.db")

    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS palavras(palavras TEXT,UNIQUE(palavras));")

    conn.commit()
    conn.close()
banco()


# In[3]:


#Criar a tabela "palavras" e populá-la 
def tabela():
    conn= sqlite3.connect("Palavras.db")
    cur = conn.cursor()

    l = open("palavras.txt", "r", encoding="utf-8")

    for i in l:
        i = i.rstrip("\n,")
        cur.execute("INSERT OR IGNORE INTO palavras VALUES (?) ", [i])

    conn.commit()

    conn.close()
tabela()


# In[4]:


def lista(n):
    global lista2
    lista2 = []
    
    #importação da lista de palavras e captura do input do usuario
    conn= sqlite3.connect("Palavras.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM palavras")  
    rows = cur.fetchall()
    conn.close()

    #Captura do primeiro item de cada tupla na lista de tuplas "rows"
    lista = [x[0] for x in rows ]

    #caso a opção seja por um número infinito (n=0) então mantemos a lista, senão criamos outra lista
    if n == 0:
        lista2 = lista
    else:
        lista2 = [x for x in lista if len(x) < n+2] #n+2 pois a lista contém o separador /n


# In[5]:


def inteira():
    list1.delete(0,END)
    expressao = e1.get()
    lista(int(e2.get()))
    #procura na lista de palavras pela correspondência em qualquer parte da palavra
    res = [x for x in lista2 if re.search(expressao, x)]
    list1.insert(END,*res)


# In[6]:


def fim():
    list1.delete(0,END)
    expressao = e1.get()
    lista(int(e2.get()))
#procura na lista de palavras pela correspondência no fim da palavra
    res = [x for x in lista2 if x.endswith(expressao)]
    list1.insert(END,*res)


# In[7]:


def meio():
    list1.delete(0,END)
    expressao = e1.get()
    lista(int(e2.get()))
 #procura na lista de palavras pela correspondência no meio da palavra
    res = [x for x in lista2 if re.search(expressao, x)]

    #criação de duas listas, uma para as palavars que começam e outra para a que terminam com o termo.
    lista3 = open("palavras.txt", "r", encoding="utf-8")
    inicio = [x for x in lista3 if x.startswith(expressao)]
    lista3.close
    lista4 = open("palavras.txt", "r", encoding="utf-8")
    fim = [x for x in lista4 if x.endswith(expressao)]
    lista4.close
    #Combinação dessas listas e criação de uma lista com todas as palavras que contém o termo menos as da lista combinada
    combinada = inicio+fim
    meio = [x for x in res if x not in combinada ]
    list1.insert(END,*meio)


# In[8]:


def inicio():
    list1.delete(0,END)
    expressao = e1.get()
    lista(int(e2.get()))
    
#procura na lista de palavras pela correspondência no início da palavra
    res = [x for x in lista2 if x.startswith(expressao)]
    list1.insert(END,*res)


# In[9]:


window = Tk()
window.wm_title("Palavras")


# In[10]:


l1 = Label(window, text="Expressão:")
l1.grid(row=0, column=0)
l2 = Label(window, text="Tamanho máximo da palavra :")
l2.grid(row=1, column=0)


# In[11]:


var=StringVar()
e1=Entry(window,textvariable=var)
e1.grid(row=0,column=1)


# In[12]:


n=StringVar()
e2=Entry(window,textvariable=n)
e2.grid(row=1,column=1)


# In[13]:


l3 = Label(window, text="Lista de palavras:")
l3.grid(row=0, column=3)


# In[14]:


l3 = Label(window, text="  ")
l3.grid(row=0, column=2)


# In[15]:


list1=Listbox(window, height=6,width=35)
list1.grid(row=1,column=3,rowspan=6,columnspan=2)


# In[16]:


sb1=Scrollbar(window)
sb1.grid(row=1,column=5,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
#list1.bind('<<ListboxSelect>>',get_selected_row)


# In[17]:


b1=Button(window,text="Pesquisa em palavra inteira", width=24,command=inteira)
b1.grid(row=2,column=0,columnspan =2)

b2=Button(window,text="Pesquisa no início da palavra", width=24,command=inicio)
b2.grid(row=3,column=0,columnspan = 2 )

b3=Button(window,text="Pesquisa no fim da palavra", width=24,command=fim)
b3.grid(row=4,column=0,columnspan = 2)

b4=Button(window,text="Pesquisa no meio da palavra", width=24,command=meio)
b4.grid(row=5,column=0,columnspan = 2)

b5=Button(window,text="Sair", width=24,command=window.destroy)
b5.grid(row=6,column=0,columnspan = 2)


# In[18]:


window.mainloop()


# In[ ]:





# In[ ]:




