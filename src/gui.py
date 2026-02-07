import customtkinter as ctk # Lib to GUI creation
import modules as mod # Backend
from tkcalendar import DateEntry # Lib to calendar


# Window parameters
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("720x600")
app.title("TaskManager")
app.resizable(False,False)

# Fonts
font_text = ctk.CTkFont(family="Roboto Condensed",size=16)
font_title = ctk.CTkFont(family="Roboto SemiCondensed",size=24)


#------------------------------------------------------ ADD TASK FUNCTION --------------------------------

def add_task():
    add_window = ctk.CTkToplevel(app)
    add_window.geometry("500x600")
    add_window.title("TaskManager")
    add_window.attributes("-topmost", True)
    add_window.grid_columnconfigure(0,weight=1)
    add_window.resizable(False,False)
    
    # Configurar inputs
    
    # TITLE INPUT
    title = ctk.CTkEntry(add_window, placeholder_text="Title. Max 40 Caracteres", font=font_text,height=50,width=350, fg_color="#1F1F1F",border_width=0)
    title.grid(row=0, column=0,pady=(20, 20))
    
    # DESCRIPTION INPUT
    description = ctk.CTkTextbox(add_window, height=150, font=font_text,wrap="word")
    description.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
    
    # DATE INPUT
    container_date = ctk.CTkFrame(add_window,fg_color="transparent")
    container_date.grid(row=2, column=0, pady=(20, 20))
    text_date = ctk.CTkLabel(container_date, text="Selecciona una fecha:", font=font_text)
    text_date.grid(row=2, column=0)
    cal = DateEntry(container_date, width=12, foreground='white', borderwidth=2, locale='es_ES')
    cal.grid(row=2, column=1, padx=20)

    # PRIORITY INPUT
    container_priority = ctk.CTkFrame(add_window,fg_color="transparent")
    container_priority.grid(row=3, column=0, pady=(0, 20))
    text_priority = ctk.CTkLabel(container_priority, text="Selecciona la prioridad:", font=font_text)
    text_priority.grid(row=3, column=0)
    priority = ctk.CTkSegmentedButton(container_priority, values=["HIGH", "MEDIUM", "LOW"])
    priority.set("MEDIUM")
    priority.grid(row=3, column=1, padx=20)

    # SEND BUTTON 
    button_send_task = ctk.CTkButton(
        add_window, text="Confirm", 
        font=font_text,height=50,width=300, cursor="hand2", 
        command=lambda:mod.save_task(add_window,title,description,cal,priority,render_mainscreen))
    
    button_send_task.grid(row=4,column=0,pady=(30))

# -------------------------------------------------------EDIT TASK WINDOW--------------------------------------------------------

def edit_task(task):
    original_title = task["title"]
    edit_window = ctk.CTkToplevel()
    edit_window.title("Task")
    edit_window.geometry("500x600")
    edit_window.attributes("-topmost", True)
    edit_window.grid_columnconfigure(0, weight=1)
    edit_window.resizable(False, False)

    # --- TITLE SECTION ---
    label_title_head = ctk.CTkLabel(edit_window, text="Title:", font=font_text)
    label_title_head.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
    
    title = ctk.CTkEntry(edit_window, height=40, font=font_text,fg_color="#1F1F1F",border_width=0)
    title.insert(0, task["title"])
    title.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

    # --- DESCRIPTION SECTION ---
    label_desc_head = ctk.CTkLabel(edit_window, text="Description:", font=font_text)
    label_desc_head.grid(row=2, column=0, padx=20, pady=(15, 0), sticky="w")
    
    description = ctk.CTkTextbox(edit_window, height=150, font=font_text, wrap="word")
    description.insert("0.0", task["description"])
    description.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

    # --- DATE SECTION ---
    label_date_head = ctk.CTkLabel(edit_window, text="Date:", font=font_text)
    label_date_head.grid(row=4, column=0, padx=20, pady=(15, 0), sticky="w")
    
    container_date = ctk.CTkFrame(edit_window, fg_color="transparent")
    container_date.grid(row=5, column=0, padx=20, pady=5, sticky="ew")
    
    cal = DateEntry(container_date, width=12, foreground='white', borderwidth=2, locale='en_US')
    cal.set_date(task["date"]) 
    cal.grid(row=0, column=0, padx=5, sticky="w")

    # --- PRIORITY SECTION ---
    label_priority_head = ctk.CTkLabel(edit_window, text="Priority:", font=font_text)
    label_priority_head.grid(row=6, column=0, padx=20, pady=(15, 0), sticky="w")
    
    priority = ctk.CTkSegmentedButton(edit_window, values=["HIGH", "MEDIUM", "LOW"], font=font_text)
    priority.set(task["priority"])
    priority.grid(row=7, column=0, padx=20, pady=5, sticky="w")

    # --- SAVE EDITS BUTTON ---
    btn_save = ctk.CTkButton(
        edit_window, 
        text="Save Changes", 
        height=50,
        font=font_text,
        command=(lambda:mod.edit_task(edit_window,title,description,cal,priority,render_mainscreen,original_title)))
    btn_save.grid(row=8, column=0, padx=20, pady=30, sticky="ew")
    
    
    # ADD HOVER REACTION TO AN OBJECT.
def on_hover(event,color,item):
    item.configure(fg_color=color)
def on_leave(event,color:str,item):
    item.configure(fg_color=color)
    

    # MAIN SCREEN FUNCTION
def render_mainscreen():
    
    for widget in app.winfo_children():
        widget.destroy()
        
    valid_json = mod.load_tasks()
    if valid_json == False:             #IF Json dont exists OR json has not data, display a default start window with only "Create task" option
        app.grid_columnconfigure(0, weight=1)
        app.grid_rowconfigure(0, weight=1)
        app.grid_rowconfigure(1, weight=1)
        
        label_logo = ctk.CTkLabel(app,text="Task Manager",font=font_title)
        label_logo.grid(row=0,column=0)
        button_add_task = ctk.CTkButton(app, text="Add Task",font=font_text,height=50,width=350, command=add_task, cursor="hand2")
        button_add_task.grid(row=1, column=0,sticky="n")
    
    # -------------------------------------DISPLAY WHEN THERE ARE TASKS TO DO--------------------------------------------------
    else:
        for widget in app.winfo_children():
            widget.destroy()
        app.grid_columnconfigure(0, weight=1)
        app.grid_rowconfigure(0, weight=1)

        scroll_frame = ctk.CTkScrollableFrame(app, label_text="TASK MANAGER", width=720,height=600)
        scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        scroll_frame.grid_columnconfigure(0,weight=1)
        scroll_frame.grid_rowconfigure(0,weight=1)

        options_container = ctk.CTkFrame(scroll_frame,fg_color="transparent",height=20)
        options_container.grid(row=0,sticky="ew",padx=15,pady=[0,15])
        
        button_add_task = ctk.CTkButton(options_container, text="Add Task",font=font_text,height=30,width=30, command=add_task, cursor="hand2")
        button_add_task.grid(row=0, column=0,padx=10,pady=10)
        
        for i, task in enumerate(valid_json,start=1):
            
            task_container = ctk.CTkFrame(scroll_frame,fg_color="#3B3B3B")
            task_container.grid(row=i, column=0,pady=[0,5],padx=10,sticky="ew")
            task_container.grid_columnconfigure(1,weight=1)
            task_container.configure(cursor="hand2")
            
            label_title = ctk.CTkLabel(task_container, text=task["title"], font=(font_text,18))
            label_title.grid(row=i, column=0, padx=25,pady=5,sticky="w")
            label_extra = ctk.CTkLabel(task_container, font=font_text,text=f"Priority: {task["priority"]}  /  {task["date"]}")
            label_extra.grid(row=i, column=1,sticky="e",padx=[0,10])
            
            # CLICK EVENT FUNCTION. 
            def click_event(widget, data=task): # "data" keeps the value of each iteration of task
                widget.bind("<Button-1>",lambda e: edit_task(data))
                
            click_event(task_container)
            click_event(label_title)
            click_event(label_extra)
            
            
            # HOVER EVENT TO CONTAINER
            task_container.bind("<Enter>", lambda e,c=task_container: on_hover(e,"#525252", c))
            task_container.bind("<Leave>", lambda e,c=task_container: on_leave(e,"#3B3B3B", c))
            
            # HOVER EVENT TO TITLE LABEL
            label_title.bind("<Enter>", lambda e,c=task_container: on_hover(e,"#525252", c))
            label_title.bind("<Leave>", lambda e,c=task_container: on_leave(e,"#3B3B3B", c))
            
            # HOVER EVENT TO DATE LABEL
            label_extra.bind("<Enter>", lambda e,c=task_container: on_hover(e,"#525252", c))
            label_extra.bind("<Leave>", lambda e,c=task_container: on_leave(e,"#3B3B3B", c))




if __name__ == "__main__": 
    render_mainscreen()
    app.mainloop()