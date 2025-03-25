
from twilio.rest import Client

sid = 'AC02980d23d1e45df3f5ddbc2a13ce9999'
auth_token = '794742c1b687e12dec7670dde7eb4412'

client = Client(sid, auth_token)
respuestas_ropa = {
    "ropa": "👚 Ropa disponible en nuestra tienda:\n- Camisetas de algodón.\n- Pantalones de mezclilla.\n- Chaquetas de abrigo.\n- Vestidos elegantes para ocasiones especiales.",
    "zapatos": "👠 Nuestra colección de zapatos incluye:\n- Zapatos deportivos de alto rendimiento.\n- Tacones elegantes.\n- Botines de invierno.\n- Sandalias cómodas para verano.",
    "calzado": "👟 Tipos de calzado que ofrecemos:\n- Zapatillas deportivas.\n- Botas de cuero.\n- Sandalias de playa.\n- Zapatos formales para eventos.",
    "tamaños": "📏 Disponibilidad de tamaños:\n- Camisetas: S, M, L, XL.\n- Zapatos: 36-44.\n- Pantalones: 28-38.",
    "ofertas": "💥 Ofertas especiales de la semana:\n- 20% de descuento en zapatos deportivos.\n- 30% de descuento en chaquetas de invierno.\n- Compra 2 camisetas y obtén la tercera gratis.",
    "envio": "🚚 Envíos: Realizamos envíos a nivel nacional. El costo varía según la ubicación. ¡Consulta las tarifas en nuestro sitio web!",
    "gracias": "🙏 ¡Gracias por tu interés en nuestra tienda de ropa y calzado! 🎉 No dudes en preguntarnos cualquier otra cosa. ¡Te esperamos pronto!",
}

mensaje_usuario = input("Escribe un mensaje: ").lower()

respuesta_bot = respuestas_ropa.get(mensaje_usuario, "🤖 Lo siento, no entendí. ¿Puedes intentar con otra palabra clave?")

try:
    message = client.messages.create(
        to='whatsapp:+5217751545997',  
        from_='whatsapp:+14155238886',  
        body=respuesta_bot
    )

    print(f"✅ Mensaje enviado correctamente. SID: {message.sid}")

except Exception as e:
    print(f"❌ Error al enviar el mensaje: {e}")