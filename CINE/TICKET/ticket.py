from datetime import datetime
import uuid

class Ticket:
    def __init__(self, pelicula, asientos, precio_total):
        self.pelicula = pelicula
        self.asientos = asientos
        self.precio_total = precio_total
        self.id = str(uuid.uuid4())  # Genera un ID único para el ticket

    def generar_ticket(self):
        # Imprimir el ticket con formato y diseño
        print("\n" + "=" * 40)
        print("\t🎟️  TICKET DE COMPRA  🎟️")
        print("=" * 40)
        print(f"Pelicula: {self.pelicula}")
        print(f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print("\nAsientos seleccionados:")
        for asiento in self.asientos:
            print(f"- Fila {asiento[0]}, Columna {asiento[1]}")
        print("\n" + "-" * 40)
        print(f"PRECIO TOTAL: €{self.precio_total:.2f}")
        print("-" * 40)
        print(f"ID del Ticket: {self.id}")
        print("=" * 40)
        print("\t¡Gracias por su compra!")
        print("=" * 40)

def generar_ticket(pelicula, asientos, precio):
    """Genera y muestra el ticket de la compra."""
    precio_total = precio * len(asientos)  # Calcular el precio total basado en el número de asientos
    mi_ticket = Ticket(pelicula.titulo, asientos, precio_total)
    mi_ticket.generar_ticket()