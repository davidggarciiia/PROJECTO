class Descuento:

    def __init__(self):
        # Inicialización de la clase Descuento
        self.descuentos = {
            1: {"tipo": "Estudiante", "porcentaje": 0.20},
            2: {"tipo": "Infantil", "porcentaje": 0.50},
            3: {"tipo": "Jubilado", "porcentaje": 0.30}
        }
    
    def mostrar_opciones(self):
        opciones = [
            "[1] Estudiante -- 20% de descuento",
            "[2] Infantil -- 50% de descuento",
            "[3] Jubilado -- 30% de descuento"
        ]
        for opcion in opciones:
            print(opcion)

    def aplicar_descuento(self, tipo_descuento, precio):
        if tipo_descuento == 1:  # Estudiante
            descuento = 0.20
        elif tipo_descuento == 2:  # Infantil
            descuento = 0.50
        elif tipo_descuento == 3:  # Jubilado
            descuento = 0.30
        else:
            print("Tipo de descuento no válido.")
            return precio

        precio_con_descuento = precio * (1 - descuento)
        print(f"Descuento aplicado: {descuento*100}%. Precio con descuento: ${precio_con_descuento:.2f}")
        return precio_con_descuento