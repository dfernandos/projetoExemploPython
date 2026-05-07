# Projeto escolar — Flask, SQLite e SQLAlchemy (didático)

Projeto de referência para aulas de **Python**, **API HTTP** e **banco de dados relacional**. O domínio é simples: **professores**, **turmas** e **alunos**. A ideia é que o aluno reconheça o mesmo vocabulário das aulas de SQL (`CREATE TABLE`, chaves estrangeiras, `SELECT`), mas agora com **Python**, **Flask** e **SQLAlchemy**.

---

## Sumário

1. [O que este projeto ensina](#1-o-que-este-projeto-ensina)
2. [Stack tecnológica](#2-stack-tecnológica)
3. [Organização das pastas e arquivos](#3-organização-das-pastas-e-arquivos)
4. [Ideias que vale a pena explicar em sala](#4-ideias-que-vale-a-pena-explicar-em-sala)
5. [Pré-requisitos no Windows](#5-pré-requisitos-no-windows)
6. [Passo a passo — Prompt de Comando (CMD)](#6-passo-a-passo--prompt-de-comando-cmd)
7. [Passo a passo — PowerShell](#7-passo-a-passo--powershell)
8. [Como saber se deu certo](#8-como-saber-se-deu-certo)
9. [Relacionar com SQL “puro”](#9-relacionar-com-sql-puro)
10. [Problemas frequentes no Windows](#10-problemas-frequentes-no-windows)

---

## 1. O que este projeto ensina

| Tema | Onde aparece no código |
|------|-------------------------|
| Definir tabelas como classes Python | `models.py` |
| Conectar ao SQLite e criar sessões | `database.py` |
| Criar tabelas e inserir dados com script | `setup_database.py` |
| Separar “regra de banco” das rotas HTTP | `servicos.py` |
| Expor URLs que devolvem JSON | `app/routes.py` |
| Montar a aplicação Flask | `app/__init__.py`, `run.py` |

Fluxo mental para o aluno:

1. Os **modelos** descrevem o esquema (como um `CREATE TABLE` conceitual).
2. O script **`setup_database.py`** materializa esse esquema no arquivo **`instance/app.db`** e insere dados de exemplo.
3. O **Flask** só recebe pedidos HTTP e pede aos **serviços** que leiam o banco e devolvam listas em formato adequado para JSON.

---

## 2. Stack tecnológica

- **Python 3** — linguagem.
- **Flask** — framework web minimalista (rotas, respostas JSON).
- **SQLAlchemy** — camada que traduz classes Python em tabelas SQL e permite consultas orientadas a objetos (sem Flask-SQLAlchemy neste projeto, para a sessão do banco ficar explícita).
- **SQLite** — banco em um único arquivo (`instance/app.db`), ideal para laboratório.

Dependências declaradas em `requirements.txt`: **Flask** e **SQLAlchemy**.

---

## 3. Organização das pastas e arquivos

```
project-python-from-scratch/
├── README.md                 ← este guia
├── requirements.txt          ← lista de bibliotecas
├── run.py                    ← sobe o servidor de desenvolvimento
├── config.py                 ← SECRET_KEY e pasta instance
├── database.py               ← engine, SessionLocal, Base, URL do SQLite
├── models.py                 ← Professor, Turma, Aluno
├── setup_database.py         ← recria tabelas e popula dados (rode antes da API)
├── servicos.py               ← consultas ao banco usadas pelas rotas
├── app/
│   ├── __init__.py           ← factory create_app()
│   └── routes.py             ← URLs /api/...
└── instance/
    └── app.db                ← criado após rodar setup_database.py (não versionar)
```

> **Nota:** a pasta `instance/` pode não existir antes do primeiro `setup_database.py`; o código cria o diretório quando necessário.

---

## 4. Ideias que vale a pena explicar em sala

**Engine** (`database.py`)  
Pense como o “motor” que sabe falar com o arquivo SQLite.

**SessionLocal e `session`** (`database.py`, `servicos.py`, `setup_database.py`)  
Uma **sessão** é um ciclo de trabalho: você consulta ou altera dados e depois **fecha** a sessão. Isso aproxima o aluno da ideia de transação (`commit` / `rollback`).

**Base e modelos** (`models.py`)  
Cada classe representa uma **tabela**; atributos `Column` representam **colunas** e `ForeignKey` representam **chaves estrangeiras**.

**Blueprint** (`app/routes.py`)  
Agrupa rotas com prefixo `/api` sem misturar tudo num único arquivo gigante.

**Separação `servicos` × `routes`**  
As rotas só dizem *qual URL* e *qual formato de resposta* (JSON). Os serviços concentram *como* ler o banco — é o mesmo padrão de muitos projetos reais.

---

## 5. Pré-requisitos no Windows

1. **Python 3 instalado** a partir de [python.org](https://www.python.org/downloads/).
2. Durante a instalação, marque **“Add python.exe to PATH”**.
3. Abra um terminal:
   - **Prompt de Comando**: tecla Windows, digite `cmd`, Enter.
   - **PowerShell**: tecla Windows, digite `PowerShell`, Enter.

Confira se o Python responde:

```bat
python --version
```

Se aparecer erro do tipo “não é reconhecido”, teste o **launcher** oficial:

```bat
py --version
```

Daqui em diante, sempre que aparecer `python` nos comandos e no seu PC só funcionar `py`, **substitua** `python` por `py` (é comum em algumas instalações).

---

## 6. Passo a passo — Prompt de Comando (CMD)

Execute os passos **na ordem**. Troque o caminho pela pasta onde você guardou o projeto (por exemplo `Documents`).

### 6.1 Entrar na pasta do projeto

```bat
cd %USERPROFILE%\Documents\project-python-from-scratch
```

> Se o projeto estiver em outro lugar, use o caminho completo, por exemplo:  
> `cd D:\disciplinas\project-python-from-scratch`

Confira se `run.py` e `requirements.txt` estão aí:

```bat
dir run.py
dir requirements.txt
```

### 6.2 Criar o ambiente virtual (uma vez por máquina ou quando quiser ambiente limpo)

O ambiente virtual isola as bibliotecas **deste** projeto das demais instalações do Windows.

```bat
python -m venv .venv
```

(Se falhar, use `py -m venv .venv`.)

### 6.3 Ativar o ambiente virtual

```bat
.venv\Scripts\activate.bat
```

Quando estiver ativo, o prompt costuma começar com `(.venv)`.

### 6.4 Atualizar o pip (opcional, recomendado)

```bat
python -m pip install --upgrade pip
```

### 6.5 Instalar as dependências do projeto

O arquivo `requirements.txt` lista Flask e SQLAlchemy. O comando correto usa **`-r`** (traço e letra **r**) e **espaço** antes do nome do arquivo:

```bat
pip install -r requirements.txt
```

> Erro comum: digitar `-requirements` em vez de `-r requirements.txt`. O `-r` significa “ler pacotes **de** um arquivo”.

### 6.6 Criar o banco e inserir dados de exemplo

Este passo **apaga e recria** as tabelas e popula professores, turmas e alunos de laboratório:

```bat
python setup_database.py
```

Você deve ver mensagens no console (“Limpando e criando tabelas…”, “Sucesso!” etc.).  
O arquivo **`instance\app.db`** será criado ou atualizado.

### 6.7 Subir o servidor Flask

```bat
python run.py
```

Deixe essa janela **aberta**. O servidor fica escutando em **http://127.0.0.1:5000** (ou `localhost:5000`).

Para parar o servidor: **Ctrl+C**.

---

## 7. Passo a passo — PowerShell

Os passos são os mesmos; mudam só **ativar o venv** e, às vezes, política de scripts.

### 7.1 Ir para a pasta do projeto

```powershell
cd $env:USERPROFILE\Documents\project-python-from-scratch
```

### 7.2 Criar e ativar o ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se aparecer erro de **execução de scripts**, rode uma vez (por usuário):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois tente ativar de novo:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 7.3 Instalar dependências, banco e servidor

```powershell
pip install -r requirements.txt
python setup_database.py
python run.py
```

---

## 8. Como saber se deu certo

### 8.1 Pelo navegador (com `python run.py` rodando)

Abra:

- http://127.0.0.1:5000/api/professores  
- http://127.0.0.1:5000/api/turmas  
- http://127.0.0.1:5000/api/alunos  

Você deve ver **JSON** (listas de objetos com `id`, `nome`, etc.).

### 8.2 Pelo CMD ou PowerShell (outra janela, com o servidor ainda rodando)

No **Windows 10/11** costuma existir `curl`:

```bat
curl -s http://127.0.0.1:5000/api/professores
```

No **PowerShell**, se preferir:

```powershell
(Invoke-WebRequest -Uri http://127.0.0.1:5000/api/professores -UseBasicParsing).Content
```

---

## 9. Relacionar com SQL “puro”

Depois de rodar `setup_database.py`, abra `instance\app.db` com o **DB Browser for SQLite** ([sqlitebrowser.org](https://sqlitebrowser.org/)) ou outra ferramenta e execute:

```sql
SELECT * FROM professores;
SELECT * FROM turmas;
SELECT * FROM alunos;
```

Isso fecha o ciclo: **modelo Python** → **arquivo SQLite** → **consulta SQL textual**.

---

## 10. Problemas frequentes no Windows

| Sintoma | O que verificar |
|---------|------------------|
| `python` não é reconhecido | Instalar Python com PATH ou usar `py` no lugar de `python`. |
| Erro ao abrir `requirements.txt` | Usar `pip install -r requirements.txt` (com `-r` e espaço). |
| Porta 5000 ocupada | Fechar outro programa que use a porta ou alterar a porta em `run.py` (argumento `port=` em `app.run`). |
| API retorna erro vazio / 500 | Rodar de novo `python setup_database.py` e conferir se `instance\app.db` existe. |
| PowerShell não ativa `.venv` | Ajustar `ExecutionPolicy` (seção 7.2). |

---

## Resumo em uma frase

**Instale dependências → rode `setup_database.py` → rode `run.py` → teste as URLs `/api/...` no navegador.**

Bons estudos.
