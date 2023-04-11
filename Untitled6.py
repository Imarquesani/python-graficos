#!/usr/bin/env python
# coding: utf-8

# In[24]:


import matplotlib.pyplot as plt
dias =(1,2,3,4,5,6,7,8,9,10,11,12)

vale5 = [82.2, 79.2, 84.0, 86.4, 84.8, 87.2, 88.8, 92.0, 89.6, 92.8, 95.2, 93.6]
unip6 = [75.0, 73.2, 75.6, 77.4, 78.2, 76.8, 78.0, 81.0, 82.2, 83.6, 83.4, 82.2 ]
bbas3 = [28.3, 27.9, 28.5, 29.2, 29.0, 29.4, 29.7, 30.1, 29.8, 30.2, 30.5, 30.3]
fig, ax = plt.subplots()

ax.plot(dias, vale5, color='green', label='Vele5')
ax.plot(dias, unip6, color='yellow', label='UNIP6')
ax.plot(dias, bbas3, color='red', label='BBAS3')

ax.set_xlabel('Dia')
ax.set_ylabel('Preço R$')
ax.set_title('Titulo')

ax.legend()
plt.show()


# In[ ]:





# In[ ]:




