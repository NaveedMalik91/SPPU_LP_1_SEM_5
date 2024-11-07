import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, font

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_widget.delete("1.0", "end")  # Delete any content present before
            text_widget.insert("1.0", content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_widget.get("1.0", "end-1c")
            file.write(content)

def find_text():
    search_term = simpledialog.askstring("Find", "Enter text to find:")
    if search_term:
        start = text_widget.search(search_term, "1.0", "end")
        if start:
            end = f"{start}+{len(search_term)}c"  # Calculate the end position
            text_widget.tag_add("highlight", start, end)
            text_widget.see(start)  # Scroll to the found text
            text_widget.mark_set("insert", end)  # Set the cursor after the found text
            text_widget.focus()  # Focus on the text widget
        else:
            messagebox.showinfo("Find", "Text not found.")

def cut_text():
    text_widget.event_generate("<<Cut>>")

def copy_text():
    text_widget.event_generate("<<Copy>>")

def paste_text():
    text_widget.event_generate("<<Paste>>")

def clear_text():
    text_widget.delete("1.0", "end")

def change_font():
    font_name = simpledialog.askstring("Font Name", "Enter font name (e.g., Arial):")
    font_size = simpledialog.askinteger("Font Size", "Enter font size (e.g., 12):")
    if font_name and font_size:
        text_widget.config(font=(font_name, font_size))

def word_count():
    content = text_widget.get("1.0", "end-1c")
    word_count = len(content.split())
    messagebox.showinfo("Word Count", f"Word Count: {word_count}")

root = tk.Tk()
root.title("TEXT FILE EDITOR")

text_widget = tk.Text(root)
text_widget.pack(fill="both", expand=True)

toolbar = tk.Frame(root)
open_button = tk.Button(toolbar, text="Open", command=open_file)
save_button = tk.Button(toolbar, text="Save", command=save_file)
cut_button = tk.Button(toolbar, text="Cut", command=cut_text)
copy_button = tk.Button(toolbar, text="Copy", command=copy_text)
paste_button = tk.Button(toolbar, text="Paste", command=paste_text)
clear_button = tk.Button(toolbar, text="Clear", command=clear_text)
font_button = tk.Button(toolbar, text="Font", command=change_font)
word_count_button = tk.Button(toolbar, text="Word Count", command=word_count)

open_button.pack(side=tk.LEFT)
save_button.pack(side=tk.LEFT)
cut_button.pack(side=tk.LEFT)
copy_button.pack(side=tk.LEFT)
paste_button.pack(side=tk.LEFT)
clear_button.pack(side=tk.LEFT)
font_button.pack(side=tk.LEFT)
word_count_button.pack(side=tk.LEFT)

toolbar.pack(fill=tk.X)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
search_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Search", menu=search_menu)
search_menu.add_command(label="Find...", command=find_text)

text_widget.tag_configure("highlight", background="yellow")

root.mainloop()