from pages.base_page import BasePage
from Data.locators import comentariosLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class Comentarios(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/CursosYa.html"
        self.locator = comentariosLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def enviar_comentario(self, input_comentario):
        self.driver.find_element(*self.locator.escribir_comentario).send_keys(input_comentario)
        self.driver.find_element(*self.locator.boton_enviar).click()

        self.driver.save_screenshot("results/enviar_comentario.png")

    def cancelar_comentario(self, input_comentario):
        self.driver.find_element(*self.locator.escribir_comentario).send_keys(input_comentario)
        self.driver.find_element(*self.locator.boton_cancelar).click()

        self.driver.save_screenshot("results/cancelar_comentario.png")