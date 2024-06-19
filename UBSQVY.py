import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

with open('data.txt', 'r') as file:
    data = json.load(file)

def modify():
    try:
        id_to_modify = input_box3.get()

        newcon_id = input_box2.get()
        newcon_result = input_box22.get()
        # Find the dictionary with the specified ID
        for person in data:
            if person['identifier'] == id_to_modify:
                old_id = person['confirmed_id']
                person['confirmed_id'] = newcon_id

                old_results = person['confirmed_results']
                person['confirmed_results'] = newcon_result

                messagebox.showinfo("Changed Successfully",
                                    f"Data modified successfully!\nPrevious Confirmed ID was {old_id}, now is is {newcon_id}.\nPrevious Confirmed Results was {old_results}, and the New Confirmed Results is {newcon_result}")
                break
        else:
            messagebox.showerror("Error", "No such ID")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid ID")


def search():
    identifier = input_box3.get()

    def ind(data, identifier):
        for index, d in enumerate(data):
            if d["identifier"] == identifier:
                return index

    i = ind(data, identifier)

    try:
        input_box2.delete(0, tk.END)
        input_box2.insert(tk.END, data[i]["confirmed_id"])
        dv.set(f"{data[i]['identifier']}")
        dv2.set(f"{data[i]['results']}")
        label221entry.delete(0, tk.END)
        input_box22.delete(0, tk.END)
        input_box22.insert(tk.END, data[i]['confirmed_results'])

        images = Image.open(f"{data[i]['id_image']}")
        images = images.resize((150, 100), Image.ANTIALIAS)
        images = ImageTk.PhotoImage(images)
        image_box1.config(image=images)
        image_box1.image = images

        image = Image.open(f"{data[i]['result_image']}")
        image = image.resize((300, 100), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        image_box2.config(image=image)
        image_box2.image = image

    except TypeError:
        dv.set("")
        dv2.set("")
        image_box1.image = ""
        image_box2.image = ""
        input_box2.delete(0, tk.END)
        input_box3.delete(0, 'end')
        input_box22.delete(0, tk.END)
        messagebox.showerror("Error", "User does not Exist")


def next_btn():
    try:
        identifier = input_box3.get()

        def ind(data, identifier):
            for index, d in enumerate(data):
                if d["identifier"] == identifier:
                    return index

        current_index = 0
        if not identifier:
            current_index = 0
        else:
            current_index = ind(data, identifier)
            current_index = current_index + 1

        # If the current index exceeds the length of the data, reset to 0
        if current_index >= len(data):
            current_index = 0

        # Update the ID entry with the next ID
        input_box2.delete(0, tk.END)
        input_box2.insert(tk.END, data[current_index]["confirmed_id"])
        input_box3.delete(0, 'end')
        input_box3.insert(0, str(data[current_index]["identifier"]))
        dv.set(f"{data[current_index]['identifier']}")
        dv2.set(f"{data[current_index]['results']}")
        input_box22.delete(0, tk.END)
        input_box22.insert(tk.END, data[current_index]['confirmed_results'])

        images = Image.open(f"{data[current_index]['id_image']}")
        images = images.resize((150, 100), Image.ANTIALIAS)
        images = ImageTk.PhotoImage(images)
        image_box1.config(image=images)
        image_box1.image = images

        image = Image.open(f"{data[current_index]['result_image']}")
        image = image.resize((300, 100), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        image_box2.config(image=image)
        image_box2.image = image
    except TypeError:
        input_box2.delete(0, tk.END)
        input_box3.delete(0, 'end')
        input_box22.delete(0, tk.END)
        messagebox.showerror("Error", "Please enter a valid ID")


def prev_btn():
    try:
        identifier = input_box3.get()

        def ind(data, identifier):
            for index, d in enumerate(data):
                if d["identifier"] == identifier:
                    return index

        current_index = 0
        if not identifier:
            current_index = -1
        else:
            current_index = ind(data, identifier)
            current_index = current_index - 1

        # If the current index exceeds the length of the data, reset to 0
        if current_index >= len(data):
            current_index = 0

        # Update the ID entry with the next ID
        input_box2.delete(0, tk.END)
        input_box2.insert(tk.END, data[current_index]["confirmed_id"])
        input_box3.delete(0, 'end')
        input_box3.insert(0, str(data[current_index]["identifier"]))
        dv.set(f"{data[current_index]['identifier']}")
        dv2.set(f"{data[current_index]['results']}")
        input_box22.delete(0, tk.END)
        input_box22.insert(tk.END, data[current_index]['confirmed_results'])

        images = Image.open(f"{data[current_index]['id_image']}")
        images = images.resize((150, 100), Image.ANTIALIAS)
        images = ImageTk.PhotoImage(images)
        image_box1.config(image=images)
        image_box1.image = images

        image = Image.open(f"{data[current_index]['result_image']}")
        image = image.resize((300, 100), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        image_box2.config(image=image)
        image_box2.image = image
    except TypeError:
        input_box2.delete(0, tk.END)
        input_box3.delete(0, 'end')
        input_box22.delete(0, tk.END)
        messagebox.showerror("Error", "Please enter a valid ID")


root = tk.Tk()
root.title("My GUI")
root.geometry("950x700")

# # Create a blue line as a border for the whole UI
border_frame = tk.Frame(root, borderwidth=0.01, relief="solid")
border_frame.pack(expand=True, padx=10, pady=10)

# # First Layer
first_layer = tk.Frame(border_frame)
first_layer.pack(fill=tk.BOTH, padx=10, pady=10)

# # # First Layer2
first_layer2 = tk.Frame(border_frame)
first_layer2.pack(fill=tk.BOTH, padx=10, pady=10)

# # Label and Input Box on the left
dv = tk.StringVar()
dv.set("")
label21entry = tk.Entry(first_layer, state="readonly", textvariable=dv)
label21 = tk.Label(first_layer, text="Identifier :  ")
label2 = tk.Label(first_layer2, text="Confirmed Identifier :  ")
label2.pack(side=tk.LEFT, padx=5, pady=5)
input_box2 = tk.Entry(first_layer2, width=30)
input_box2.pack(side=tk.LEFT, padx=10, pady=10)
label21.pack(side=tk.LEFT, padx=0, pady=10)
label21entry.pack(side=tk.LEFT, padx=0, pady=10)

# # Image Box on the right
image_box1 = tk.Label(first_layer)
image_box1.pack(side=tk.RIGHT, padx=10, pady=10)

# # Second Layer
second_layer = tk.Frame(border_frame)
second_layer.pack(fill=tk.BOTH, padx=10, pady=10)

# Label and Input Box
dv2 = tk.StringVar()
dv2.set("")
input_box22 = tk.Entry(second_layer, width=30)
input_box22.pack(side=tk.BOTTOM, padx=5, pady=5)
label221entry = tk.Entry(second_layer, state="readonly", textvariable=dv2)
label221 = tk.Label(second_layer, text=f"Results : ")
label221.pack(side=tk.TOP, padx=10, pady=10)
label22 = tk.Label(second_layer, text="Confirmed Results :   ")
label22.pack(side=tk.BOTTOM, padx=5, pady=5)
label221entry.pack(side=tk.TOP, padx=10, pady=10)

# # Third Layer
third_layer = tk.Frame(border_frame)
third_layer.pack(fill=tk.BOTH, padx=10, pady=10)

# # Image Box
image_box2 = tk.Label(third_layer)
image_box2.pack(padx=10, pady=10)

# # Bottom Layer2
bottom_layer2 = tk.Frame(border_frame)
bottom_layer2.pack(fill=tk.X, padx=10, pady=(0, 10))

button3 = tk.Button(bottom_layer2, text="Search", width=15, command=search)
button3.pack(side=tk.RIGHT, padx=10, pady=10)
input_box3 = tk.Entry(bottom_layer2, width=30)
input_box3.pack(side=tk.RIGHT, padx=5, pady=5)
label2 = tk.Label(bottom_layer2, text="Identifier \n to find :  ")
label2.pack(side=tk.RIGHT, padx=5, pady=5)

# # Bottom Layer
bottom_layer = tk.Frame(border_frame, bg="white")
bottom_layer.pack(fill=tk.X, padx=10, pady=(0, 10))

# # Buttons
button1 = tk.Button(bottom_layer, text="Show Previous", width=15, command=prev_btn)
button1.pack(side=tk.LEFT, padx=10, pady=10)
button2 = tk.Button(bottom_layer, text="Show Next", width=15, command=next_btn)
button2.pack(side=tk.LEFT, padx=10, pady=10)
button2 = tk.Button(bottom_layer, text="Modify", width=15, command=modify)
button2.pack(side=tk.LEFT, padx=10, pady=10)

# # # Start the GUI main loop
root.mainloop()

with open('data.txt', 'w') as file:
    json.dump(data, file)