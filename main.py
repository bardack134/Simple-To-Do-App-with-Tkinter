from tkinter import *

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

#funcion que se ejecutara cuando el usario oprima el boton submit
def submit():
    #usando el metodo get obtenemos la informacion ingresada por el user
    enter_data_get=enter_data.get()
    
    #agregamos la tarea a la lista
    user_data_list.append(enter_data_get)
    
    #imprimo en consola para saber si estamos　leyendo la informacion ingresada por el user correctamente
    print(user_data_list)
    
    #reccoro con un ciclo for la lista de tareas del user 'user_data_list'
    for i in user_data_list:
        
        #con el metodo insert, agrego la informacion escrita por el usuario al text_widget
        text_widget.insert(INSERT, f"{i}\n")

#Entry widget que el usuario usara para ingresar la tarea
data_entry_widget=Entry(window, textvariable=enter_data, width=30, font=("Helvetica", "14") )
data_entry_widget.pack( pady=7, padx=7)


#Boton de submit
submit_button=Button(window, text='Submit', command=submit )
submit_button.pack(pady=7)


#Donde se mostraran las tareas que el usuario vaya agregando
text_widget=Text(window, height=10, width=30, font=("Helvetica", "17"))
text_widget.pack(pady=7, padx=7)

# text_widget.insert(INSERT, "esto es una prueba")

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