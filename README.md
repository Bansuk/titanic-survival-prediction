# Sistema de Predição de Sobrevivência do Naufrágio do Titanic  
Um sistema para prever se um(a) passageiro(a) a bordo do Titanic teria sobrevivido ao naufrágio, com base em diversas características.

### Pré-requisitos (mínimos)
```
$ git --version   # v2.34.1
$ pip --version   # v22.0.2
$ python --version   # v3.10.12
```
### Instalação
1. Clone o repositório
```bash
 git clone https://github.com/Bansuk/titanic-survival-prediction-back-end
```

Este projeto usa um ambiente virtual (venv) para isolar as dependências.
2. Crie o ambiente virtual
```bash
python -m venv .venv
 ```

3. Ative o ambiente virtual
```bash
source .venv/bin/activate
 ```

4. Com o venv ativo, instale as dependências
```bash
pip install -r requirements.txt
 ```

### Rodando o Projeto
```bash
python3 src/app.py
```

### Rodando testes (com venv ativo)
```bash
pytest -v src/tests/
```

### Documentação
Com o projeto em execução, acesse [Swagger UI](http://localhost:5000/api/docs/swagger-ui) para obter a documentação dos endpoints na especificação OpenAPI.
### Feito Com
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org)