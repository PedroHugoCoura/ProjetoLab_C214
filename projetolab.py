import tkinter as tk
from tkinter import ttk, messagebox

class IMCCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        self.history = []

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 14))
        style.configure("TButton", font=("Helvetica", 12), padding=8)
        style.configure("Title.TLabel", font=("Helvetica", 20, "bold"), anchor="center")

        ttk.Label(self.root, text="Calculadora de IMC", style="Title.TLabel").pack(pady=20)
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill="x", pady=20)

        ttk.Label(input_frame, text="Altura (cm):").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.height_entry = ttk.Entry(input_frame, font=("Helvetica", 14))
        self.height_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        ttk.Label(input_frame, text="Peso (kg):").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.weight_entry = ttk.Entry(input_frame, font=("Helvetica", 14))
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        input_frame.columnconfigure(1, weight=1)

        calculate_button = ttk.Button(main_frame, text="Calcular IMC", command=self.calculate_bmi)
        calculate_button.pack(pady=20, ipadx=20)

        self.result_label = ttk.Label(main_frame, text="", font=("Helvetica", 16, "bold"), foreground="#007BFF")
        self.result_label.pack(pady=10)

        ttk.Label(main_frame, text="Histórico de Cálculos", style="Title.TLabel").pack(pady=20)

        history_frame = ttk.Frame(main_frame, borderwidth=2, relief="groove", padding=10)
        history_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.history_listbox = tk.Listbox(history_frame, font=("Helvetica", 12), height=10)
        self.history_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.history_listbox.config(yscrollcommand=scrollbar.set)

    def calculate_bmi(self):
        try:

            height = float(self.height_entry.get()) / 100

            weight = float(self.weight_entry.get())

            bmi = weight / (height ** 2)
            category = self.determine_category(bmi)

            result_text = f"IMC: {bmi:.2f} - Categoria: {category}"
            self.result_label.config(text=result_text)

            self.history.append(result_text)
            self.update_history()

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def determine_category(self, bmi):
        if bmi < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            return "Peso normal"
        elif 25 <= bmi < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"

    def update_history(self):
        self.history_listbox.delete(0, tk.END)
        for record in self.history:
            self.history_listbox.insert(tk.END, record)

if __name__ == "__main__":
    root = tk.Tk()
    app = IMCCalculator(root)
    root.mainloop()
