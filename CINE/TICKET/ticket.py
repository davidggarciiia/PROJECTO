import qrcode
from datetime import datetime
from Cine import CINE
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

        # Generar el código QR con la información del ticket
        info_qr = {
            "id": self.id,
            "pelicula": self.pelicula,
            "asientos": self.asientos,
            "precio_total": self.precio_total,
            "fecha": datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        }
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(info_qr)
        qr.make(fit=True)

        # Guardar el QR como imagen
        qr_img = qr.make_image(fill="black", back_color="white")
        qr_img.save("ticket_qr.png")
        print("\nCódigo QR generado: ticket_qr.png")