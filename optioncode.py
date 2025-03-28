 
from twilio.rest import Client

sid = 'AC02980d23d1e45df3f5ddbc2a13ce9999'
auth_token = '794742c1b687e12dec7670dde7eb4412'

client = Client(sid, auth_token)

opciones = {
    "1": "👚 Ropa disponible en nuestra tienda:\n- Camisetas de algodón.\n- Pantalones de mezclilla.\n- Chaquetas de abrigo.\n- Vestidos elegantes para ocasiones especiales.",
    "2": "👠 Nuestra colección de zapatos incluye:\n- Zapatos deportivos de alto rendimiento.\n- Tacones elegantes.\n- Botines de invierno.\n- Sandalias cómodas para verano.",
    "3": "👟 Tipos de calzado que ofrecemos:\n- Zapatillas deportivas.\n- Botas de cuero.\n- Sandalias de playa.\n- Zapatos formales para eventos.",
    "4": "📏 Disponibilidad de tamaños:\n- Camisetas: S, M, L, XL.\n- Zapatos: 36-44.\n- Pantalones: 28-38.",
    "5": "💥 Ofertas especiales de la semana:\n- 20% de descuento en zapatos deportivos.\n- 30% de descuento en chaquetas de invierno.\n- Compra 2 camisetas y obtén la tercera gratis.",
    "6": "🚚 Envíos: Realizamos envíos a nivel nacional. El costo varía según la ubicación. ¡Consulta las tarifas en nuestro sitio web!",
    "7": "🙏 ¡Gracias por tu interés en nuestra tienda de ropa y calzado! 🎉 No dudes en preguntarnos cualquier otra cosa. ¡Te esperamos pronto!",
}

mensaje_usuario = input("Elige una opción:\n1 - Ropa\n2 - Zapatos\n3 - Calzado\n4 - Tamaños\n5 - Ofertas\n6 - Envíos\n7 - Gracias\n").strip()

respuesta_bot = opciones.get(mensaje_usuario, "🤖 Lo siento, no entendí. ¿Puedes intentar con otra opción?")

try:
    message = client.messages.create(
        to='whatsapp:+5217751545997',  
        from_='whatsapp:+14155238886', 
        body=respuesta_bot
    )

    print(f"✅ Mensaje enviado correctamente. SID: {message.sid}")

except Exception as e:
    print(f"❌ Error al enviar el mensaje: {e}")



    





"""
  from twilio.rest import Client

sid = 'AC02980d23d1e45df3f5ddbc2a13ce9999'
auth_token = '794742c1b687e12dec7670dde7eb4412'

client = Client(sid, auth_token)

opciones = {
    "1": " Ropa disponible en nuestra tienda:\n\n- Camisetas de algodón.\n- Pantalones de mezclilla.\n- Chaquetas de abrigo.\n- Vestidos elegantes para ocasiones especiales.",
    "2": " Nuestra colección de zapatos incluye:\n\n- Zapatos deportivos de alto rendimiento.\n- Tacones elegantes.\n- Botines de invierno.\n- Sandalias cómodas para verano.",
    "3": " Tipos de calzado que ofrecemos:\n\n- Zapatillas deportivas.\n- Botas de cuero.\n- Sandalias de playa.\n- Zapatos formales para eventos.",
    "4": " Disponibilidad de tamaños:\n\n- Camisetas: S, M, L, XL.\n- Zapatos: 36-44.\n- Pantalones: 28-38.",
    "5": " Ofertas especiales de la semana:\n\n- 20% de descuento en zapatos deportivos.\n- 30% de descuento en chaquetas de invierno.\n- Compra 2 camisetas y obtén la tercera gratis.",
    "6": " Envíos: Realizamos envíos a nivel nacional. El costo varía según la ubicación. ¡Consulta las tarifas en nuestro sitio web!",
    "7": " ¡Gracias por tu interés en nuestra tienda de ropa y calzado!  No dudes en preguntarnos cualquier otra cosa. ¡Te esperamos pronto!",
}

print("Elige una opción:")
print("1. Ropa")
print("2. Zapatos")
print("3. Calzado")
print("4. Tamaños")
print("5. Ofertas")
print("6. Envíos")
print("7. Gracias")

mensaje_usuario = input("Escribe el número de la opción que deseas: ").strip()

respuesta_bot = opciones.get(mensaje_usuario, " Lo siento, no entendí. ¿Puedes intentar con otra opción?")

try:
    message = client.messages.create(
        to='whatsapp:+5217751545997',
        from_='whatsapp:+14155238886',
        body=respuesta_bot
    )

    print(f"✅ Mensaje enviado correctamente. SID: {message.sid}")

except Exception as e:
    print(f"❌ Error al enviar el mensaje: {e}")"
    ""
    """