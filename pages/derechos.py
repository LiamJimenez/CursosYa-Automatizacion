from pages.base_page import BasePage
from Data.locators import derechosLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os

class Derechos(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/CursosYa.html#derechos"
        self.locator = derechosLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def acceder_derechos(self):
        self.driver.find_element(*self.locator.boton_derechos).click()
        self.driver.save_screenshot("results/derechos.png")

    def acceder_mas_informacion(self):
        self.driver.find_element(*self.locator.boton_mas_informacion).click()
        self.driver.save_screenshot("results/mas_informacion.png")

   
    



