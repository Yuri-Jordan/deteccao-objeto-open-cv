#!/usr/bin/env python
# coding: utf-8

# In[21]:


import cv2, numpy, os


# In[22]:


#pathFrames = r'\assets\caxorrimFrames'
pathFrames = r'\assets\dogDriftFrames'
#pathFrames = r'\assets\gatoPiscinaFrames'
diretorioFrames = os.getcwd() + pathFrames
diretorioFramesFiltrados = os.getcwd() + r'\assets\output'


# In[23]:


foregroundModel = cv2.createBackgroundSubtractorMOG2()
frameEmProcessamento = ''

# variáveis relacionadas a função manter_objetos_tamanho_significante 
limiarTamanhoObjeto = 100

# variáveis relacionadas a gravação de imagens com movimentos 
minimaQuantidadeDeFrames = 2
arrayMovimentoDetectado = []
arrayCapturaDeFrames = []
idxFrameAtual = 0


# In[24]:


def reduzir_ruidos(foregroundMask):
    morf = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    return cv2.morphologyEx(numpy.float32(foregroundMask), cv2.MORPH_OPEN, morf)


# In[14]:


def frames_sao_consecutivos(arrayMovimentoDetectados):
    return arrayMovimentoDetectado[-1] > arrayMovimentoDetectado[-2] + 1


# In[15]:


def salvar_sequencia(arrayCapturaDeFrames, idxFrameAtual, minimaQuantidadeDeFrames, diretorioFramesFiltrados):

    if len(arrayCapturaDeFrames) < minimaQuantidadeDeFrames:
        pass
    else:
        frameSequenciaAtual = 1
        for frame in arrayCapturaDeFrames:
            nomeImagem = str(idxFrameAtual) + '_' + str(frameSequenciaAtual) + '.jpg'
            outPath = os.path.join(diretorioFramesFiltrados, nomeImagem)
            cv2.imwrite(outPath, frame)
            frameSequenciaAtual += 1


# In[16]:


def manter_objetos_tamanho_significante(foregroundMask):
    a, componentes_conectados = cv2.connectedComponents(numpy.array(foregroundMask > 0, numpy.uint8))
    imagemForeground = numpy.zeros(componentes_conectados.shape)<0
    componentes_unicos = numpy.unique(componentes_conectados.flatten())
    
    for componente in componentes_unicos:
        if componente == 0: #significa que o pixel é de background
            continue
        else:
            componente_conectado = componentes_conectados == componente
            if numpy.sum(componente_conectado) > limiarTamanhoObjeto:
                imagemForeground = imagemForeground | componente_conectado
    return numpy.uint8(255*imagemForeground)


# In[17]:


def processar_imagem(arrayMovimentoDetectado, arrayCapturaDeFrames, idxFrameAtual, minimaQuantidadeDeFrames, diretorioFramesFiltrados):
    foregroundMask = foregroundModel.apply(frameEmProcessamento)
    foregroundMask = reduzir_ruidos(foregroundMask)
    foregroundMask = manter_objetos_tamanho_significante(foregroundMask)
    
    
    if numpy.sum(foregroundMask) > 0:
        arrayMovimentoDetectado.append(idxFrameAtual)
        arrayCapturaDeFrames.append(frameEmProcessamento)
        
    if len(arrayMovimentoDetectado) >= 2 and frames_sao_consecutivos(arrayMovimentoDetectado):
        salvar_sequencia(arrayCapturaDeFrames, idxFrameAtual, minimaQuantidadeDeFrames, diretorioFramesFiltrados)
        arrayMovimentoDetectado = []
        arrayCapturaDeFrames = []
    
    
    matrizVazia = numpy.zeros(frameEmProcessamento.shape, numpy.uint8)
    matrizVazia[:,:,0], matrizVazia[:,:,1], matrizVazia[:,:,2] = foregroundMask, foregroundMask, foregroundMask
    frameConcat = numpy.hstack((frameEmProcessamento, matrizVazia))
    return frameConcat


# In[18]:


for nomeframe in os.listdir(diretorioFrames): 
    
    idxFrameAtual += 1
    
    caminhoFrame = os.path.join(diretorioFrames, nomeframe)
    
    frameEmProcessamento = cv2.imread(caminhoFrame)
    frameEmProcessamento = cv2.resize(frameEmProcessamento, dsize=(600, 400))
    frameConcat = processar_imagem(arrayMovimentoDetectado, arrayCapturaDeFrames, idxFrameAtual, minimaQuantidadeDeFrames, diretorioFramesFiltrados)
    
    
    cv2.imshow('Teste', frameConcat)
    cv2.waitKey(20)
    
salvar_sequencia(arrayCapturaDeFrames, idxFrameAtual, minimaQuantidadeDeFrames, diretorioFramesFiltrados)
cv2.destroyAllWindows()


# ## Ler resultado do processamento 

# In[27]:


for nomeframe in os.listdir(diretorioFramesFiltrados): 
    
    
    
    caminhoFrame = os.path.join(diretorioFramesFiltrados, nomeframe)
    
    frame = cv2.imread(caminhoFrame)
    frame = cv2.resize(frame, dsize=(600, 400))    
    
    cv2.imshow('Resultado', frame)
    cv2.waitKey(20)
    
cv2.destroyAllWindows()


# In[ ]:




