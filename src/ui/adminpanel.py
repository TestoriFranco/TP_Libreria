import tkinter as tk
from src.ui.styles import apply_styles, RoundedButton


class AdminFrame(tk.Frame):
    def __init__(self, parent, show_frame, role_id):
        super().__init__(parent)
        self.show_frame = show_frame
        self.role_id = role_id
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        if self.role_id == 1:
            RoundedButton(self, text="Administrar Libros", command=self.show_abm_libros_frame, width=180, height=60, bg='white', fg='#013220').pack(pady=10)
            RoundedButton(self, text="Administrar Usuarios", command=self.show_abm_usuarios_frame, width=180, height=60, bg='white', fg='#013220').pack(pady=10)
        elif self.role_id == 2:
            RoundedButton(self, text="Administrar Libros", command=self.show_abm_libros_frame, width=180, height=60, bg='white', fg='#013220').pack(pady=10)

        RoundedButton(self, text="Ver Tienda", command=self.show_productos_frame, width=180, height=60, bg='white', fg='#013220').pack(pady=10)
        RoundedButton(self, text="Ver Pedidos", command=self.show_pedidos_frame, width=180, height=60, bg='white', fg='#013220').pack(pady=10)

    def show_productos_frame(self):
        productos_frame = self.master.children.get("!productosframe")
        if productos_frame:
            productos_frame.tkraise()
        else:
            print("¡Error! El frame '!productosframe' no está disponible.")

    def show_pedidos_frame(self):
        pedidos_frame = self.master.children.get("!pedidosframe")
        if pedidos_frame:
            pedidos_frame.tkraise()
        else:
            print("¡Error! El frame '!pedidosframe' no está disponible.")

    def show_abm_libros_frame(self):
        abm_libros_frame = self.master.children.get("!abmlibrosframe")
        if abm_libros_frame:
            abm_libros_frame.tkraise()
        else:
            print("¡Error! El frame '!abmlibrosframe' no está disponible.")

    def show_abm_usuarios_frame(self):
        abm_usuarios_frame = self.master.children.get("!abmusuariosframe")
        if abm_usuarios_frame:
            abm_usuarios_frame.tkraise()
        else:
            print("¡Error! El frame '!abmusuariosframe' no está disponible.")
