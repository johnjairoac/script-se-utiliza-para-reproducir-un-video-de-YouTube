import time
import webbrowser
import random

# Enlace del vídeo de YouTube
youtube_link = "https://www.youtube.com/watch?v=Mn6taI8Wzao&t=7s"

# Tiempo de espera antes de cerrar el vídeo (en segundos)
tiempo_espera = 158  # 2 minutos y 38 segundos

# Tiempo de espera entre cada reproducción (en segundos)
tiempo_espera_hora = 3600  # 3600 segundos = 1 hora

# Función para generar una dirección IP ficticia
def generar_ip_ficticia():
    ip = "192.168." + ".".join(str(random.randint(0, 255)) for _ in range(2))
    return ip

# Función para reproducir el vídeo
def reproducir_video():
    # Generar una dirección IP ficticia
    ip_ficticia = generar_ip_ficticia()
    # Establecer la dirección IP ficticia en la variable de entorno http_proxy
    # Esto es solo un ejemplo y puede no funcionar en todas las configuraciones
    # En entornos reales, es posible que necesites usar una biblioteca como requests con proxies
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open_new("http://{}".format(ip_ficticia))
    webbrowser.get('chrome').open(youtube_link)
    tiempo_actual = time.time()
    print("Reproduciendo el vídeo. Tiempo actual:", time.strftime("%H:%M:%S", time.localtime(tiempo_actual)))
    time.sleep(tiempo_espera)
    # Puedes ajustar el tiempo de espera aquí si deseas simular una pausa más larga entre cada reproducción

# Función para calcular y mostrar el tiempo transcurrido
def mostrar_tiempo_transcurrido(tiempo_inicial):
    tiempo_transcurrido = time.time() - tiempo_inicial
    print("Tiempo transcurrido:", int(tiempo_transcurrido / 3600), "horas,", int((tiempo_transcurrido % 3600) / 60), "minutos,", int(tiempo_transcurrido % 60), "segundos")

# Iniciar el temporizador principal
tiempo_inicial = time.time()

# Reproducir el vídeo cada hora
while True:
    reproducir_video()
    # Esperar hasta la próxima hora antes de continuar
    tiempo_restante = tiempo_espera_hora - (time.time() - tiempo_inicial) % tiempo_espera_hora
    print("Esperando", int(tiempo_restante / 60), "minutos hasta la próxima reproducción...")
    time.sleep(tiempo_restante)
    mostrar_tiempo_transcurrido(tiempo_inicial)
