import tkinter
from tkinter import messagebox
import pickle

def check_credentials():
    # Implement the actual authentication process here.
    root.destroy()
    main()

def create_account():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror(title="Error", message="Username and password cannot be empty.")
        return

    with open("user_credentials.txt", "a") as f:
        f.write(f"{username}:{password}\n")

    messagebox.showinfo(title="Success", message="Account created!")

def main():   ## To-Do list application
    root = tkinter.Tk()
    root.title(" To-Do list ")

    def add_task():
        task = entry_task.get()
        if task != "":
            Listbox_tasks.insert(tkinter.END, task)
            entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Warning",message="You must enter a task.")

    def delete_task():
        try:
            task_index = Listbox_tasks.curselection()[0]
            Listbox_tasks.delete(task_index)
        except:
            tkinter.messagebox.showwarning(title="Warning", message="You must select a task.")

    def load_task():
        try:
            tasks = pickle.load(open("tasks.txt","rb"))
            Listbox_tasks.delete(0, tkinter.END)
            for task in tasks:
                Listbox_tasks.insert(tkinter.END,task )
        except:
            tkinter.messagebox.showwarning(title="Warning", message="cannot find tasks.txt")

    def save_task():
        tasks = Listbox_tasks.get(0,Listbox_tasks.size())
        Listbox_tasks.delete(0, tkinter.END)
        pickle.dump(tasks,open("tasks.txt" , "wb"))

    #Create GUI
    frame_tasks= tkinter.Frame(root)
    frame_tasks.pack()

    Listbox_tasks= tkinter.Listbox(frame_tasks, height=10 , width=50 )
    Listbox_tasks.pack(side=tkinter.LEFT)

    scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)

    Listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=Listbox_tasks.yview)

    entry_task = tkinter.Entry(root, width=50)
    entry_task.pack()

    button_add_task=tkinter.Button(root, text="Add task",width=48,command=add_task)
    button_add_task.pack()

    button_delete_task=tkinter.Button(root, text="Delete task",width=48,command=delete_task)
    button_delete_task.pack()

    button_load_task=tkinter.Button(root, text="Load task",width=48,command=load_task)
    button_load_task.pack()

    button_save_task=tkinter.Button(root, text="Save task",width=48,command=save_task)
    button_save_task.pack()

    root.mainloop()
#username password GUI
root = tkinter.Tk()
root.title("Login")

tkinter.Label(root, text="Username:").pack()
entry_username = tkinter.Entry(root)
entry_username.pack()

tkinter.Label(root, text="Password:").pack()
entry_password = tkinter.Entry(root, show='*')
entry_password.pack()

tkinter.Button(root, text="Login", command=check_credentials).pack()

tkinter.Button(root, text="Signup", command=create_account).pack()

root.mainloop()