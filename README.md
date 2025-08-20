Resumo completo do que fiz
Criou a pasta do projeto controle_despesas
Criou os arquivos:
main.py → menu e execução
despesas_controller.py → funções de adicionar/listar/calcular
database.json → armazenamento das despesas
README.md → descrição do projeto
Rodou o programa no terminal e testou:
Adicionar despesa ✅
Listar despesas ✅
Ver total ✅
Inicializou o Git local na pasta do projeto:

git init
git add .
git commit -m "Projeto controle de despesas inicial"

Criou o repositório no GitHub e conectou o local:

git remote add origin https://github.com/hdelmass/controle_despesas.git
git branch -M main
git push -u origin main


Criou uma branch nova (adicionar_despesas), fez alterações e enviou para o GitHub:

git checkout -b adicionar_despesas
git add .
git commit -m "Teste: adicionando comentário na branch adicionar_despesas"
git push -u origin adicionar_despesas


Merge da branch na main e envio para o GitHub:

git checkout main
git merge adicionar_despesas
git push


Como verificar que está tudo pronto

No GitHub:

Vá para https://github.com/hdelmass/controle_despesas

Veja os arquivos: main.py, despesas_controller.py, database.json, README.md

Veja a branch main com as alterações finais

Veja a branch adicionar_despesas (pode estar lá também)

No terminal:

Digite:

git status


Deve mostrar On branch main e nothing to commit, working tree clean → significa que não há mais alterações pendentes

Rodar o programa de novo:

python main.py


Teste adicionar, listar e ver total de despesas → tudo funcionando

