import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from conexion_sqlserver import conectar

def registrar_venta():
    id_prod = entry_id.get()
    tienda = entry_tienda.get()
    cantidad = int(entry_cantidad.get())

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Ventas (id_producto, tienda, cantidad_vendida, fecha_venta)
        VALUES (?, ?, ?, ?)""",
        (id_prod, tienda, cantidad, datetime.now()))
    
    cursor.execute("""
        UPDATE Inventario
        SET cantidad_disponible = cantidad_disponible - ?
        WHERE id_producto = ? AND tienda = ?""",
        (cantidad, id_prod, tienda))
    
    conn.commit()
    conn.close()

    messagebox.showinfo("Venta", "Venta registrada correctamente.")

ventana = tk.Tk()
ventana.title("POS - TechStore")

tk.Label(ventana, text="ID Producto").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Tienda").pack()
entry_tienda = tk.Entry(ventana)
entry_tienda.pack()

tk.Label(ventana, text="Cantidad").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

tk.Button(ventana, text="Registrar Venta", command=registrar_venta).pack()

ventana.mainloop()
