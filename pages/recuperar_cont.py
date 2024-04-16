from pages.base_page import BasePage
from Data.locators import recuperarcontLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class Recuperar_Cont(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/login.html"
        self.locator = recuperarcontLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def recuperar_cont_fallida(self, input_email, input_password):
        self.driver.find_element(*self.locator.boton_recuperarcont).click()
        self.driver.find_element(*self.locator.escribir_email_recuperar).send_keys(input_email)
        self.driver.find_element(*self.locator. escribir_contraseña_recuperar).send_keys(input_password)
        self.driver.find_element(*self.locator.  escribir_contraseña_recuperar_confir).send_keys(input_password)
        self.driver.find_element(*self.locator.boton_continuar).click()

        self.driver.save_screenshot("results/recuperar_fallido.png")

    def recuperar_cont_exito(self, input_email, input_password):
        self.driver.find_element(*self.locator.boton_recuperarcont).click()
        self.driver.find_element(*self.locator.escribir_email_recuperar).send_keys(input_email)
        self.driver.find_element(*self.locator. escribir_contraseña_recuperar).send_keys(input_password)
        self.driver.find_element(*self.locator.  escribir_contraseña_recuperar_confir).send_keys(input_password)
        self.driver.find_element(*self.locator.boton_continuar).click()

        self.driver.save_screenshot("results/recuperar_exito.png")