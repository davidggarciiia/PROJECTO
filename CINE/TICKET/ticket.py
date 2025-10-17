from datetime import datetime
import uuid

class Ticket:
    def __init__(self, pelicula, asientos, precio_total):
        self.pelicula = pelicula
        self.asientos = asientos
        self.precio_total = precio_total
        self.id = str(uuid.uuid4())  # Genera un ID único para el ticket

    def generar_ticket(self):
        # Imprimir el ticket por pantalla
        print("🎟️ Ticket de Compra 🎟️")
        print(f"Pelicula: {self.pelicula}")
        print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("Asientos seleccionados:")
        for asiento in self.asientos:
            print(f"- Fila {asiento[0]}, Columna {asiento[1]}")
        print(f"Precio Total: ${self.precio_total:.2f}")
        print(f"ID del Ticket: {self.id}")
        print("¡Gracias por su compra!")