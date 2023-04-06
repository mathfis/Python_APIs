# Python_APIs

## DESCRIÇÃO

API que acessa dois arquivos contendo informações sobre consultas e o cadastro de pessoas profissionais de saúde, sendo capaz de acessar, criar, editar e excluir cadastros de ambos.


## ARQUIVOS DE ENTRADA

"consultas.json" --> arquivo em formato json com informações sobre consulta. Cada entrada possui 3 campos, da seguinte forma que são:
	- "id_consulta" é o campo contendo o código de identificação de cada consulta (int);
	- "data" é o campo com a data da consulta (str);
	- "id_profissional" é o campo contendo o código de identificação da pessoa profissional responsável pela consulta (int). 


"pessoas_profissionais.json" --> arquivo em formato json com informações sobre consulta. Cada entrada possui 3 campos, da seguinte forma que são:
	- "id_profissional" é o campo contendo o código de identificação da pessoa profissional cadastrada (int). 
	- "nome de registro" é o campo contendo o nome de registro da pessoa profissional (str);
	- "nome social" é o campo contendo o nome de registro da pessoa profissional;
	- "especialidade" é a especialidade da pessoa profissional dentro da área da saúde (str).
	
  
## FUNCIONALIDADES

- visualização dos cadastros por id_profissional: "consultas" (id_profissional);
- inserir novo, editar e deletar cadastros: "consultas" (utilizando id_consulta) e "pessoas_profissionais" (utilizando id_profissional).


## AMBIENTE VIRTUAL

  1) Ter instalado na máquina
    - Python 3.7 ou mais recente.
      * Caso não possua o Python instalado, acesse https://www.python.org/downloads/windows/ para obter a versão mais recente. Siga as instruções de instalação, lembrando de adicionar "python.exe" ao PATH (selecionando a segunda caixa na abertura da instalação)  
      ![image](https://user-images.githubusercontent.com/109297697/230498523-b769cd86-3eab-4fea-bfd9-a51f8575fb26.png)

    - Flask
      * Caso não possua o Flask, siga as instruções disponíveis em https://flask.palletsprojects.com/en/2.2.x/installation/
      ![image](https://user-images.githubusercontent.com/109297697/230498746-2811b495-43bd-4c80-aa32-c7cc93847bc6.png)
      
  OBS: a aplicação foi testada apenas em sistema Windows. 
    
  2) Para executar a API, deve-se criar uma pasta em arquivo local contendo os seguintes arquivos:
    - API_consultas.py
    - consultas.json
    - pessoas_profissionais.json
  
  
## EXECUÇÃO
  
  1. No sistema Windows, vá em INICIAR, digite "Prompt de Comando" e acesse o aplicativo;
  2. Navegue até a pasta onde encontra-se o arquivo "API_consultas.py";
  3. Digite  <i> flask --app API_consultas run </i> ;
  
  - Uma mensagem indicando que a API está em execução deve surgir, conforme figura abaixo
  ![image](https://user-images.githubusercontent.com/109297697/230501907-065a46a2-cadf-451e-b675-c7e589ba2f03.png)

## UTILIZAÇÃO

  1. Faça o download e a instalação do aplicativo Postman, disponível em: https://www.postman.com/downloads/
  2. Uma vez no postman, para:
     - Acessar consulta por id_profissional:
        *Método: GET, endereço: http://localhost:5000/consultas/[digite aqui o id_profissional]
     - Inserir nova consulta:
        *Método: POST, endereço: http://localhost:5000/consultas/
     - Inserir nova pessoa profissional:
        *Método: POST, endereço: http://localhost:5000/pprofis/
     - Editar consulta por id_consulta:
        *Método: PUT, endereço: http://localhost:5000/consultas/[digite aqui o novo id_consulta]
     - Editar pessoa profissional por id_consulta:
        *Método: PUT, endereço: http://localhost:5000/pprofis/[digite aqui o novo id_profissional]
     - Editar consulta por id_consulta:
        *Método: DELETE, endereço: http://localhost:5000/consultas/[digite aqui o novo id_consulta]
     - Editar pessoa profissional por id_consulta:
        *Método: DELETE, endereço: http://localhost:5000/pprofis/[digite aqui o novo id_profissional]


## DESENVOLVIMENTO

    - MATHEUS LARA 
      LinkedIn: https://www.linkedin.com/in/laramatheus/ 
      contato: matfis@gmail.com
    
    
