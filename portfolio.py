import customtkinter as ctk
import webbrowser

# --- 1. MODEL (SEUS DADOS) ---
# Centralizamos as informações aqui para fácil edição
DATA = {
    "profile": {
        "name": "Elieuton Lemos Jr.",
        "role": "Dev Full Stack & Eng. de Telecomunicações",
        "summary": (
            "Estudante de Engenharia de Telecomunicações (IFCE) e Técnico em Desenvolvimento "
            "de Sistemas (SENAC). Busco estágio em TI/Desenvolvimento.\n\n"
            "Tenho mais de 300h de cursos e experiência prática em projetos acadêmicos, "
            "focando em Python, interfaces modernas e Clean Code."
        ),
        "location": "Fortaleza, Ceará",
        "email": "lemosjunior8751@outlook.com",
        "linkedin": "https://www.linkedin.com/in/dev-elieuton-d-s-lemos-junior",
        "github": "https://github.com/lemosjr"
    },
    "skills": [
        "Python", "CustomTkinter", "JavaScript", "React", 
        "SQL (MySQL/PostgreSQL)", "Git & GitHub", "VS Code", "POO"
    ],
    "education": [
        ("Engenharia de Telecomunicações", "IFCE | 2024 - 2029"),
        ("Técnico em Desenv. de Sistemas", "Senac Brasil | 2025 - 2026"),
        ("Inglês como Segundo Idioma", "IMPARH | 2024 - 2026")
    ],
    "experience": [
        {
            "role": "Desenvolvedor de Projetos Acadêmicos",
            "company": "Senac Brasil (2 meses)",
            "desc": "Criação de GUI modernas em Python com CustomTkinter, focando em UX e POO."
        }
    ]
}

# --- 2. CONFIGURAÇÕES VISUAIS ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class SectionFrame(ctk.CTkScrollableFrame):
    """Classe base para criar seções com rolagem"""
    def __init__(self, master, title, **kwargs):
        super().__init__(master, **kwargs)
        self.title_label = ctk.CTkLabel(
            self, 
            text=title, 
            font=("Roboto Medium", 24), 
            text_color="#3B8ED0" # Azul destaque
        )
        self.title_label.pack(pady=(20, 10), anchor="w", padx=20)

class PortfolioApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title("Portfólio | Elieuton Lemos Jr.")
        self.geometry("900x600")
        
        # Grid Layout (2 colunas: Menu Lateral | Conteúdo Principal)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- MENU LATERAL (Sidebar) ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(5, weight=1)

        # Logo / Nome no Menu
        self.logo_label = ctk.CTkLabel(
            self.sidebar, 
            text="< EL />", 
            font=("Roboto Medium", 20, "bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Botões do Menu
        self.create_sidebar_button("Início", self.show_home, 1)
        self.create_sidebar_button("Sobre", self.show_about, 2)
        self.create_sidebar_button("Habilidades", self.show_skills, 3)
        self.create_sidebar_button("Formação", self.show_education, 4)

        # --- ÁREA DE CONTEÚDO ---
        # Criamos todos os frames, mas mostramos apenas um por vez
        self.home_frame = self.create_home_frame()
        self.about_frame = self.create_about_frame()
        self.skills_frame = self.create_skills_frame()
        self.edu_frame = self.create_education_frame()

        # Inicia na Home
        self.show_home()

    def create_sidebar_button(self, text, command, row):
        btn = ctk.CTkButton(
            self.sidebar, 
            text=text, 
            command=command, 
            fg_color="transparent", 
            text_color=("gray10", "#DCE4EE"), 
            hover_color=("gray70", "gray30"),
            anchor="w"
        )
        btn.grid(row=row, column=0, padx=20, pady=10, sticky="ew")

    # --- FUNÇÕES DE NAVEGAÇÃO ---
    def hide_all_frames(self):
        for frame in [self.home_frame, self.about_frame, self.skills_frame, self.edu_frame]:
            frame.grid_forget()

    def show_home(self):
        self.hide_all_frames()
        self.home_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_about(self):
        self.hide_all_frames()
        self.about_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    
    def show_skills(self):
        self.hide_all_frames()
        self.skills_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_education(self):
        self.hide_all_frames()
        self.edu_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    # --- CRIAÇÃO DAS SEÇÕES (VIEWS) ---
    
    def create_home_frame(self):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        
        # Container centralizado
        inner = ctk.CTkFrame(frame, fg_color="transparent")
        inner.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            inner, 
            text=f"Olá, eu sou\n{DATA['profile']['name']}", 
            font=("Roboto Medium", 32),
            justify="center"
        ).pack(pady=10)

        ctk.CTkLabel(
            inner, 
            text=DATA['profile']['role'], 
            font=("Roboto", 18), 
            text_color="gray"
        ).pack(pady=(0, 30))

        # Botões de Ação
        btn_frame = ctk.CTkFrame(inner, fg_color="transparent")
        btn_frame.pack()

        ctk.CTkButton(
            btn_frame, 
            text="LinkedIn", 
            command=lambda: webbrowser.open(DATA['profile']['linkedin'])
        ).pack(side="left", padx=10)
        
        ctk.CTkButton(
            btn_frame, 
            text="GitHub", 
            fg_color="transparent", 
            border_width=2, 
            text_color=("gray10", "#DCE4EE"),
            command=lambda: webbrowser.open(DATA['profile']['github'])
        ).pack(side="left", padx=10)

        return frame

    def create_about_frame(self):
        frame = SectionFrame(self, "Sobre Mim", fg_color="transparent")
        
        # Texto Resumo
        ctk.CTkLabel(
            frame, 
            text=DATA['profile']['summary'], 
            font=("Roboto", 14), 
            wraplength=600, 
            justify="left"
        ).pack(padx=20, anchor="w")

        # Experiência
        ctk.CTkLabel(
            frame, 
            text="Experiência Recente", 
            font=("Roboto Medium", 18), 
            text_color="#3B8ED0"
        ).pack(pady=(30, 10), padx=20, anchor="w")

        for exp in DATA['experience']:
            card = ctk.CTkFrame(frame, fg_color=("gray85", "gray20"))
            card.pack(fill="x", padx=20, pady=5)
            
            ctk.CTkLabel(card, text=exp['role'], font=("Roboto", 15, "bold")).pack(anchor="w", padx=10, pady=(10,0))
            ctk.CTkLabel(card, text=exp['company'], text_color="gray").pack(anchor="w", padx=10)
            ctk.CTkLabel(card, text=exp['desc'], wraplength=550).pack(anchor="w", padx=10, pady=(5,10))

        return frame

    def create_skills_frame(self):
        frame = SectionFrame(self, "Habilidades Técnicas", fg_color="transparent")
        
        # Grid de Habilidades
        grid_frame = ctk.CTkFrame(frame, fg_color="transparent")
        grid_frame.pack(padx=20, fill="x")
        
        # Colunas dinâmicas (usando grid)
        cols = 3
        for i, skill in enumerate(DATA['skills']):
            card = ctk.CTkFrame(grid_frame, fg_color=("gray85", "gray20"))
            card.grid(row=i//cols, column=i%cols, padx=5, pady=5, sticky="ew")
            
            # Label centralizada no card
            ctk.CTkLabel(card, text=skill, font=("Roboto", 14)).pack(pady=15, padx=10)
        
        # Configurar peso das colunas para esticar igualmente
        for c in range(cols):
            grid_frame.grid_columnconfigure(c, weight=1)

        return frame

    def create_education_frame(self):
        frame = SectionFrame(self, "Formação Acadêmica", fg_color="transparent")

        for curso, inst in DATA['education']:
            card = ctk.CTkFrame(frame, fg_color=("gray85", "gray20"), corner_radius=10)
            card.pack(fill="x", padx=20, pady=8)
            
            # Ícone visual simples (Pipe)
            ctk.CTkLabel(card, text="|", font=("Arial", 30), text_color="#3B8ED0").pack(side="left", padx=(15, 5))
            
            text_frame = ctk.CTkFrame(card, fg_color="transparent")
            text_frame.pack(side="left", pady=10)
            
            ctk.CTkLabel(text_frame, text=curso, font=("Roboto", 15, "bold")).pack(anchor="w")
            ctk.CTkLabel(text_frame, text=inst, text_color="gray").pack(anchor="w")

        return frame

if __name__ == "__main__":
    app = PortfolioApp()
    app.mainloop()