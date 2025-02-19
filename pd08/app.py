
# bibliotecas
from click import style
from shiny import App, ui

# interface do usuário
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Página 1",
        ui.layout_sidebar(
            ui.sidebar(
                ui.markdown(
                    """
                    Uma frase com **negrito** e *itálico*, além de um [Link](https://analisemacro.com.br/).
                    - Item 1
                    - Item 2
                    - Item 3

                    ![](https://aluno.analisemacro.com.br/wp-content/uploads/dlm_uploads/2023/05/logo_am_45.png)                    
                    """
            ),
            bg = "#d3d3d3"
        ),
        "Painel Principal",
        ui.markdown("Texto *markdown*"),
        ui.img(src = "https://aluno.analisemacro.com.br/wp-content/uploads/dlm_uploads/2023/05/logo_am_45.png", width = 55),
        ui.row(
            ui.column(3,"Linha 1 - Coluna A", style = "background-color: gray;"),
            ui.column(3,"Linha 1 - Coluna B", style = "background-color: white;"),
            ),
        ui.row(
            ui.column(3,"Linha 2 - Coluna A", style = "background-color: gray;"),
            ui.column(3,"Linha 2 - Coluna B", style = "background-color: white;"), 
            ),
        ui.layout_columns(
            ui.card(ui.card_header("Título"),"Gráfico 1"),
            ui.card("Tabela A"),
        ),    
        ui.layout_columns(
            ui.card(ui.card_header("Título"),"Gráfico 2"),
            ui.card("Tabela B"),
        ),
        ui.layout_columns(
            ui.card(ui.card_header("Título"),"Gráfico 3"),
            ui.card("Tabela C"),
        ),   
        bg = "#e8e8e8"
        )
    ),
    ui.nav_panel("Página 2", "Conteúdo da Página 2"),
    ui.nav_control(ui.a("Análise Macro", href = "https://analisemacro.com.br/")),
    ui.nav_menu(
        "Saiba mais",
        ui.nav_control(ui.a("Site", href = "https://analisemacro.com.br/")),
        ui.nav_control(ui.a("Blog", href = "https://analisemacro.com.br/blog/"))
    ),
    title = ui.row(
        ui.column(4, ui.img(src = "https://aluno.analisemacro.com.br/wp-content/uploads/dlm_uploads/2023/05/logo_am_45.png")),
        ui.column(8, "Análise Macro")
    ),
    bg = "gray",
    inverse = True,
    window_title = "Análise Macro"
)

# Servidor
def server(input, output, session):
    ...

# Dashboard
app = App(app_ui, server)
