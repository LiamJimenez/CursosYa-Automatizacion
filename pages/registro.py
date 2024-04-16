from pages.base_page import BasePage
from Data.locators import registroLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class Registro(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/registro.html"
        self.locator = registroLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def make_a_registro_fail(self, input_nombre, input_email, input_password):
        self.driver.find_element(*self.locator.escibir_nombreR).send_keys(input_nombre)
        self.driver.find_element(*self.locator.escibir_emailR).send_keys(input_email)
        self.driver.find_element(*self.locator.escribir_contraseñaR).send_keys(input_password)
        self.driver.find_element(*self.locator.boton_registro).click()

        self.driver.save_screenshot("results/registro_fallido.png")

    def make_a_registro_successful(self, input_nombre, input_email, input_password):
        self.driver.find_element(*self.locator.escibir_nombreR).send_keys(input_nombre)
        self.driver.find_element(*self.locator.escibir_emailR).send_keys(input_email)
        self.driver.find_element(*self.locator.escribir_contraseñaR).send_keys(input_password)
        self.driver.find_element(*self.locator.boton_registro).click()

        self.driver.save_screenshot("results/registro_exitoso.png")


    