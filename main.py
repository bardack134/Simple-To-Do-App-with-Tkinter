from tkinter import *
from tkinter import messagebox

#creamos ventana
window=Tk()

#configuramos ventana
window.config(bg="black", padx=8, pady=7)

window.title("To-Do App") 

#label de guia al usuario
EnterYourTask_label=Label(window, text='Enter your task', bg="black", fg="white", font=('calibre', 14, 'bold'))
EnterYourTask_label.pack(side=TOP)

#lista donde se guardaran las tareas ingresadas por el usuario
user_data_list=[]


enter_data=StringVar()

#variable que determina la posicion de la tarea dentro de nuestro texto 'text_widget'
position=0 

#funcion que se ejecutara cuando el usario oprima el boton submit
def submit():
    global position
    #usando el metodo get obtenemos la informacion ingresada por el user
    enter_data_get=enter_data.get()
    
    #agregamos la tarea a la lista
    user_data_list.append(enter_data_get)
    
    #imprimo en consola para saber si estamos　leyendo la informacion ingresada por el user correctamente
    print(user_data_list)
    
    #con el metodo insert, agrego la informacion escrita por el usuario al text_widget
    list_widget.insert(position, f"[{position}] {enter_data_get}\n")
    
    #aumento la posicion en 1
    position +=1
    
    # Para borrar el contenido del Entry
    data_entry_widget.delete(0, END)
                         
#Entry widget que el usuario usara para ingresar la tarea
data_entry_widget=Entry(window, textvariable=enter_data, width=30, font=("Helvetica", "14") )
data_entry_widget.pack( pady=7, padx=7)


#Boton de submit
submit_button=Button(window, text='Submit', command=submit )
submit_button.pack(pady=7)


#Donde se mostraran las tareas que el usuario vaya agregando
# text_widget=Text(window, height=10, width=30, font=("Helvetica", "17"))
# text_widget.pack(pady=7, padx=7)
list_widget=Listbox(
                  bg = "black",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow",
                  selectmode=MULTIPLE)
list_widget.pack(pady=7, padx=7)

#label dindicando al usuario que ingrese el numero de la tarea a eliminar
elimanate_task_label=Label(window, text='Enter the task number to delete', bg="black", fg="white", font=('calibre', 14, 'bold'))
elimanate_task_label.pack(side=TOP)

#funcion que borra una tarea de la lista de tareas
delete_data=StringVar()

def deleteTask():
    if list_widget.size()==0:
        print("No task")
        messagebox.showerror("No task")
    else:
        delete_data_get=delete_data.get()
        
        list_widget.delete(delete_data_get)

def endTask():

    for i in list_widget.curselection():
        #  la sgt linea  da el texto asociado a ese índice i
        item = list_widget.get(i)
        completed_task_list.insert(position, f"{item}  OK")
    
#Entry widget que el usuario usara para eliminar una tarea
eliminate=Entry(window, textvariable=delete_data, width=5, font=("Helvetica", "15") )
eliminate.pack( pady=7,)


#delete Botton
delete_button=Button(window, command=deleteTask, text='Delete', )
delete_button.pack(pady=7)

#label dindicando al usuario que seleccione las tareas que desea completar
complete_task_label=Label(window, text="Please select the tasks you have completed and click the 'Complete Task' button.",
                        bg="black", fg="white", font=('calibre', 14, 'bold'))
complete_task_label.pack()


#Completar tatera Botton
task_completed_button=Button(window, command=endTask, text='complete task', )
task_completed_button.pack(pady=7)

#Donde se mostraran las tareas que el usuario ha completado
completed_task_list=Listbox(
                  bg = "black",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")
completed_task_list.pack(pady=7, padx=7)


#bucle para que la ventana permaniezca abierta
window.mainloop()