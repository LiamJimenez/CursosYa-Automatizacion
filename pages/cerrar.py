from pages.base_page import BasePage
from Data.locators import cerrarsesionLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Cerrar(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/CursosYa.html#cursos%20populares"
        self.locator = cerrarsesionLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def no_cerrar_sesion(self):
        self.driver.find_element(*self.locator.boton_cerrar).click()
        self.driver.find_element(*self.locator.boton_no_cerrar).click()

        self.driver.save_screenshot("results/no_cerrar_sesion.png")

    def si_cerrar_sesion(self):
        self.driver.find_element(*self.locator.boton_cerrar).click()
        self.driver.find_element(*self.locator.boton_si_cerrar).click()

        self.driver.save_screenshot("results/si_cerrar_sesion.png")
