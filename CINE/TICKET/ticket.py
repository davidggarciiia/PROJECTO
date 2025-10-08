import qrcode
def aplicar_descuento(self, tipo_descuento):
        """
        Aplica un descuento al ticket
        
        Args:
            tipo_descuento: Tipo de descuento ('jubilado', 'dia_espectador', 'matinal', 'estudiante')
        
        Returns:
            bool: True si el descuento se aplicó correctamente, False si no existe
        """
        if tipo_descuento in self.DESCUENTOS:
            descuento = self.DESCUENTOS[tipo_descuento]
            self.precio_final = self.precio_base * (1 - descuento)
            self.descuento_aplicado = tipo_descuento
            return True
        else:
            print(f"⚠️  Descuento '{tipo_descuento}' no disponible")
            return False
    
    def generar_qr(self):
        # Extraer información del asiento y película
        info_ticket = {
            'id': self.id,
            'sala': self.asiento.sala if hasattr(self.asiento, 'sala') else 'N/A',
            'fila': self.asiento.fila,
            'columna': self.asiento.columna,
            'pelicula': self.pelicula.titulo if hasattr(self.pelicula, 'titulo') else str(self.pelicula),
            'horario': self.pelicula.horario if hasattr(self.pelicula, 'horario') else 'N/A',
            'tipo': self.tipo_entrada,
            'precio': f"{self.precio_final:.2f}€"
        }
        
        datos_qr = json.dumps(info_ticket, ensure_ascii=False)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2
        )
        qr.add_data(datos_qr)
        qr.make(fit=True)
        
        img_qr = qr.make_image(fill_color="black", back_color="white")
        return img_qr
    
    def generar_ticket(self):
        """
        Genera el ticket en formato texto para consola
        
        Returns:
            str: Ticket formateado con toda la información
        """
        # INFO ASIENTO
        fila = self.asiento.fila
        columna = self.asiento.columna
        
        # INFO PELI
        titulo_pelicula = self.pelicula.titulo
        horario = self.pelicula.horario #PENDIENTE
        
        # Generar información de descuento si aplica
        descuento_info = ""
        if self.descuento_aplicado:
            porcentaje = int(self.DESCUENTOS[self.descuento_aplicado] * 100)
            descuento_info = f"║  Descuento: {self.descuento_aplicado.upper():<15} (-{porcentaje}%)  ║\n"
            descuento_info += f"║  Precio base: {self.precio_base:>21.2f}€  ║\n"
        
        ticket = f"""
╔═══════════════════════════════════════════════╗
║           🎬 CINEMAX CINEMAS 🎬              ║
╠═══════════════════════════════════════════════╣
║                                               ║
║  Película: {titulo_pelicula:<34} ║
║  Horario:  {horario:<34} ║
║  Butaca:   Fila {fila} - Columna {columna:<20} ║
║                                               ║
║  Tipo:     {self.tipo_entrada.upper():<34} ║
{descuento_info}║  PRECIO:   {self.precio_final:>30.2f}€  ║
║                                               ║
║  ID Ticket: {self.id:<32} ║
║  Comprado:  {self.fecha_compra:<30} ║
║                                               ║
║  ⚠️  Presentar este ticket en la entrada     ║
║  📱 Escanear QR para validación              ║
╚═══════════════════════════════════════════════╝
        """
        return ticket
    
    def guardar_qr(self, nombre_archivo=None):
        """
        Guarda el código QR como imagen PNG
        
        Args:
            nombre_archivo: Nombre del archivo (opcional, se genera automáticamente si no se proporciona)
        
        Returns:
            str: Nombre del archivo guardado
        """
        if nombre_archivo is None:
            nombre_archivo = f"qr_ticket_{self.id}.png"
        
        img_qr = self.generar_qr()
        img_qr.save(nombre_archivo)
        print(f"✅ QR guardado: {nombre_archivo}")
        return nombre_archivo
    
    def __str__(self):
        """Representación en string del ticket"""
        return self.generar_ticket()
    
    def __repr__(self):
        """Representación técnica del ticket"""
        return f"Ticket(id='{self.id}', pelicula='{self.pelicula}', asiento={self.asiento}, precio={self.precio_final:.2f}€)"
















































































