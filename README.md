# Geocontainer - Cadastro de Sítios Geológicos MOSIS LAB - Projeto Técnicas de Programação
Projeto para entrega de trabalho da disciplina de Técnicas de Programação
O uso de ferramentas computacionais, no âmbito das geociências, cresce a cada dia, tornando assim essencial a criação de ferramentas que auxiliem na centralização dos dados oriundos das coletas de campo realizadas para as mais diversas atividades do ramo das geociências, como mineração, geologia do petróleo etc. O projeto Geocontainer tem como objetivo centralizar uma cadastros de amostras, que contenham o nome do pesquisador responsável, o nome do sítio geológico correspondente a amostra, as coordenadas geográficas do local e uma breve descrição de características que definem a rocha. Estas informações centralizadas no banco de dados podem ser exportadas para outros softwares GIS que trabalham com linguagens SQL  podendo assim o profissional ter um banco de dados acessível aos softwares convencionais de trabalho para o geocientista, que pode ser atualizado através de uma página web, assim contando com um incremento de dados de diversos outros parceiros de pesquisa ou de grupos de trabalho. O sistema parte da utilização do Docker e sua capacidade de estrutura em microserviços, que possibilita a conexão entre aplicação, serviço web e o banco de dados. 

## Microserviços necessários:



#### 1. Para a reprodução do projeto é necessária a instalação do software Docker Desktop. Após a instalação do aplicativo, é necessário o download dos códigos anexados ao projeto Geocontainer e sua localização em um diretório de interesse. 

#### 2. Após os downloads necessários, através de um terminal shell, localizado no diretório onde os arquivos do projeto Geocontainer se encontram-se, aplica-se o comando : 
	Docker-compose up
#### 3. O Docker irá iniciar o Docker-compose.yml, que irá dar início aos serviços listados no código. 
#### 4. Para acessar o serviço web, digita http://localhost:80



#### 5. Digite as informações do sitio geológico nos campos listados


#### 6. Aperte em Salvar

#### 7. Mensagem com os itens listado aparece na tela, confirmando o registro no banco de dados. 
