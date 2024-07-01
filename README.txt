************** Autor ***************
Jeovani Paxe

********** Descrição do projecto *********
Tema: API to do List
Descrição: Uma API para criar, listar, atualizar e excluir tarefas.

Com essa API é possivel pode fazer o gerenciamento de tarefas onde o usuario possa visualizar os trabalhos
ou as tarefas que ela pode realizar, os que ainda estao em falta e caso uma tarefa for concluida ele 
podera excluir facilmente. 

E para isso usei o framwork FastAPI para a criaçao desta mesma API.

Operações CRUD:
    * Create: Adicionar uma nova tarefa.
    * Read: Listar todas as tarefas ou uma tarefa específica.
    * Update: Atualizar o status ou os detalhes de uma tarefa.
    * Delete: Excluir uma tarefa.

*********** Libs usadas ***********
FastAPI
BaseModel
List

************* Instalação ***********
pip install fastapi
obs: Instalara todos os pacotes necessarios para o uso.

************* Como executar ***********
uvicorn index:app --reload

************** Para testar a API *********
http://127.0.0.1:8000/docs