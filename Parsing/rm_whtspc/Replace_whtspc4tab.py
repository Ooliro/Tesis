#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Abre el archivo limpio de encabezados y colas innecesarios. 
# Todos los archivos de salida de HMMER tienen "#" al inicio así que purga esos.

import re
import sys

infile = input("File's absolute path:") # Pregunta por la ubicación del archivo a convertir
tab = open(infile, 'r')
hmm_tab = tab.read()
tab.close()


# In[7]:


hmm_tab = re.sub(' +', ' ',hmm_tab)

# Reemplaza varios espacios en blanco por solo uno.


# In[8]:


# Guarda esta primera tabla delimitada por espacios simples. No es necesario por ahora!

#save_tab = open('pre_tabbed.tab','w+')
#save_tab.writelines(hmm_tab)
#save_tab = save_tab.close()


# In[9]:


# Abre esta primera tabla delimitada por espacios simples

#tab2 = open(r'/home/rolivares/Documentos/Tesis/lab/pre_tabbed.tab', 'r')
#noht_tab = tab2.read()
#tab2.close()


# In[10]:


final_tab = hmm_tab.replace(' ', '\t')

# Reemplaza los espacios simples por tabs.


# In[17]:


save_tab = open('tabbed.tab','w+')

save_tab.writelines(final_tab)

save_tab = save_tab.close()

print("Done! Your tabbed.tab file is on the same directory as this python script")

# Guarda esta segunda tabla delimitada por tabs.


# In[ ]:




