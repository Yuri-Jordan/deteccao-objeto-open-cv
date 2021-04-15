#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2, numpy, os


# In[14]:


pathFrames = r'\assets\caxorrimFrames'
#pathFrames = r'\assets\dogDriftFrames'
#pathFrames = r'\assets\gatoPiscinaFrames'
diretorioFrames = os.getcwd() + pathFrames


# In[15]:


foregroundModel = cv2.createBackgroundSubtractorMOG2()


# In[16]:


def aplicar_mascara(frame):
    foregroundMask = foregroundModel.apply(frame)
    matrizVazia = numpy.zeros(frame.shape, numpy.uint8)
    matrizVazia[:,:,0], matrizVazia[:,:,1], matrizVazia[:,:,2] = foregroundMask, foregroundMask, foregroundMask
    frameConcat = numpy.hstack((frame, matrizVazia))
    return frameConcat


# In[17]:


for nomeframe in os.listdir(diretorioFrames): 
    
    caminhoFrame = os.path.join(diretorioFrames, nomeframe)
    
    frame = cv2.imread(caminhoFrame)
    frame = cv2.resize(frame, dsize=(600, 400))
    frameConcat = aplicar_mascara(frame)
    
    
    cv2.imshow('Teste', frameConcat)
    cv2.waitKey(30)
    
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




