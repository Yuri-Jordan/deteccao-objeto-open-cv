<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<br />

  <h3 align="center">Detector de Objetos em Python com OpenCV</h3>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Conteúdo</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o projeto</a>
    </li>
    <li>
      <a href="#configurando-o-ambiente">Configurando o ambiente</a>
      <ul>
        <li><a href="#pré-requisitos">Pré-requisitos</a></li>
        <li><a href="#instalação">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#contribuição">Contribuição</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre o Projeto

![alt text](/assets/readme/main.png)

Detector de movimento e identificador de objetos de imagens. Consiste em ler os frames de algum vídeo, tratrar cada imagem para que apenas as partes do vídeo que há movimento sejam salvas. Esse projeto foi pensado em ser utilizado junto aos vídeos gerados por câmeras de vigilância, por exemplo, com o intuito de facilitar as buscas por imagens em um banco de dados. 

<!-- GETTING STARTED -->
## Configurando o ambiente

Para ter uma cópia desse projeto local, siga esses passos.

### Pré-requisitos

Para OS Windows, instale o [Python3](https://www.python.org/downloads/release/python-392/) (o python já vem instalado em distribuições Linux).

![alt text](/assets/readme/exe-python.png)

Para facilitar o processo de instalação do das bibliotecas e utilização do Jupyter Notebook, você pode instalar o Python na raíz do seu sistema de arquivos.

![alt text](/assets/readme/custom-install.png)

![alt text](/assets/readme/install-c.png)


Instale as bibliotecas necessárias (instale a cvlib e depois o tensorflow).

* pip3
  ```sh
  pip3 install jupyter
  ```

* pip3
  ```sh
  pip3 install opencv-python
  ```

* pip3
  ```sh
  pip3 install cvlib
  ```

* pip3
  ```sh
  pip3 install tensorflow
  ```

### Instalação

1. Clone o repositório
   ```sh
   git clone https://github.com/Yuri-Jordan/deteccao-objeto-open-cv.git
   ```
2. Vá até a pata raíz do projeto
   ```sh
   cd deteccao-objeto-open-cv
   ```
3. Inicie o ambiente do Jupyter Notebook
   ```sh
   jupyter notebook
   ```

Uma nova janela será aberta em seu browser no endereço: http://localhost:8888/tree.
Clique no arquivo **deteccao_objeto_open_cv.ipynb** e divirta-se!


<!-- CONTRIBUTING -->
## Contribuição

Se você deseja contribuir com o projeto, siga os passos a seguir.

1. Dê um Fork no repositório
2. Crie sua branch de feature (`git checkout -b feature/FeatureTop`)
3. Para facilitar a revisão de código (`jupyter nbconvert deteccao_objeto_open_cv.ipynb --to html`) ou (`jupyter nbconvert deteccao_objeto_open_cv.ipynb --to python`)
4. Comite suas mudanças (`git commit -m 'adiciona uma FeatureTop'`)
5. Push (`git push origin feature/FeatureTop`)
6. Abra um Pull Request

