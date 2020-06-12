# App do Desafio
Este repositório apresenta um app que soluciona o problema proposto.
O App que trabalha baseado na arquitetura REST.
Em seu desenvolvimento foi usada a linguagem Python, junto ao framework Django

### Requisitos atendidos:
- CRUD dos funcionários (Baseado nos métodos HTTP)
- API com os relatórios de idade e salário dos funcionários

### Requisitos de funcionamento em uma Máquina Local:
Python instalado (v. 3.5; 3.6; 3.7 ou 3.8)<br/>
Bibliotecas Para desenvolvimento com django (disponíveis no arquivo "bibliotecas.txt")<br/>
(Opcional) - Aplicativo para trabalhar no padrão REST - {Insomnia, Advances REST Client}

### Procedimento de uso da aplicação
1. Fazer download do código fonte da aplicação disponibilizadan neste repositório
2. Abrir o Prompt de Comando
3. Ir até o diretório venv/Scripts
4. rodar o arquivo activate.bat (Inicializa um ambiente virual criado pelo Django para que o sistema funcione)
5. Com o venv inicializado, Deve-se ir ao diretório "api" que se encontra na pasta principal.
7. Dentro do diretório api, o comando "python manage.py runserver" deve ser realizado pra iniciar o servidor
6. A partir desse momento o projeto está funcionando. Basta enviar as requisições ao servidor.

#### Exemplos de requisições
As requisições feitas devem ser realizadas com um Token, que serve pra autenticar e garantir mais seguranca<br/>

Token:  c08d773479e40d24a20066947425311a14303755<br/>

Ex:
> curl -H "Content-type: application/json" -H "Authorization: Token c08d773479e40d24a20066947425311a14303755" localhost:8000/employees/

A requisição acima irá listar todos os funcionários cadastrados como mostrado na imagem abaixo

![request-response](https://user-images.githubusercontent.com/64163998/84538023-de34fe00-acbe-11ea-9d41-ad3e2239886c.png)






