import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")

def adicionar():
    tarefa= entry_task.get()
    if tarefa != "":
        listbox_tasks.insert(tkinter.END, tarefa)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Tarefa!", message="Seleciona uma tarefa.")

def deletar():
    try:
        tarefa_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(tarefa_index)
    except:
        tkinter.messagebox.showwarning(title="Tarefa!", message="Seleciona uma tarefa.")



quadro_tarefas = tkinter.Frame(root)
quadro_tarefas.pack()

listbox_tasks = tkinter.Listbox(quadro_tarefas, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

barra_tarefas = tkinter.Scrollbar(quadro_tarefas)
barra_tarefas.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=barra_tarefas.set)
barra_tarefas.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=56)
entry_task.pack()

button_adicionar = tkinter.Button(root, text="Adicionar", width=50, command=adicionar)
button_adicionar.pack()

button_deletar = tkinter.Button(root, text="Deletar", width=50, command=deletar)
button_deletar.pack()



root.mainloop()