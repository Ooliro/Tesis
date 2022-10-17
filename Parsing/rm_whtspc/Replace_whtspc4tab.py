#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

tab = open(r'/home/rolivares/Documentos/Tesis/lab/raw_res/noheadtail_specdomt.tab', 'r')
hmm_tab = tab.read()
tab.close()

# Abre el archivo limpio de encabezados y colas innecesarios. Todos los archivos de salida de HMMER tienen "#" al inicio así que purga esos.


# In[ ]:


hmm_tab = re.sub(' +', ' ',hmm_tab)

hmm_tab 

# Reemplaza varios espacios en blanco por solo uno.


# In[ ]:


save_tab = open('pre_tabbed.tab','w+')

save_tab.writelines(hmm_tab)

save_tab = save_tab.close()

# Guarda esta primera tabla delimitada por espacios simples


# In[ ]:


tab2 = open(r'/home/rolivares/Documentos/Tesis/lab/pre_tabbed.tab', 'r')
noht_tab = tab2.read()
tab2.close()

# Abre esta primera tabla delimitada por espacios simples


# In[ ]:


final_tab= noht_tab.replace(' ', '\t')

# Reemplaza los espacios simples por tabs.


# In[ ]:


save_tab = open('tabbed.tab','w+')

save_tab.writelines(final_tab)

save_tab = save_tab.close()

# Guarda esta segunda tabla delimitada por tabs.


# In[ ]:




