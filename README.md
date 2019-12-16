# automationReplicasetMongoDB
This is script replicaset  automation to mongodb, writing in python.

O objetivo deste projeto é a automatização da instalação e configuração de uma replicação (simples) de um ambiente de mongoDB. Assim, o usuário pode ter em poucos minutos uma replicação de três serviços (nós de mongoDB) para testes e desenvolvimento em uma maquina *stand alone*.

Como dicionário de dados, vamos chamar o projeto de robô.
<br>

Sugestões: 
* Rode o robô em uma maquina virtual.
* Antes de executar o robô, crie um snapshot da maquina virtual.
<br>

OBS. Para mongoDB, o robô utilizará distribuição da Percona mongoDB

---
<br>

## Pré requisitos:

* Linux CentOS (Distribuições suportadas: 6, 7 e 8) - (Proxíma versão suportará também Debian 9 e 10);
* Conexão com a internet;
* Python 3;
* Ser administrador da máquina;
* Ip fixo.

<br>

## Instalação:

Baixe o projeto para um diretório dentro do sistema operacional ao qual irá hospedar o conjunto de replicas.

Entre no diretório principal do projeto, teremos um arquivo e uma pasta:
* src
* index.py
<br>

## Execução:
<br>

> **>python from DeployMongoDB.index import C_index as c**

> **c.cor_index()** 
<br>

... Agora é aguardar o robô concluír a instalação e a configuração do ambiente de replicação-=.

O robô fará os seguintes passos:

* Verifica qual o sistema operacional em uso;
* Verifica qual versão do sistema operacional em uso;
* Verifica qual versão do Python em uso. Caso seja < que 3, o robô interromperá a instalação e sugerirá a instação do Python 3;
* Instalação de dependência: wget
* Download mongoDB de acordo com a versão/distribução do sistema operacional;
* Cria diretório para extração dos binários do Percona MongoDb: /usr/perconaMongodb/;
* Copia o arquivo de download do Percona MongoDB para o diretório criado na etapa anterior;
* Extrai o arquivo de download;
* Instala a distribuição do Percona MongoDB no sisema operacional;
* Inicia o serviço do Percona MongoDB;
* Cria os diretório de dados para cada um dos serviços de replicação: Raiz /mongodb;
* Cria um arquivo de KeyFile para que as replicas se "enxerguem";
* Altera o *Owner* do diretório raiz (/mongodb) para usuário mongod;
* Instala requerimento: pip3;
* Instala pymongo através do pip3;
* Cria um usuário com permissão de root no mongodb; (O robô exibirá o nome de usuário e senha ao termino de sua execução);
* Reconfigura mongo.conf para o IP atual do host;
* Reconfigura a porta padrão para conexão no mongodb de 27017 para 47017;
* Habilita na configuração de mongo.conf o modo de autenticação;
* Habilita na configuração de mongo.conf o modo de replicação;
* Subistitui na configuração de mongo.conf o dbpath para Raiz /mongodb;
* Reinicia o serviço do mongodb;
* Testa o novo usuário e senha; (saída será o resultado do comando show dbs);
* Cria diretório para replicar a configuração do mongo.conf: /etc/mongo_config;
* Replica 2 copias do mongo.conf para o diretório criado na etapa anterior;
* Em cada uma das cópias do mongo.conf para os serviços de replicação são alterados os: 
dbpath para cada um dos diretórios criados no diretório raiz /mongodb; <br>
Altera a porta padrão com base na porta reconfigurada, adicionando + 1.<br>
Exemplo: Master: 47017. Nó 2: 47018. Nó 3: 47019; <br>
Altera o IP do host adicionado ao mongo.conf de cada uma das cópias adicionando + 1. <br>
Exemplo: Master 10.11.11.1. Nó2: 10.11.11.2. Nó 3: 10.11.11.3;<br>
* Para o serviço do mongodb;
* Inicia o serviço de replicação; 1 para cada nó na máquina, ao total de 3 serviços;
* Configuração da replicação:
* Adiciona cada um dos nós ao nó principal eleito como Master;
* Insere 1001 linhas no eleito Master;
* Exibi IP, Porta, Usuário e senha para poder conectar ao nó Master.
<br>

String de conexão para nó master:
> mongo --host *IPHost* --port 47017 -u *Usuário* -p *Senha*
<br>

A string de conexão para os nós slaves, basta subistituir somar + 1 final do IP e da Porta do Master.
<br>
Exemplo:
<br>

Master: --host 10.10.11.1  --port 47017;<br>
Slave-01: --host 10.10.11.2 --port 47018;<br>
Slave-01: --host 10.10.11.3 --port 47019;<br>

---
Agora basta entrar em um dos nós slaves, colocar como leitura **rs.slaveOk()** e verificar se os dados foram replicados:
<br>
> use test;<br>
> db.test.percona.find({}).count();<br>
> db.test.percona.find({}).top(10);<br>





