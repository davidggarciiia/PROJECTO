from datetime import datetime
import uuid
import csv
import os

class Ticket:
    def __init__(self, pelicula, asientos, precio_total):
        self.pelicula = pelicula
        self.asientos = asientos
        self.precio_total = precio_total
        self.id = str(uuid.uuid4())  # Genera un ID único para el ticket
        self.fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def generar_ticket(self):
        """Imprime el ticket con formato y lo guarda en CSV"""
        # --- Mostrar ticket ---
        print("\n" + "=" * 52)
        print("\t       🎟️  TICKET DE COMPRA 🎟️")
        print("=" * 52)
        print(f"Pelicula: {self.pelicula}")
        print(f"Fecha: {self.fecha}")
        print("\nAsientos seleccionados:")
        for asiento in self.asientos:
            print(f"- Fila {asiento[0]}, Columna {asiento[1]}")
        print("\n" + "-" * 52)
        print(f"PRECIO TOTAL: €{self.precio_total:.2f}")
        print("-" * 52)
        print(f"ID del Ticket: {self.id}")
        print("=" * 52)
        print("\t       ¡Gracias por su compra!")
        print("=" * 52)

        # --- Guardar en CSV ---
        self.guardar_en_csv()

    def guardar_en_csv(self):
        """Guarda la información del ticket en un archivo CSV dentro de la carpeta actual (TICKET/)."""
        # Obtener la ruta del archivo actual (carpeta TICKET)
        carpeta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_csv = os.path.join(carpeta_actual, "tickets.csv")

        # Verificar si el archivo ya existe
        existe = os.path.isfile(ruta_csv)

        with open(ruta_csv, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # Si el archivo no existe, escribir encabezado
            if not existe:
                writer.writerow(["ID", "Pelicula", "Fecha", "Asientos", "Precio Total (€)"])

            # Convertir lista de asientos a texto legible
            asientos_str = "; ".join([f"Fila {a[0]}, Columna {a[1]}" for a in self.asientos])

            # Escribir datos del ticket
            writer.writerow([self.id, self.pelicula, self.fecha, asientos_str, f"{self.precio_total:.2f}"])


def generar_ticket(pelicula, asientos, precio):
    """Genera y muestra el ticket de la compra, y lo guarda en CSV."""
    precio_total = precio * len(asientos)  # Calcular el precio total basado en el número de asientos
    mi_ticket = Ticket(pelicula.titulo, asientos, precio_total)
    mi_ticket.generar_ticket()
