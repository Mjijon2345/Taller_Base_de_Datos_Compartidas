CREATE DATABASE TechStore;
GO

USE TechStore;
GO

CREATE TABLE Productos (
    id_producto INT PRIMARY KEY,
    nombre NVARCHAR(100),
    descripcion NVARCHAR(MAX),
    precio DECIMAL(10, 2)
);

CREATE TABLE Inventario (
    id_inventario INT IDENTITY(1,1) PRIMARY KEY,
    id_producto INT,
    tienda NVARCHAR(100),
    cantidad_disponible INT,
    estado_stock NVARCHAR(50),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

CREATE TABLE Ventas (
    id_venta INT IDENTITY(1,1) PRIMARY KEY,
    id_producto INT,
    tienda NVARCHAR(100),
    cantidad_vendida INT,
    fecha_venta DATETIME,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

CREATE TABLE Auditoria (
    id_auditoria INT IDENTITY(1,1) PRIMARY KEY,
    tabla_afectada NVARCHAR(50),
    operacion NVARCHAR(10),
    id_referencia INT,
    fecha DATETIME DEFAULT GETDATE()
);

CREATE TRIGGER trg_UpdateProducto_Auditoria
ON Productos
AFTER UPDATE
AS
BEGIN
    INSERT INTO Auditoria (tabla_afectada, operacion, id_referencia)
    SELECT 'Productos', 'UPDATE', id_producto FROM inserted;
END;
GO

CREATE TRIGGER trg_InsertVenta_Auditoria
ON Ventas
AFTER INSERT
AS
BEGIN
    INSERT INTO Auditoria (tabla_afectada, operacion, id_referencia)
    SELECT 'Ventas', 'INSERT', id_producto FROM inserted;
END;
GO
