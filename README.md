````markdown
# Portfólio Desktop | Elieuton Lemos Jr.

![Badge Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Badge CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![Badge Status](http://img.shields.io/static/v1?label=STATUS&message=FINALIZADO&color=GREEN&style=for-the-badge)

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
* **Design Patterns:** Orientação a Objetos (Herança de classes e encapsulamento de views).

---

## 🚀 Como Executar

### Pré-requisitos
Você precisa ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.

### Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/lemosjr/seu-repo-portfolio-desktop.git](https://github.com/lemosjr/seu-repo-portfolio-desktop.git)
````

2.  Instale a biblioteca necessária:
    ```bash
    pip install customtkinter packaging
    ```

### Execução

Rode o arquivo principal:

```bash
python portfolio.py
```

*(Ou `python3 portfolio.py` dependendo do seu sistema)*

-----

## 📂 Estrutura do Código

O código foi organizado para simular uma aplicação escalável:

  * **`DATA` Dictionary:** Atua como um "Model", armazenando as informações do perfil.
  * **`PortfolioApp` Class:** Classe principal que herda de `ctk.CTk`, gerenciando a janela e a navegação.
  * **`SectionFrame` Class:** Classe utilitária para padronizar os títulos e áreas de rolagem das seções.
  * **Métodos `create_*_frame`:** Responsáveis por renderizar cada "página" da aplicação separadamente.

-----

## 📬 Contato

**Elieuton da Silva Lemos Junior** *Desenvolvedor Full Stack & Estudante de Engenharia de Telecomunicações*

  * 📧 **Email:** lemosjunior8751@outlook.com
  * 💼 **LinkedIn:** [linkedin.com/in/dev-elieuton-d-s-lemos-junior](https://www.google.com/search?q=https://www.linkedin.com/in/dev-elieuton-d-s-lemos-junior)
  * 🐙 **GitHub:** [github.com/lemosjr](https://www.google.com/search?q=https://github.com/lemosjr)

-----

Desenvolvido com 🐍 e 💙 por Elieuton Lemos Jr.

```
```