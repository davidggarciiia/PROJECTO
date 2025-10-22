class Descuento:

    def __init__(self):
        self.descuentos = {
            1: {"tipo": "Estudiante", "porcentaje": 0.20},
            2: {"tipo": "Infantil", "porcentaje": 0.50},
            3: {"tipo": "Jubilado", "porcentaje": 0.30}
        }
    
    def mostrar_opciones(self):
        for clave, info in self.descuentos.items():
            porcentaje = int(info["porcentaje"] * 100)
            print(f"[{clave}] {info['tipo']} -- {porcentaje}% de descuento")

    def aplicar_descuento(self, tipo_descuento, precio):
        if tipo_descuento not in self.descuentos:
            print("Tipo de descuento no válido.")
            return precio
        
        if precio < 0:
            print("El precio no puede ser negativo.")
            return precio

        descuento_info = self.descuentos[tipo_descuento]
        descuento = descuento_info["porcentaje"]
        precio_con_descuento = precio * (1 - descuento)
        
        print(f"Descuento aplicado: {descuento*100:.0f}%. Precio con descuento: ${precio_con_descuento:.2f}")
        return precio_con_descuento