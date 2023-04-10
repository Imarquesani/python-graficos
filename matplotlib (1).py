#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

fig, ax = plt.subplots()
ax.plot (x, y)

plt.show


# In[27]:


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

fig, ax = plt.subplots()
ax.plot(x, y, color='green', linestyle='--', marker='o', label='Dados')

ax.set_xlabel('Rotulo X')
ax.set_ylabel('Rotulo Y')
ax.set_title('Titulo')

ax.legend()
plt.show()


# In[38]:


import matplotlib.pyplot as plt

rotulos = ['maças','laranjas','bananas', 'uvas', 'figos']
valores = [5, 3, 6, 4, 7]

fig, ax = plt.subplots()
ax.barh(rotulos, valores, color='silver', label='Dados')

ax.set_xlabel('Fruta')
ax.set_ylabel('Quantidade')
ax.set_title('Quantidade de frutas')

ax.legend()
plt.show()


# In[10]:


import matplotlib.pyplot as plt

rotulos=['maças','laranjas','banana', 'uvas', 'figos']
tamanhos=[50, 30, 64, 45, 70]
cores=['red', 'orange', 'yellow', 'purple', 'blue']

fig, ax = plt.subplots()
ax.pie(tamanhos, labels=rotulos, colors=cores, autopct='%1.1f%%')

ax.set_title ('Distribuição das Frutas')

plt.show()


# In[8]:


#Grafico de Dispersão
import matplotlib.pyplot as plt
import numpy as np
#Gerar um conjunto de dados aleartórios
np.random.seed(123)
x = np.random.normal(0, 1, 50)
y = np.random.normal(0, 1, 50)

#Criar figura e eixo
fig, ax = plt.subplots()

#criar gráfico de dispersão
ax.scatter(x,y)

#inserir rótulos de dados e título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scatterplot')

#Exibir o grafico
plt.show()


# In[ ]:





# In[ ]:




