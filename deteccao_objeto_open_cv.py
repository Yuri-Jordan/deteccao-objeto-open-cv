#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2, numpy, os


# In[11]:


pathFrames = r'\assets\caxorrimFrames'
#pathFrames = r'\assets\dogDriftFrames'
#pathFrames = r'\assets\gatoPiscinaFrames'
diretorioFrames = os.getcwd() + pathFrames


# In[12]:


for nomeframe in os.listdir(diretorioFrames): 
    caminhoFrame = os.path.join(diretorioFrames, nomeframe)
    frame = cv2.imread(caminhoFrame)
    frame = cv2.resize(frame, dsize=(600, 400))
    cv2.imshow('Teste', frame)
    cv2.waitKey(30)
    
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




