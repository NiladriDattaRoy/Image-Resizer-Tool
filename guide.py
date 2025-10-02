import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox
from PIL import Image

# Function to browse input folder
def browse_input():
    folder_selected = filedialog.askdirectory()
    input_folder_var.set(folder_selected)

# Function to browse output folder
def browse_output():
    folder_selected = filedialog.askdirectory()
    output_folder_var.set(folder_selected)

# Function to resize images
def resize_images():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    try:
        width = int(width_var.get())
        height = int(height_var.get())
        new_format = format_var.get().upper()
    except ValueError:
        messagebox.showerror("Error", "Width and Height must be integers!")
        return

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders!")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    count = 0
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        try:
            with Image.open(file_path) as img:
                img_resized = img.resize((width, height))
                base_name = os.path.splitext(filename)[0]
                new_file_path = os.path.join(output_folder, f"{base_name}.{new_format.lower()}")
                img_resized.save(new_file_path)
                count += 1
        except Exception as e:
            print(f"Skipping {filename}: {e}")

    messagebox.showinfo("Done", f"Resized {count} images!")

# Create main window
root = Tk()
root.title("Batch Image Resizer")

# Variables
input_folder_var = StringVar()
output_folder_var = StringVar()
width_var = StringVar()
height_var = StringVar()
format_var = StringVar(value="PNG")

# UI Elements
Label(root, text="Input Folder:").grid(row=0, column=0, sticky="e")
Entry(root, textvariable=input_folder_var, width=40).grid(row=0, column=1)
Button(root, text="Browse", command=browse_input).grid(row=0, column=2)

Label(root, text="Output Folder:").grid(row=1, column=0, sticky="e")
Entry(root, textvariable=output_folder_var, width=40).grid(row=1, column=1)
Button(root, text="Browse", command=browse_output).grid(row=1, column=2)

Label(root, text="Width:").grid(row=2, column=0, sticky="e")
Entry(root, textvariable=width_var).grid(row=2, column=1, sticky="w")

Label(root, text="Height:").grid(row=3, column=0, sticky="e")
Entry(root, textvariable=height_var).grid(row=3, column=1, sticky="w")

Label(root, text="Format (PNG/JPG):").grid(row=4, column=0, sticky="e")
Entry(root, textvariable=format_var).grid(row=4, column=1, sticky="w")

Button(root, text="Resize Images", command=resize_images, bg="lightgreen").grid(row=5, column=1, pady=10)

root.mainloop()
