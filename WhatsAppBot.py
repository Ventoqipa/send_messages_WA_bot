from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(r"C:\Users\USER\python\01.whatsAppBot\driver\msedgedriver.exe")
options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Edge(service=service, options=options)

def seleccionarChat(nombre: str):
    print("🔍 BUSCANDO CHAT...")
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "span")))
        elements = browser.find_elements(By.TAG_NAME, "span")
        for element in elements:
            try:
                if element.text == nombre:
                    print(f"✅ Chat '{nombre}' encontrado.")
                    element.click()
                    return True
            except Exception:
                pass
        print(f"❌ Chat '{nombre}' no encontrado.")
        return False
    except Exception as e:
        print(f"❌ Error al buscar el chat: {e}")
        return False

def validaQR():
    """Verifica si el código QR está presente en la página de WhatsApp Web."""
    try:
        browser.find_element(By.TAG_NAME, "canvas")
        return True
    except Exception:
        return False

def enviarmensaje(mensaje: str):
    """Envía un mensaje al chat seleccionado."""
    try:
        chatbox = WebDriverWait(browser, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'))
        )
        chatbox.send_keys(mensaje)
        chatbox.send_keys(Keys.ENTER)
        time.sleep(2) 
        print("✅ Mensaje enviado con éxito:", mensaje)
    except Exception as e:
        print(f"❌ Error al enviar el mensaje: {e}")

def leerArchivo():
    """Lee un archivo de texto y envía los mensajes al chat activo."""
    try:
        with open('./resource/PruebaBot.txt', mode='r', encoding='utf-8') as archivo:
            for linea in archivo.readlines():
                mensaje = linea.strip()
                if mensaje: 
                    print("MENSAJE:", mensaje)
                    enviarmensaje(mensaje)
        print("✅ Mensajes enviados desde archivo.")
    except Exception as e:
        print(f"❌ Error al leer o enviar mensajes desde el archivo: {e}")

def botWhatsapp():
    """Abre WhatsApp Web y espera la autenticación del usuario."""
    browser.get("https://web.whatsapp.com/")
    time.sleep(25)  
    while True:
        print("⌛ ESPERANDO AUTENTICACIÓN...")
        if not validaQR():
            print("✅ SE AUTENTICÓ")
            break
        time.sleep(2)


botWhatsapp()
    

time.sleep(25)

if seleccionarChat("Ruby"):
    leerArchivo()

print("\n✅ WhatsApp Web sigue abierto. Puedes escribir más comandos en la terminal.")
