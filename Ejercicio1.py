class Producto:
    def __init__(self, nombre, precio_costo, cantidad):
        # Inicializa un nuevo producto con su nombre, precio de costo y cantidad disponible.
        self.nombre = nombre
        self.precio_costo = precio_costo
        self.cantidad = cantidad
        self.precio_venta = 0.0

    def establecer_precio_venta(self, precio_venta):
        # Establece el precio de venta del producto.
        self.precio_venta = precio_venta

    def __str__(self):
        # Devuelve una representación en cadena del producto.
        return f"Producto: {self.nombre}, Precio de Venta: {self.precio_venta}, Cantidad: {self.cantidad}"

class Tienda:
    def __init__(self):
        # Inicializa una nueva tienda con un inventario vacío y sin total de ventas.
        self.inventario = []
        self.total_ventas = 0.0

    def agregar_producto(self, producto):
        # Agrega un nuevo producto al inventario de la tienda.
        self.inventario.append(producto)

    def realizar_venta(self, nombre_producto, cantidad_comprada, dinero_cliente):
        # Realiza una venta, actualiza el inventario y calcula el vuelto para el cliente.
        for producto in self.inventario:
            if producto.nombre == nombre_producto:
                if producto.cantidad >= cantidad_comprada:
                    total = producto.precio_venta * cantidad_comprada
                    producto.cantidad -= cantidad_comprada
                    self.total_ventas += total
                    vuelto = dinero_cliente - total
                    return f"Venta realizada. Total: {total}. Vuelto: {vuelto}."
                else:
                    return  print("No hay suficiente cantidad en inventario.")
        return print("Producto no encontrado.")

    def recibir_proveedor(self, nombre_producto, cantidad, precio_costo, precio_venta_sugerido):
        # Recibe un producto de un proveedor y lo agrega o actualiza en el inventario.
        for producto in self.inventario:
            if producto.nombre == nombre_producto:
                producto.cantidad += cantidad
                producto.precio_costo = precio_costo
                producto.establecer_precio_venta(precio_venta_sugerido)
                return
        nuevo_producto = Producto(nombre_producto, precio_costo, cantidad)
        nuevo_producto.establecer_precio_venta(precio_venta_sugerido)
        self.agregar_producto(nuevo_producto)

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario de la tienda.
        for producto in self.inventario:
            print(producto)

# Ejemplo de uso
tienda = Tienda()

# Recibir productos de un proveedor
tienda.recibir_proveedor("Manzanas", 50, 0.5, 1.0)
tienda.recibir_proveedor("Naranjas", 30, 0.4, 0.8)

# Mostrar el inventario
print("Inventario actual:")
tienda.mostrar_inventario()

# Realizar una venta
print(tienda.realizar_venta("Manzanas", 10, 15.0))

# Mostrar el inventario actualizado
print("\nInventario después de la venta:")
tienda.mostrar_inventario()
