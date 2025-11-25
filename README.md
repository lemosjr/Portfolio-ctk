````markdown
# Portfólio Desktop | Elieuton Lemos Jr.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge" alt="CustomTkinter Badge">
  <img src="http://img.shields.io/static/v1?label=STATUS&message=FINALIZADO&color=GREEN&style=for-the-badge" alt="Status Badge">
</div>

<br>

## 🖥️ Sobre o Projeto

Este projeto é uma aplicação **Desktop** desenvolvida em Python que funciona como um portfólio interativo.

O objetivo foi demonstrar competências em **Desenvolvimento de Software**, criação de **Interfaces Gráficas (GUI)** modernas e aplicação de conceitos de **Programação Orientada a Objetos (POO)**. Diferente de um site, esta aplicação roda localmente na máquina do usuário, simulando um software corporativo ou utilitário.

---

## 🎨 Funcionalidades

* **Interface Moderna:** Utiliza a biblioteca `customtkinter` para um visual "Dark Mode" nativo e limpo, superior ao Tkinter padrão.
* **Navegação SPA (Single Page Application):** Sistema de menu lateral que alterna entre as telas (Home, Sobre, Skills, Formação) sem recarregar a janela.
* **Dados Centralizados:** Todo o conteúdo (textos, experiências, links) está separado da lógica visual, facilitando a manutenção.
* **Interatividade:** Botões funcionais que abrem links externos (LinkedIn, GitHub) no navegador padrão.
* **Layout Responsivo:** Uso de Grid Layout (`sticky="nsew"`) para que a aplicação se adapte ao redimensionamento da janela.

---

## 🛠 Tecnologias Utilizadas

* **Linguagem:** [Python](https://www.python.org/)
* **GUI Framework:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Wrapper moderno para o Tkinter)
* **Design Patterns:** Orientação a Objetos (Herança de classes e encapsulamento de views)

---

## 🚀 Como Executar

### Pré-requisitos
Você precisa ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/lemosjr/portfolio-desktop.git](https://github.com/lemosjr/portfolio-desktop.git)
    ```

2.  **Entre na pasta do projeto:**
    ```bash
    cd portfolio-desktop
    ```

3.  **Instale as bibliotecas necessárias:**
    ```bash
    pip install customtkinter packaging
    ```

### Execução

Rode o arquivo principal:

```bash
python portfolio.py
````

*(Caso não funcione, tente `python3 portfolio.py` dependendo da configuração do seu sistema)*

-----

## 📂 Estrutura do Código

O código foi organizado para simular uma aplicação escalável e fácil de manter:

| Componente | Função |
| :--- | :--- |
| **`DATA` Dictionary** | Atua como um "Model", armazenando todas as informações do perfil (JSON-like). |
| **`PortfolioApp`** | Classe principal (Controller) que gerencia a janela e a navegação entre telas. |
| **`SectionFrame`** | Classe utilitária para padronizar o design dos títulos e áreas de rolagem. |
| **`create_*_frame`** | Métodos responsáveis por construir e renderizar cada "página" visualmente. |

-----

## 📬 Contato

**Elieuton da Silva Lemos Junior** *Desenvolvedor Full Stack & Estudante de Engenharia de Telecomunicações*

  * 📧 **Email:** lemosjunior8751@outlook.com
  * 💼 **LinkedIn:** [linkedin.com/in/dev-elieuton-d-s-lemos-junior](https://www.google.com/search?q=https://www.linkedin.com/in/dev-elieuton-d-s-lemos-junior)
  * 🐙 **GitHub:** [github.com/lemosjr](https://www.google.com/search?q=https://github.com/lemosjr)

-----

\<div align="center"\>
Desenvolvido com 🐍 e 💙 por Elieuton Lemos Jr.
\</div\>

```

### O que eu melhorei:

1.  **Centralização das Badges:** Coloquei as badges dentro de uma `div align="center"` para ficarem centralizadas e visualmente mais bonitas no topo.
2.  **Link do Git Clone:** Corrigi o erro onde o link aparecia duplicado (`[...] (...)`). Agora está limpo, apenas o comando.
3.  **Tabela de Estrutura:** Transformei a lista da "Estrutura do Código" em uma tabela Markdown. Isso deixa a leitura técnica muito mais agradável e organizada.
4.  **Espaçamento:** Ajustei as quebras de linha para que os parágrafos não fiquem "grudados".
```