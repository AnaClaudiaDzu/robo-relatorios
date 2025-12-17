🤖 Robô de Relatórios — Automação em Python

📌 Visão Geral

O Robô de Relatórios é um aplicativo desktop desenvolvido em Python que automatiza a coleta de dados, o processamento das informações e a geração de relatórios em PDF, tudo por meio de uma interface gráfica amigável.

O projeto foi criado com foco em automação de tarefas, boas práticas de arquitetura, multiplataforma (Linux/Windows) e entrega real de software, simulando um cenário comum em empresas: geração automática de relatórios.

##########################################################################################################################################################

🎯 Objetivos do Projeto

Demonstrar habilidades práticas em:

Automação de processos

Desenvolvimento de aplicações desktop

Organização de código em camadas

Processamento de dados

Geração de relatórios profissionais

Empacotamento e distribuição de software

##########################################################################################################################################################

🖥️ Funcionalidades

Interface gráfica em PyQt5

Execução da automação em thread separada (sem travar a UI)

Coleta automática de dados (simulada, pronta para Selenium/Playwright)

Geração de arquivo CSV

Criação de gráfico com Matplotlib

Geração de relatório PDF com ReportLab

Salvamento automático em Documentos/Robo de Relatorios

Botão para abrir a pasta do relatório

Compatível com Linux e Windows

##########################################################################################################################################################

🛠️ Tecnologias Utilizadas

Python 3.10+

PyQt5 — Interface gráfica

Pandas — Manipulação de dados

Matplotlib — Geração de gráficos

ReportLab — Criação de PDFs

PyInstaller — Geração de executável

##########################################################################################################################################################

📂 Estrutura do Projeto

robo_relatorios/
├── main.py
├── ui/
│ └── interface.py
├── core/
│ ├── app_logic.py
│ ├── coletor.py
│ └── relatorio.py
├── assets/
│ └── robo.png
├── requirements.txt
└── README.md

##########################################################################################################################################################

📄 Local de Salvamento dos Relatórios

Os relatórios são salvos automaticamente em:

Documentos/
└── Robo de Relatorios/
├── dados/
│ └── produtos.csv
└── relatorios/
└── relatorio_saucedemo.pdf

##########################################################################################################################################################

🎥 Demonstração

📹 Vídeo de demonstração: (adicione aqui o link do vídeo)

O vídeo mostra:

Abertura do aplicativo

Execução da automação

Geração do relatório

Abertura do PDF

##########################################################################################################################################################

🚀 Possíveis Evoluções

Integração real com Selenium ou Playwright

Buscador de preços em e-commerces

Exportação para Excel

Envio automático por e-mail

Histórico de relatórios

Atualização automática

##########################################################################################################################################################

⬇️ Download

O aplicativo já está disponível em formato executável.

👉 Acesse:
https://github.com/seuusuario/robo-relatorios/releases

- 🪟 Windows: `robo_relatorios.exe`
- 🐧 Linux: `robo_relatorios`

##########################################################################################################################################################

👩‍💻 Autora

Ana Claudia Dzulinski

Projeto desenvolvido para estudo, portfólio e demonstração de habilidades em automação com Python.

##########################################################################################################################################################

📜 Licença

Este projeto é de uso educacional e demonstrativo.
