import tkinter as tk
from tkinter import ttk
from conexion_sqlserver import conectar

def cargar_datos():
    tree.delete(*tree.get_children())

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id_producto, p.nombre, p.precio, i.tienda, i.cantidad_disponible
        FROM Productos p
        JOIN Inventario i ON p.id_producto = i.id_producto
    """)
    resultados = cursor.fetchall()
    for fila in resultados:
        tree.insert('', 'end', values=fila)
    
    conn.close()

ventana = tk.Tk()
ventana.title("📊 Panel de Consulta - TechStore")

tk.Label(ventana, text="Inventario y Productos Actualizados", font=("Arial", 14)).pack(pady=10)

cols = ('ID Producto', 'Nombre', 'Precio', 'Tienda', 'Stock')
tree = ttk.Treeview(ventana, columns=cols, show='headings')

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(pady=10)
tk.Button(ventana, text="🔄 Refrescar Datos", command=cargar_datos).pack(pady=5)

cargar_datos()
ventana.mainloop()
