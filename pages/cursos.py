from pages.base_page import BasePage
from Data.locators import cursosLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Cursos(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/CursosYa.html#cursos%20populares"
        self.locator = cursosLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def acceder_cursos(self):
        self.driver.find_element(*self.locator.boton_cursos).click()

        self.driver.save_screenshot("results/cursos.png")

    def acceder_cursos_populares(self):
        self.driver.find_element(*self.locator. boton_cursos_populares).click()

        self.driver.save_screenshot("results/cursos_populares.png")