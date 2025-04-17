import tkinter as tk
from tkinter import messagebox
from conexion_sqlserver import conectar

def asignar_stock():
    id_prod = entry_id.get()
    tienda = entry_tienda.get()
    stock = entry_stock.get()

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Inventario (id_producto, tienda, cantidad_disponible, estado_stock)
            VALUES (?, ?, ?, 'Disponible')""", (id_prod, tienda, stock))
        conn.commit()
        messagebox.showinfo("Asignado", "Stock asignado a tienda.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

ventana = tk.Tk()
ventana.title("Gestión de Inventario por Tienda")

tk.Label(ventana, text="ID Producto").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Tienda").pack()
entry_tienda = tk.Entry(ventana)
entry_tienda.pack()

tk.Label(ventana, text="Cantidad a asignar").pack()
entry_stock = tk.Entry(ventana)
entry_stock.pack()

tk.Button(ventana, text="📦 Asignar Stock", command=asignar_stock).pack(pady=10)

ventana.mainloop()
