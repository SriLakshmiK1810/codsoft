import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sqlite3

def addingtask():
    string=a.get()#a
    if len(string)==0:
        messagebox.showerror("Error","No Task is Entered")
    else:
        task.append(string)
        cursor.execute("INSERT INTO task VALUES(?)",(string,))
        update()
        a.delete(0,"end")
def update():
    clear()
    for i in task:
        listbox.insert("end",i)
def delete():
    try:
        value=listbox.get(listbox.curselection())
        if value in task:
            task.remove(value)
            update()
            cursor.execute("DELETE FROM task WHERE title=(?)",(value,))
    except:
         messagebox.showinfo("Error","No Task is Selected.Cannot Delete!")
def delete_all():
    message=messagebox.askyesno("Delete All","Do you want to delete all ?")
    if message==True:
        while(len(task)!=0):
            task.pop()
            cursor.execute(" DELETE FROM task")
            update()
def clear():
    listbox.delete(0,"end")
def close():
    print(task)
    messagebox.askokcancel("close","DO You Want To Exit?")
    gui.destroy()

#main function
if __name__=="__main__":
    gui=t.Tk()
    gui.title("TO-DO LIST")
    gui.geometry("500x450+300+100")
    gui.resizable(0,0)
    gui.configure(bg="blue")
    connection=sqlite3.connect("list.db")
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS task(title text)")
    task=[]
    headerframe=t.Frame(gui, bg = "blue")  
    functionsframe=t.Frame(gui, bg = "blue")
    listboxframe=t.Frame(gui,bg="blue")
    headerframe.pack(fill="both")
    functionsframe.pack(side="left",expand=True,fill="both")
    listboxframe.pack(side="right",expand=True,fill="both")

    headerlabel = t.Label(headerframe,text = "To-Do List",font = ("ALGEBRIAN", "30"),background = "blue",foreground = "white") 
    headerlabel.pack(padx=20,pady=20)
    tasklabel=t.Label(functionsframe,text="ENTER TASK:",font=("calibrian","13","bold"),background="blue",foreground="white")

    tasklabel.place(x=30,y=50)
    a=t.Entry(functionsframe,font=("calibrian","16"),width=18,background="white",foreground="black")
    a.place(x=30,y=80)

    add_button=ttk.Button(functionsframe,text="ADD",width=25,command=addingtask)
    del_button=ttk.Button(functionsframe,text="DELETE ",width=25,command=delete)
    delete_all_button=ttk.Button(functionsframe,text="DELETE ALL",width=25,command=delete_all)
    exit_button=ttk.Button(functionsframe,text="EXIT",width=25,command=close)
    
    add_button.place(x=30,y=120)
    del_button.place(x=30,y=160)  
    delete_all_button.place(x=30,y=200)  
    exit_button.place(x=30,y=240)
    listbox=t.Listbox(listboxframe,width=28,height=15,selectmode="DOUBLE",background=("white"),foreground="black",selectbackground="#99ccff",selectforeground="black")
    listbox.place(x=20,y=40)
    update()
    gui.mainloop()
    connection.commit()
    cursor.close()
