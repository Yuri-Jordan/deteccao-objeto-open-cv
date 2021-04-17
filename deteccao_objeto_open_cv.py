#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2, numpy, os


# In[59]:


pathFrames = r'\assets\caxorrimFrames'
#pathFrames = r'\assets\dogDriftFrames'
#pathFrames = r'\assets\gatoPiscinaFrames'
diretorioFrames = os.getcwd() + pathFrames


# In[60]:


foregroundModel = cv2.createBackgroundSubtractorMOG2()


# In[61]:


def reduzir_ruidos(foregroundMask):
    morf = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    return cv2.morphologyEx(numpy.float32(foregroundMask), cv2.MORPH_OPEN, morf)


# In[62]:


def aplicar_mascara(frame):
    foregroundMask = foregroundModel.apply(frame)
    foregroundMask = reduzir_ruidos(foregroundMask)
    matrizVazia = numpy.zeros(frame.shape, numpy.uint8)
    matrizVazia[:,:,0], matrizVazia[:,:,1], matrizVazia[:,:,2] = foregroundMask, foregroundMask, foregroundMask
    frameConcat = numpy.hstack((frame, matrizVazia))
    return frameConcat


# In[ ]:


for nomeframe in os.listdir(diretorioFrames): 
    
    caminhoFrame = os.path.join(diretorioFrames, nomeframe)
    
    frame = cv2.imread(caminhoFrame)
    frame = cv2.resize(frame, dsize=(600, 400))
    frameConcat = aplicar_mascara(frame)
    
    
    cv2.imshow('Teste', frameConcat)
    cv2.waitKey(20)
    
cv2.destroyAllWindows()


# In[ ]:




