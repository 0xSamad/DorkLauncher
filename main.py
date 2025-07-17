import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import time
import threading

class DorkLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("DuckDuckGo Dork Launcher")
        self.root.geometry("580x330")
        self.root.configure(bg="#eaeff2")  # soft light gray background

        self.dorks = []
        self.dorks_file = ""
        self.batch_size = 10
        self.current_index = 0

        # Fonts and Colors
        self.font_title = ("Segoe UI", 14, "bold")
        self.font_regular = ("Segoe UI", 11)
        self.color_primary = "#005bbb"     # Professional blue
        self.color_secondary = "#ffffff"   # White
        self.input_bg = "#ffffff"
        self.input_fg = "#000000"
        self.label_fg = "#333333"

        # --- GUI Components ---
        tk.Label(root, text="DuckDuckGo Dork Launcher", font=self.font_title,
                 bg="#eaeff2", fg=self.color_primary).pack(pady=12)

        frm_target = tk.Frame(root, bg="#eaeff2")
        frm_target.pack(pady=5)
        tk.Label(frm_target, text="Target domain:", font=self.font_regular,
                 bg="#eaeff2", fg=self.label_fg).pack(side=tk.LEFT, padx=5)
        self.domain_entry = tk.Entry(frm_target, width=40, font=self.font_regular,
                                     bg=self.input_bg, fg=self.input_fg, relief=tk.RIDGE, bd=2)
        self.domain_entry.pack(side=tk.LEFT)

        frm_buttons = tk.Frame(root, bg="#eaeff2")
        frm_buttons.pack(pady=15)

        self.load_button = tk.Button(frm_buttons, text="📂 Load Dorks File", command=self.load_dorks_file,
                                     font=self.font_regular, bg=self.color_primary, fg=self.color_secondary,
                                     activebackground="#004699", activeforeground=self.color_secondary,
                                     width=18, relief=tk.FLAT)
        self.load_button.grid(row=0, column=0, padx=10)

        self.start_button = tk.Button(frm_buttons, text="🚀 Start Dorking", command=self.start_dorking,
                                      font=self.font_regular, bg=self.color_primary, fg=self.color_secondary,
                                      activebackground="#004699", activeforeground=self.color_secondary,
                                      width=18, relief=tk.FLAT)
        self.start_button.grid(row=0, column=1, padx=10)

        self.next_button = tk.Button(root, text="➡️ Next Batch", command=self.next_batch,
                                     font=self.font_regular, bg="#bbbbbb", fg="#444444",
                                     activebackground="#999999", activeforeground="#ffffff",
                                     width=20, relief=tk.FLAT, state=tk.DISABLED)
        self.next_button.pack(pady=5)

        self.status = tk.Label(root, text="", font=self.font_regular, bg="#eaeff2", fg="#444444")
        self.status.pack(pady=8)

    def load_dorks_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.dorks_file = file_path
            with open(file_path, 'r') as f:
                self.dorks = [line.strip() for line in f if line.strip()]
            messagebox.showinfo("Dorks Loaded", f"{len(self.dorks)} dorks loaded.")
            self.status.config(text=f"{len(self.dorks)} dorks ready.")

    def start_dorking(self):
        self.target = self.domain_entry.get().strip()
        if not self.target:
            messagebox.showerror("Missing Input", "Please enter a target domain.")
            return
        if not self.dorks:
            messagebox.showerror("Missing Dorks", "Please load a dorks file first.")
            return

        self.current_index = 0
        self.start_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL, bg=self.color_primary, fg=self.color_secondary)
        self.status.config(text="Opening first batch...")
        threading.Thread(target=self.open_batch).start()

    def next_batch(self):
        self.current_index += self.batch_size
        if self.current_index >= len(self.dorks):
            messagebox.showinfo("Finished", "All dorks have been processed.")
            self.next_button.config(state=tk.DISABLED, bg="#bbbbbb", fg="#444444")
            self.start_button.config(state=tk.NORMAL)
            self.status.config(text="All dorks processed.")
        else:
            self.status.config(text=f"Opening batch {self.current_index // self.batch_size + 1}...")
            threading.Thread(target=self.open_batch).start()

    def open_batch(self):
        batch = self.dorks[self.current_index:self.current_index + self.batch_size]
        for dork in batch:
            query = f"site:{self.target} {dork}".replace(" ", "+")
            url = f"https://duckduckgo.com/?q={query}"
            webbrowser.open_new_tab(url)
            time.sleep(0.4)
        self.status.config(text=f"Batch {self.current_index // self.batch_size + 1} opened. Close tabs, then click 'Next Batch'.")

# Run
if __name__ == "__main__":
    root = tk.Tk()
    app = DorkLauncher(root)
    root.mainloop()
