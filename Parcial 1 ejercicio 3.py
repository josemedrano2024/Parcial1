class Hotel:
    def __init__(self):
        self.habitaciones = {
            'Simple': 50,
            'Doble': 75,
            'Suite': 120
        }
        self.servicios_extra = {
            'Piscina': 10,
            'Cancha de Golf': 30
        }
        self.reservas = []

    def mostrar_habitaciones(self):
        print("\n--- Habitaciones Disponibles ---")
        for tipo, precio in self.habitaciones.items():
            print(f"{tipo}: ${precio} por noche")

    def mostrar_servicios(self):
        print("\n--- Servicios Extra ---")
        for servicio, costo in self.servicios_extra.items():
            print(f"{servicio}: ${costo}")

    def registrar_reserva(self, nombre_cliente, tipo_habitacion, noches, servicios=[]):
        if tipo_habitacion not in self.habitaciones:
            print("Habitación no disponible.")
            return

        costo_habitacion = self.habitaciones[tipo_habitacion] * noches
        costo_servicios = sum(self.servicios_extra[servicio] for servicio in servicios)
        total = costo_habitacion + costo_servicios

        reserva = {
            'cliente': nombre_cliente,
            'habitacion': tipo_habitacion,
            'noches': noches,
            'servicios': servicios,
            'total': total
        }
        self.reservas.append(reserva)

        self.generar_factura(reserva)

    def generar_factura(self, reserva):
        print("\n--- Factura ---")
        print(f"Cliente: {reserva['cliente']}")
        print(f"Habitación: {reserva['habitacion']}")
        print(f"Número de noches: {reserva['noches']}")
        print(f"Total por habitación: ${self.habitaciones[reserva['habitacion']] * reserva['noches']}")
        
        if reserva['servicios']:
            print("\nServicios extra:")
            for servicio in reserva['servicios']:
                print(f"{servicio}: ${self.servicios_extra[servicio]}")
            print(f"Total por servicios: ${sum(self.servicios_extra[servicio] for servicio in reserva['servicios'])}")
        
        print(f"\nTotal a pagar: ${reserva['total']}")

# Ejemplo de uso
hotel = Hotel()
hotel.mostrar_habitaciones()
hotel.mostrar_servicios()

# Simulación de reserva
nombre_cliente = "Juan Pérez"
tipo_habitacion = "Suite"
noches = 3
servicios = ["Piscina", "Cancha de Golf"]

hotel.registrar_reserva(nombre_cliente, tipo_habitacion, noches, servicios)
