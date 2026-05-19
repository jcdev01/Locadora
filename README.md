# 🎬 Sistema de Locadora

> Aplicação desktop que simula a experiência de um cliente em uma locadora, permitindo consultar e interagir com itens disponíveis para locação.

---

## 📋 Sobre o Projeto

O **Sistema de Locadora** foi desenvolvido com foco na experiência do usuário final, representando o fluxo real de utilização de uma locadora do ponto de vista do cliente. O projeto aplica conceitos de programação orientada a objetos, organização de software e desenvolvimento de interfaces gráficas com Python.

> ⚠️ O sistema **não contempla funcionalidades administrativas** — é voltado exclusivamente para o uso pelo cliente.


![Dashboard](imagens/screenshot.png)



---


## ✨ Funcionalidades

- 🔐 Tela de login
- 📋 Cadastro de usuário
- 🚗 Dashboard com itens disponíveis para locação
- 📄 Consulta e gerenciamento de contratos
- 💾 Armazenamento local com SQLite

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.x | Linguagem principal |
| CustomTkinter | latest | Interface gráfica moderna |
| SQLite3 | built-in | Banco de dados local |
| Pillow (PIL) | latest | Manipulação de imagens |

---

## 📁 Estrutura do Projeto

```
Locadora/
├── data/                  # Banco de dados
├── imagens/               # Assets e fundos das telas
│   ├── fundo_aluguel.png
│   ├── fundo_cadastro.png
│   ├── fundo_contratos.png
│   ├── fundo_dashboard.png
│   └── fundo_login.png
├── telas/
│   ├── back/              # Lógica e banco de dados
│   │   ├── banco.py
│   │   ├── classes.py
│   │   └── database.db
│   ├── tela_aluguel.py
│   ├── tela_cadastro.py
│   ├── tela_contratos.py
│   ├── tela_dashboard.py
│   └── tela_login.py
├── session.py             # Gerenciamento de sessão
├── main.py                # Ponto de entrada
└── README.md
```

---

## ▶️ Como Executar

### Pré-requisitos

- Python 3.x instalado
- pip

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/jcdev01/Locadora.git

# 2. Acesse a pasta do projeto
cd Locadora

# 3. Instale as dependências
pip install customtkinter pillow

# 4. Execute o projeto
python main.py
```

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido com o objetivo de representar o fluxo de utilização de uma locadora do ponto de vista do cliente, aplicando na prática conceitos como:

- Programação Orientada a Objetos (POO)
- Organização modular de software
- Desenvolvimento de interfaces gráficas desktop
- Persistência de dados com SQLite

---

## 👨‍💻 Autor

Desenvolvido por **[jcdev01](https://github.com/jcdev01)**