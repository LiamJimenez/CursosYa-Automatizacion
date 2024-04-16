from selenium.webdriver.common.by import By

class LoginLocators:
    escibir_email = (By.XPATH, "//*[@id='email']")
    escribir_contraseña = (By.XPATH, "//*[@id='password']")
    boton_acceder = (By.XPATH, "//*[@id='btn-acceder']")

class registroLocators:
    escibir_nombreR = (By.XPATH, "//*[@id='nombreR']")
    escibir_emailR = (By.XPATH, "//*[@id='emailR']")
    escribir_contraseñaR = (By.XPATH, "//*[@id='passwordR']")
    boton_registro = (By.XPATH, "//*[@id='btn-registrarse']")

class nosotrosLocators:
    boton_nosotros = (By.XPATH, "//*[@id='link-nosotros']")
    boton_facebook = (By.XPATH, "//*[@id='redes-sociales']")

class cursosLocators:
    boton_cursos = (By.XPATH, "//*[@id='link-cursos']")
    boton_cursos_populares = (By.XPATH, "//*[@id='link-cursos-populares']")

class cerrarsesionLocators:
    boton_cerrar = (By.XPATH, "//*[@id='cerrar-sesion-item']")
    boton_no_cerrar = (By.XPATH, "//*[@id='boton-no']")
    boton_si_cerrar = (By.XPATH, "//*[@id='boton-si']")

class derechosLocators:
    boton_derechos = (By.XPATH, "//*[@id='link-derechos']")
    boton_mas_informacion = (By.XPATH, "//*[@id='mas-informacion-derechos']")
    
class comentariosLocators:
    escribir_comentario = (By.XPATH, "//*[@id='texto-comentario']")
    boton_enviar = (By.XPATH, "//*[@id='enviar-comentario']")
    boton_cancelar = (By.XPATH, "//*[@id='cancelar-comentario']")

class cursosgratuitosLocators:
    boton_cursos_gratuitos = (By.XPATH, "//*[@id='link-cursos-gratuitos']")
    iniciar_video = (By.XPATH, "//*[@id='thumbnail-image']")

class recuperarcontLocators:
    boton_recuperarcont = (By.XPATH, "//*[@id='link-recuperar']")
    escribir_email_recuperar = (By.XPATH, "//*[@id='email']")
    escribir_contraseña_recuperar = (By.XPATH, "//*[@id='password']")
    escribir_contraseña_recuperar_confir = (By.XPATH, "//*[@id='confirm-password']")
    boton_continuar = (By.XPATH, "//*[@id='btn-continuar']")

class ayudaLocators:
    boton_ayuda = (By.XPATH, "//*[@id='link-Ayuda']")
    boton_mas_info = (By.XPATH, "//*[@id='mas-info-btn']")


   
    


