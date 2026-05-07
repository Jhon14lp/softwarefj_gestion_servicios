import tkinter as tk
from tkinter import messagebox, ttk
#modls
from sistema import SistemaGestion
from cliente import Cliente
from reserva import ReservaSala
from servicios import AlquilerEquipo, AsesoriaEspecializada

class AppSoftwareFJ:
    def __init__(self, root):
        self.sistema = SistemaGestion()
        self.root = root
        self.root.title("Software FJ - Gestión")
        self.root.geometry("450x550")
        self.root.configure(padx=20, pady=20)

        # --- SECCIÓN CLIENTE ---
        tk.Label(root, text="REGISTRO DE CLIENTE", font=('Arial', 12, 'bold')).grid(row=0, columnspan=2, pady=10)
        
        tk.Label(root, text="ID:").grid(row=1, column=0, sticky="w")
        self.ent_id = tk.Entry(root)
        self.ent_id.grid(row=1, column=1, pady=5)

        tk.Label(root, text="Nombre:").grid(row=2, column=0, sticky="w")
        self.ent_nombre = tk.Entry(root)
        self.ent_nombre.grid(row=2, column=1, pady=5)

        tk.Label(root, text="Email:").grid(row=3, column=0, sticky="w")
        self.ent_email = tk.Entry(root)
        self.ent_email.grid(row=3, column=1, pady=5)

        tk.Button(root, text="Registrar Cliente", command=self.reg_cliente, bg="#4CAF50", fg="white").grid(row=4, columnspan=2, pady=10)

        # Separador visual
        ttk.Separator(root, orient='horizontal').grid(row=5, columnspan=2, sticky="ew", pady=15)

        # --- SECCIÓN SERVICIOS ---
        tk.Label(root, text="NUEVO SERVICIO", font=('Arial', 12, 'bold')).grid(row=6, columnspan=2, pady=10)

        tk.Label(root, text="Tipo:").grid(row=7, column=0, sticky="w")
        self.combo = ttk.Combobox(root, values=["Reserva Sala", "Alquiler Equipo", "Asesoría"], state="readonly")
        self.combo.grid(row=7, column=1, pady=5)

        tk.Label(root, text="Cant. (Horas/Días):").grid(row=8, column=0, sticky="w")
        self.ent_cant = tk.Entry(root)
        self.ent_cant.grid(row=8, column=1, pady=5)

        tk.Label(root, text="Tarifa ($):").grid(row=9, column=0, sticky="w")
        self.ent_tarifa = tk.Entry(root)
        self.ent_tarifa.grid(row=9, column=1, pady=5)

        tk.Button(root, text="Procesar y Calcular", command=self.proc_servicio, bg="#2196F3", fg="white").grid(row=10, columnspan=2, pady=20)

    def reg_cliente(self):
        try:
            c = Cliente(int(self.ent_id.get()), self.ent_nombre.get(), self.ent_email.get())
            self.sistema.registrar_cliente(c)
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def proc_servicio(self):
        try:
            tipo = self.combo.get()
            cant = float(self.ent_cant.get())
            tari = float(self.ent_tarifa.get())

            if tipo == "Reserva Sala":
                obj = ReservaSala(int(cant), tari)
            elif tipo == "Alquiler Equipo":
                obj = AlquilerEquipo(int(cant), tari)
            elif tipo == "Asesoría":
                obj = AsesoriaEspecializada(int(cant), tari)
            else:
                return messagebox.showwarning("Atención", "Elija un servicio")

            costo = self.sistema.procesar_servicio(obj)
            messagebox.showinfo("Costo Total", f"El total es: ${costo:,.2f}\nDetalle: {obj.detallar()}")
        except Exception as e:
            messagebox.showerror("Error", f"Verifique los datos: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    AppSoftwareFJ(root)
    root.mainloop()