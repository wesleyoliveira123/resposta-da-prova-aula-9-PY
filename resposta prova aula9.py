import flet as ft
def main(page: ft.Page):
    def adicionar_tarefa(e):
        if tarefa.value:      
            lista_tarefas.controls.append(ft.Text(tarefa.value))
            tarefa.value = ""  
            lista_tarefas.update()  

    page.title = "Lista de Tarefas"
  
    tarefa = ft.TextField(label="Nova tarefa", width=300)
  
    botao_adicionar = ft.ElevatedButton(text="Adicionar Tarefa", on_click=adicionar_tarefa)
   
    lista_tarefas = ft.Column()

    page.add(ft.Row(controls=[tarefa, botao_adicionar]),lista_tarefas)

ft.app(target=main)
