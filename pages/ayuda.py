from pages.base_page import BasePage
from Data.locators import ayudaLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class Ayuda(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/CursosYa.html"
        self.locator = ayudaLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def ver_ayuda(self):
        self.driver.find_element(*self.locator.boton_ayuda).click()

        self.driver.save_screenshot("results/ayuda.png")

    def ver_ayuda_info(self):
        self.driver.find_element(*self.locator.boton_ayuda).click()
        self.driver.find_element(*self.locator.boton_mas_info).click()

        self.driver.save_screenshot("results/ayuda_info.png")