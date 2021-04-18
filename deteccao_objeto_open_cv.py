#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2, numpy, os


# In[69]:


pathFrames = r'\assets\caxorrimFrames'
#pathFrames = r'\assets\dogDriftFrames'
#pathFrames = r'\assets\gatoPiscinaFrames'
diretorioFrames = os.getcwd() + pathFrames


# In[70]:


foregroundModel = cv2.createBackgroundSubtractorMOG2()


# In[71]:


def reduzir_ruidos(foregroundMask):
    morf = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    return cv2.morphologyEx(numpy.float32(foregroundMask), cv2.MORPH_OPEN, morf)


# In[75]:


def manter_objetos_significantes(foregroundMask):
    limiar = 100
    a, componentes_conectados = cv2.connectedComponents(numpy.array(foregroundMask > 0, numpy.uint8))
    imagemForeground = numpy.zeros(componentes_conectados.shape)<0
    componentes_unicos = numpy.unique(componentes_conectados.flatten())
    
    for componente in componentes_unicos:
        if componente == 0: #significa que o pixel é de background
            continue
        else:
            componente_conectado = componentes_conectados == componente
            if numpy.sum(componente_conectado) > limiar:
                imagemForeground = imagemForeground | componente_conectado
    return numpy.uint8(255*imagemForeground)


# In[73]:


def aplicar_mascara(frame):
    foregroundMask = foregroundModel.apply(frame)
    foregroundMask = reduzir_ruidos(foregroundMask)
    foregroundMask = manter_objetos_significantes(foregroundMask)
    matrizVazia = numpy.zeros(frame.shape, numpy.uint8)
    matrizVazia[:,:,0], matrizVazia[:,:,1], matrizVazia[:,:,2] = foregroundMask, foregroundMask, foregroundMask
    frameConcat = numpy.hstack((frame, matrizVazia))
    return frameConcat


# In[74]:


for nomeframe in os.listdir(diretorioFrames): 
    
    caminhoFrame = os.path.join(diretorioFrames, nomeframe)
    
    frame = cv2.imread(caminhoFrame)
    frame = cv2.resize(frame, dsize=(600, 400))
    frameConcat = aplicar_mascara(frame)
    
    
    cv2.imshow('Teste', frameConcat)
    cv2.waitKey(20)
    
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




