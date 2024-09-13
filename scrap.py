from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar el driver automáticamente
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abrir la página de login
driver.get("https://host-a-monitorear:4200")

# Esperar un poco para que la página cargue (puedes ajustar el tiempo si es necesario)
time.sleep(2)

# Localizar los campos de usuario y contraseña (ajusta estos selectores según el HTML de la página)
clientcode_input = driver.find_element(By.NAME, "clientCode") # Asume que "clientCode" es el atributo del input, verifica si es el correcto
username_input = driver.find_element(By.NAME, "userName")  # Asume que "username" es el atributo del input, verifica si es el correcto
password_input = driver.find_element(By.NAME, "password")  # Asume que "password" es el atributo del input

# Introducir las credenciales
clientcode_input.send_keys("clienteee") 
username_input.send_keys("tu_usuario")  # Cambia "tu_usuario" por tu nombre de usuario real
password_input.send_keys("tu_contraseña")  # Cambia "tu_contraseña" por tu contraseña real

# Localizar y hacer clic en el botón de inicio de sesión (ajusta el selector si es necesario)
login_button = driver.find_element(By.XPATH, "//button[@type='button']")  # Verifica el XPath del botón de login
login_button.click()

# Esperar un poco para permitir que la página de inicio de sesión procese
time.sleep(30)

# Configurar el tiempo máximo de ejecución (en segundos), por ejemplo, 1 hora = 3600 segundos
time_limit = 3600  # 1 hora
start_time = time.time()  # Obtener el tiempo de inicio


button_found = False
while (time.time() - start_time) < time_limit:
    try:
        # Intentar encontrar el botón con el texto "Confirm"
        confirm_button = driver.find_element(By.XPATH, "//button[text()='Confirm']")
        if not button_found:
            # Si el botón se encuentra, hacer clic y marcar que fue encontrado
            confirm_button.click()
            button_found = True
            print("¡Botón encontrado y clickeado!")
        else:
            print("Botón ya fue clickeado, esperando durante el tiempo restante...")
    except NoSuchElementException:
        # Si el botón no se encuentra, continuar esperando
        print("Botón no encontrado, intentando nuevamente...")
    
    # Esperar 5 segundos entre intentos para evitar sobrecargar el navegador
    time.sleep(5)

# Una vez que pase 1 hora, finaliza el script
print("Se ha alcanzado el límite de tiempo. Cerrando el navegador...")
driver.quit()
