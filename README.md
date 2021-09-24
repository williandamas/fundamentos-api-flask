# ApiRest com Flask

O projeto consiste em uma api que insere dados (id, idade e nome) de um "Lead" no banco de dados usando o POST, o id é gerado automaticamnete.
O mesmo "Lead" pode ser alterado com o PUT e também pode ser excluido com o DELETE, ambos usando o ID como filtro de busca.
O GET foi criado de duas maneiras, um que busca toda a base de dados enquanto o outro pode ser usado como filtro o id único.

Os dados são apresentados com um contador (count) com a quantidade de leads na base, e com uma lista com os dados de cada lead.



<br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/80868200/134597368-a0b9297f-f5c0-436c-acef-e118b9a3d9db.png" width="850px"/>
</div>
<br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/80868200/134597371-0cb837bf-b197-4075-af6c-9740fc44f058.png" width="850px"/>
</div>
<br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/80868200/134597370-2fdd797f-c0d1-4cd3-85a5-41110d94b034.png width="850px""/>
</div>
<br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/80868200/134597366-7f3609dd-a4f6-4530-bfdc-0d78668224cc.png" width="850px"/>
</div>
<br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/80868200/134597372-d2bc3ce3-31cf-43e7-b158-174a565f69f2.png" width="850px"/>
</div>
<br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/80868200/134597242-b45faf4d-9b07-4441-b770-85b0d3a629b8.png" width="850px"/>
</div>

# Como executar o projeto

Pré-requisitos: Python 3 || Flask || Pydantics || TinyDB

```bash
# Clonar repositório
git clone https://github.com/williandamas/fundamentos-api-flask.git

# Entrar na pasta do projeto 
cd fundamentos-api-flask

# Execultar
flask run

# Abrir Swagger
http://localhost:5000/apidoc/swagger
```

# Autor

<b>Willian de Oliveira Damas</b>

[![Linkedin: Willian](https://img.shields.io/badge/-Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wiillianoliveira/)](https://www.linkedin.com/in/wiillianoliveira/) 
