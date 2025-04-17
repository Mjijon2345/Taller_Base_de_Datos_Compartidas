import tkinter as tk
from tkinter import messagebox
from conexion_sqlserver import conectar

def agregar_producto():
    id_prod = entry_id.get()
    nombre = entry_nombre.get()
    desc = entry_desc.get()
    precio = entry_precio.get()

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO Productos (id_producto, nombre, descripcion, precio)
            VALUES (?, ?, ?, ?)""", (id_prod, nombre, desc, precio))
        conn.commit()
        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

def actualizar_precio():
    id_prod = entry_id.get()
    precio = entry_precio.get()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Productos SET precio = ? WHERE id_producto = ?", (precio, id_prod))
    conn.commit()
    conn.close()

    messagebox.showinfo("Actualizado", "Precio actualizado correctamente.")

ventana = tk.Tk()
ventana.title("Gestión de Productos")

tk.Label(ventana, text="ID Producto").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Descripción").pack()
entry_desc = tk.Entry(ventana)
entry_desc.pack()

tk.Label(ventana, text="Precio").pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()

tk.Button(ventana, text="➕ Agregar Producto", command=agregar_producto).pack(pady=5)
tk.Button(ventana, text="💲 Actualizar Precio", command=actualizar_precio).pack(pady=5)

ventana.mainloop()
