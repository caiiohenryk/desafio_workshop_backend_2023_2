# Aplicação fictícia para requisição de dados sobre Boletins de Ocorrência pra Polícia. Feito para o **desafio da Fábrica de Software**
***
## Passo-a-passo de como utilizar/clonar o código:
- Primeiro, deve-se ler o requirements.txt, presente na própria source do repositório.

- Lá contém informações sobre todas as packages necessárias para o bom funcionamento do código!

- O código inteiro contém comentários sobre o funcionamento e deve ser de fácil entendimento mesmo para aqueles que não tem muita experiência com programação/criação de CRUDs.

***
## Servidor
- O servidor utilizado foi o **PostgreSQL**, usei-o através do pgAdmin4.

***
## Como testar o funcionamento do código?
- Após instalar tudo que é necessário para o funcionamento do código (acesse requirements.txt), você deve inserir os seguintes códigos num terminal:

```python manage.py makemigration```
```python manage.py migrate```
```python manage.py runserver```

- Após inserir estes comandos, o terminal deve te retornar um IP de uso (~~do seu localhost~~).

- Ao dar **Ctrl+click no IP**, você será redirecionado para a página inicial do projeto. Pode navegar entre as tabelas de classes inserindo /admin/**,** /pessoa **ou** /ocorrencia ao final do url de seu navegador.

- Nestas sessões, você pode inserir itens à tabela que serão enviados diretamente ao banco de dados **PostgreSQL**.

- Você pode atualizar ou deletar algum objeto inserido apenas colocando seu ID após a URL (por exemplo: __/pessoa/1/__), usuários com permissão de admnistrador conseguem apagar ou atualizar objetos diretamente da página de administrador (/admin/)

- A páginação foi feita de forma simples, porém pode ser vista dentro das páginas já citadas acima!

***
# Sobre o código
- O melhor entendimento sobre o funcionamento da aplicação será através da leitura dos comentários feitos no código. Recomendo começar pelo 'models.py' presente na pasta 'police_app'

***

# Espero que goste ;D