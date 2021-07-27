# **Tutorial de configuração para desenvolver com MySQL no Linux utilizando docker**

Este tutorial foi produzido por mim com intuito de ajudar as pessoas que estão iniciando no mundo de desenvolvimento a fim de aprender a configurar o banco de dados MySQL em um container docker em um ambiente de desenvolvimento Linux.

## **1 - Instalação e Configuração do MySQL no Linux**

Para instalação do docker em sua distribuição linux consulte a documentação oficial no link abaixo:

https://docs.docker.com/engine/install/

**1.1 - Criar container docker do MySQL com a versão 8.0.26:**

No link abaixo é possível obter informações sobre a imagem oficial do MySQL no Docker Hub:

https://hub.docker.com/_/mysql

Para manter os dados localmente é necessário criar um diretório em /home para ter a persistência dos dados, use os comandos abaixo:

```
mkdir ~/mysql_data
```

Instale o MySQL na versão 8.0.26 com o comando abaixo:

```
docker run -d \
--name mysql-8.0.26 \
-p 3306:3306 \
-v ~/mysql_data:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD='@#dev2021' \
mysql:8.0.26
```

**1.2 - Verificar se o MySQL foi instalado no docker:**

```
docker ps -a
```

![Screenshot_20210722_121600.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_121600.png)


**1.3 - Executar o container com o MySQL:**

Ao utilizar o comando docker ps -a é possível obter o CONTAINER ID, copie e cole no comando abaixo seu ID:

```
docker start <CONTAINER ID>
```

Ao colar o ID do seu container docker o comando ficará assim:

```
docker start 1dba1feb6b72
```

**1.4 - Parar o funcionamento do container:**

```
docker stop mysql-8.0.26
```

ou

```
docker stop 1dba1feb6b72
```

**1.5 - Iniciar o container:**

```
docker start mysql-8.0.26
```

ou

```
docker start 1dba1feb6b72
```

**2 - Conectar e acessar o banco de dados pelo DBeaver:**

Para download do DBeaver acesse o link abaixo:

https://dbeaver.io/download/

- Ir em: Database > New Database Connection
- Conforme imagem abaixo, clique no icone do MySQL e depois clique em next( botão na parte inferior).

  ![Screenshot_20210722_135708.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_135708.png)

- Confome imagem abaixo, use os seguintes valores:

  - Server Host: localhost
  - Database:
  - Username: root
  - Password(definido durante a instalação do container): @#dev2021

  ![Screenshot_20210722_121804.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_121804.png)

  - Clique em Test Connection para verificar se a configuração está correta e realizar uma conexão com sucesso.

  ![Screenshot_20210722_121826.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_121826.png)

- Agora o MySQL está configurado no DBeaver para uso no Linux conforme imagem abaixo:

  ![Screenshot_20210722_122111.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_122111.png)

## **3 - Criar e acessar um banco de dados utilizando python**

**3.1 - Criar ambiente virtual:**

Requisitos:

- Necessário ter o python na versão 3.xx instalado em seu sistema operacional, para instalação acesse o link abaixo:

  https://www.python.org/

- Crie uma pasta com o nome desejado, abra o pasta criada no visual studio code e dentro dela crie o ambiente virtual conforme abaixo.

- Necessário ter o virtualenv instalado, para instalação acesse link abaixo:

  https://virtualenv.pypa.io/en/latest/installation.html

  Ou utilize o comando abaixo:

  ```
  pip install virtualenv
  ```

- Criar ambiente virtual do python:

  ```
  virtualenv venv
  ```

- Ativar ambiente virtual: 

  ```
  source venv/bin/activate
  ```

- Verificar se o path do python aponta para o ambiente virtual criado após a ativação:

  ```
  which python
  ```

  Conforme imagem abaixo é possível verificar que o path do python realmente aponta para o ambiente virtual, caso o 
  seu não aponte para a pasta do ambiente virtual, ative novamente o ambiente virtual.

  ![Screenshot_20210722_122810.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_122810.png)


- Se clonar o repositório, crie o ambiente virtual e instale o requirements.txt com o comando abaixo:

  ```
  pip install requirements.txt
  ```

**3.2 - Instalar o MySQL Connector como dependencia para o python ter acesso ao banco de dados a ser criado:**

```
pip install mysql-connector-python
```

**3.3 - Criar arquivo para acessar o MySQL e criar banco de dados**

- Crie uma pasta src e dentro dela crie um arquivo chamado createdb.py

- Digite o código abaixo:

 ```python
from getpass import getpass
from mysql.connector import connect, Error

# Estabece conexão com o MySQL
try:
    with connect(
        host="localhost",
        # username = root
        user=input("Digite o username: "),
        # password = @#dev2021
        password=getpass("Digite o password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE TUTORIAL_MYSQL"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

  ```

- Agora digite o comando abaixo para acessar o MySQL e criar um banco de dados:

  ``` python
  python src/createdb.py
  ```

  Conforme imagem abaixo digite o usuário(root) e a senha(@#dev2021):

  ![Screenshot_20210722_124338.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_124338.png)

- Abra o DBeaver, clique com botão direito do mouse sobre Databases no canto esquerda da tela. Vai abrir um menu, clique
em refresh. Conforme imagem abaixo é possível ver que o banco de dados foi criado:

  ![Screenshot_20210722_133412.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_133412.png)

**3.4 - Criar tabelas no banco de dados**

- Crie um arquivo chamado create_tables.py

- Digite o código abaixo:

```python
from getpass import getpass
from mysql.connector import connect, Error

try:
    # Estabelece conexão com o MySQL
    with connect(
        host="localhost",
        user=input("Digite o username: "),
        password=getpass("Digite o password: "),
        database="TUTORIAL_MYSQL",
    ) as connection:
        # Cria tabelas no banco de dados TUTORIAL_MYSQL
        create_movies_table_query = """
        CREATE TABLE movies(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR(4),
            genre VARCHAR(100),
            rate INT
        )
        """
        create_reviewers_table_query = """
        CREATE TABLE reviewers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
        )
        """
        create_ratings_table_query = """
        CREATE TABLE ratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
            PRIMARY KEY(movie_id, reviewer_id)
        )
        """
        # Caso a conexão seja um sucesso as queries serão executadas no banco de dados
        with connection.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            cursor.execute(create_reviewers_table_query)
            cursor.execute(create_ratings_table_query)
            connection.commit()
except Error as e:
    print(e)

```

- Agora digite o comando abaixo para criar as tabelas no banco de dados:

  ``` python
  python src/create_tables.py
  ```

![Screenshot_20210722_125523.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_125523.png)


- Abra o DBeaver, clique com botão direito do mouse sobre Tables no canto esquerda da tela. Vai abrir um menu, clique
em refresh. Conforme imagem abaixo é possível ver que as tabelas foram criadas no banco de dados:

![Screenshot_20210722_125505.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210722_125605.png)

**3.4 - Diagrama do banco de dados criado:**

![diagram.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/database/diagram/diagram.png)

**3.5 - Considerações finais:**

O objetivo desse tutorial não é fazer um CRUD(Create, Read, Update, Delete), mas sim aprender a utilizar MySQL com Docker.
Se sinta a vontade para fazer um CRUD e criar seu próprio banco de dados.

## **4 - Error Public Key Retrieval is not allowed**

Existe a possibilidade de ao reiniciar o banco de dados no docker acontecer o error Public Key Retrieval is not allowed.
Caso isso aconteça, siga os passos abaixo para habilitar o allowPublicKeyRetrieval como TRUE.

![Screenshot_20210723_172649.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210723_172649.png)

- Clique com o botão direito do mouse sobre o localhost do MySQL, depois vá em Edit Connection > Driver properties, em allowPublicKeyRetrieval coloque a váriavel como TRUE.

![Screenshot_20210723_172717.png](https://github.com/lipegomes/tutorial-como-instalar-mysql-no-docker-linux/blob/main/assets/img/Screenshot_20210723_172717.png)

Pronto o MySQL está pronto novamente para uso.

###  Operational System:

- [Manjaro](https://manjaro.org/)

###  Programs Used:

- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [Dbeaver](https://dbeaver.io/)
- [Visual Studio Code](https://code.visualstudio.com/)

### Tools:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/)

### Programming language:

- [Python](https://www.python.org/)

### Data Base in Docker Hub:

- [MySQL](https://hub.docker.com/_/MySQL)
