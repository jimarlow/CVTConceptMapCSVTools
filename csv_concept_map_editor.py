import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os

from csv_concept_map import ConceptMap

class CSVConceptMapEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Text Editor")
        self.geometry("800x600")
        self.filename = None

        # --- Text widget for editing ---
        self.text = tk.Text(self, wrap='none', font=('Courier', 12), undo=True)
        self.text.pack(fill='both', expand=True, padx=10, pady=10)

        # --- Context menu for Cut/Copy/Paste ---
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Cut", command=self.cut)
        self.context_menu.add_command(label="Copy", command=self.copy)
        self.context_menu.add_command(label="Paste", command=self.paste)

        # Bind right-click to show context menu
        self.text.bind("<Button-3>", self.show_context_menu)

        # --- Button frame ---
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill='x', padx=10, pady=5)

        self.open_btn = tk.Button(btn_frame, text="Open CSV", command=self.open_file)
        self.open_btn.pack(side='left', padx=5)

        self.save_btn = tk.Button(btn_frame, text="Save CSV", command=self.save_file)
        self.save_btn.pack(side='left', padx=5)

        self.cm_btn = tk.Button(btn_frame, text="Concept map png", command=self.render_concept_map_png)
        self.cm_btn.pack(side='left', padx=5)

        self.cm_btn = tk.Button(btn_frame, text="Concept map svg", command=self.render_concept_map_svg)
        self.cm_btn.pack(side='left', padx=5)

        self.cm_btn = tk.Button(btn_frame, text="Concept map pdf", command=self.render_concept_map_pdf)
        self.cm_btn.pack(side='left', padx=5)

        # Keyboard bindings for cut/copy/paste
        self.text.bind('<Control-x>', self.cut)
        self.text.bind('<Control-c>', self.copy)
        self.text.bind('<Control-v>', self.paste)

        # --- Do NOT open file at startup ---
        # self.open_file()  # <-- This line is removed

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )
        if not file_path:
            return
        self.filename = file_path
        self.load_csv_to_text()

    def load_csv_to_text(self):
        self.text.delete('1.0', tk.END)
        with open(self.filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                line = ','.join([f'"{item}"' if ',' in item or '"' in item else item for item in row])
                self.text.insert(tk.END, line + '\n')

    def save_file(self):
        if not self.filename:
            file_path = filedialog.asksaveasfilename(
                title="Save CSV File As",
                defaultextension=".csv",
                filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
            )
            if not file_path:
                return  # User cancelled save dialog
            self.filename = file_path

        content = self.text.get('1.0', tk.END).strip()
        lines = content.split('\n')
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                for line in lines:
                    for row in csv.reader([line]):
                        writer.writerow(row)
            #messagebox.showinfo("Saved", f"File saved: {os.path.basename(self.filename)}")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))

    def render_concept_map(self, format='png'):
        if self.filename:
            print(f"Current file: {self.filename}")
            cg = ConceptMap(os.path.splitext(self.filename)[0])
            cg.from_file(self.filename)
            cg.render(engine='dot', format=format)
        else:
            print("No file loaded.")

    def render_concept_map_png(self):
        self.save_file()
        self.render_concept_map('png')

    def render_concept_map_svg(self):
        self.save_file()
        self.render_concept_map('svg')

    def render_concept_map_pdf(self):
        self.save_file()
        self.render_concept_map('pdf')

    # --- Edit menu/context menu actions ---
    def cut(self, event=None):
        self.text.event_generate('<<Cut>>')
        return "break"

    def copy(self, event=None):
        self.text.event_generate('<<Copy>>')
        return "break"

    def paste(self, event=None):
        self.text.event_generate('<<Paste>>')
        return "break"

    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

if __name__ == "__main__":
    app = CSVConceptMapEditor()
    app.mainloop()
