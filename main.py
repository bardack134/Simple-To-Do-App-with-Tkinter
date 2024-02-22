from tkinter import *

#creamos ventana
window=Tk()

#configuramos ventana
window.config(bg="black", padx=8, pady=7)

window.title("To-Do App") 

#label de guia al usuario
EnterYourTask_label=Label(window, text='Enter your task', bg="black", fg="white", font=('calibre', 14, 'bold'))
EnterYourTask_label.pack(side=TOP)


#Entry widget que el usuario usara para ingresar la tarea
data_entry_widget=Entry(window, width=30, font=("Helvetica", "14") )
data_entry_widget.pack( pady=7, padx=7)


#Boton de submit
submit_button=Button(window, text='Submit', )
submit_button.pack(pady=7)


#Donde se mostraran las tareas que el usuario vaya agregando
text_widget=Text(window, height=10, width=30, font=("Helvetica", "17"))
text_widget.pack(pady=7, padx=7)


#label dindicando al usuario que ingrese el numero de la tarea a eliminar
elimanate_task_label=Label(window, text='Enter the task number to delete', bg="black", fg="white", font=('calibre', 14, 'bold'))
elimanate_task_label.pack(side=TOP)


#Entry widget que el usuario usara para eliminar una tarea
eliminate=Entry(window, width=5, font=("Helvetica", "15") )
eliminate.pack( pady=7,)


#delete Botton
delete_button=Button(window, text='Delete', )
delete_button.pack(pady=7)





#bucle para que la ventana permaniezca abierta
window.mainloop()