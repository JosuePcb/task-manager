import json
import routes
import pyglet

# Global vars
DIR_JSON = routes.DIR_JSON
tasks_list = []

# Fonts 
pyglet.font.add_file(routes.ROBOTO_REGULAR)
pyglet.font.add_file(routes.ROBOTO_BOLD)

# Function to check if there are valid tasks or if the json exists / and return the tasklist if it has
def load_tasks():    
    global tasks_list
    global DIR_JSON
    try:
        with open(DIR_JSON, 'r') as info:
            tasks_list = json.load(info)
            if tasks_list == []:
                return False                # Return false if the json exists but HAS NOT real data
            else:
                return tasks_list # Return the task list if the json exists AND HAS real data
    except FileNotFoundError:
        with open(DIR_JSON, 'w') as f:
            f.write("[]")
            return False # Return False if the json didnt exists

# GET TASKS FROM FRONTEND TO BACKEND AND VALIDATE IT

def get_task(title,description,cal,priority):   
    

    val_title = title.get().strip()
    val_description = description.get("1.0","end-1c").strip()
    if not val_description:
        val_description = "No Description"
    val_date = cal.get_date()
    str_date = cal.get_date().strftime("%d/%m/%Y")
    val_priority = priority.get().strip()
    
    # Validations
    flag = True
    if not val_title or len(val_title) > 40 or val_title.isdigit():
        title.configure(border_width=1,border_color="red")
        flag = False
    else:
        title.configure(border_color="gray")
        
    if len(val_description) > 250:
        description.configure(border_color="red",border_width=1)
        flag = False
    else:
        description.configure(border_color="gray")
    if flag == False:
        return
    
    new_task = {
        "title": val_title, 
        "description": val_description, 
        "priority": val_priority, 
        "date": str_date
    }
    
    return new_task

# EDIT TASKS ADDED
def edit_task(window,title,description,cal,priority,refresh,original_title):
    
    new_task = get_task(title,description,cal,priority)
    
    tasks_list = load_tasks()
    if tasks_list is None:
        return
    
    for i in range(len(tasks_list)):
        if tasks_list[i]["title"] == original_title:
            tasks_list[i] = new_task
            break
    
    with open(DIR_JSON, 'w') as task_file:
        json.dump(tasks_list, task_file, indent=4)
    
    window.destroy()
    refresh()
# Function to add tasks to the Json
def save_task(window,title,description,cal,priority,refresh):
    
    # Carga nueva task
    new_task = get_task(title, description, cal, priority)
    
    # Carga todas las tasks
    tasks_list = load_tasks()
    if tasks_list is False:
        tasks_list = []
    
    tasks_list.append(new_task)
    
    # Add information to .json
    with open(DIR_JSON, 'w') as task:
        json.dump(tasks_list, task, indent=4)
    window.destroy()
    refresh()