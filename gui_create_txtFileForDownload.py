import os
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import downloadfile

def get_stt():
    """Read and return the current STT value."""
    try:
        with open(r'C:\Users\Admin\Downloads\stt.txt') as f:
            return f.read().strip()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read stt.txt: {e}")
        return None

def save_data():
    """Save data to a file and process it."""
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "No input provided!")
        return

    lines = input_text.splitlines()
    animated = any(".mp4" in line for line in lines)
    stt = get_stt()
    if not stt:
        return

    # Determine file name and path
    file_name = rf"C:\Users\Admin\Downloads\d1 resource\{stt}a.txt" if animated else rf"C:\Users\Admin\Downloads\d1 resource\{stt}.txt"

    # Save data to file
    try:
        with open(file_name, "w") as file:
            file.writelines([line + "\n" for line in lines])

        # Update stt.txt if not animated
        if not animated:
            with open(r'C:\Users\Admin\Downloads\stt.txt', 'w') as writef:
                writef.write(str(int(stt) + 1))

        messagebox.showinfo("Success", f"Data saved to {file_name}")
        downloadfile.process_file(stt, os.path.join(downloadfile.base_input_dir, file_name), animated)
        root.destroy()  # Close the application after saving
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

def paste_from_clipboard():
    """Paste clipboard content into the input area."""
    try:
        clipboard_data = root.clipboard_get()
        text_input.insert(tk.END, clipboard_data)
    except tk.TclError:
        messagebox.showwarning("Warning", "No data in clipboard to paste!")

# Create GUI
root = tk.Tk()
root.title("Data Entry Tool")
root.geometry("600x400")

# Input area
tk.Label(root, text="Paste data (Press 'Paste' to insert clipboard content):").pack(anchor="w", padx=10, pady=5)
text_input = ScrolledText(root, wrap=tk.WORD, height=15, width=70)
text_input.pack(padx=10, pady=5)

# Buttons
tk.Button(root, text="Paste from Clipboard", command=paste_from_clipboard, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Finish", command=save_data, bg="green", fg="white").pack(pady=10)

root.mainloop()
