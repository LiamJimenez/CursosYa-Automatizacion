from pages.base_page import BasePage
from Data.locators import cursosgratuitosLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class CursosGratis(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/CursosYa.html"
        self.locator = cursosgratuitosLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def ver_cursos_gratuitos(self):
        self.driver.find_element(*self.locator.boton_cursos_gratuitos).click()

        self.driver.save_screenshot("results/cursosgratuitos.png")

    def ver_video(self):
        self.driver.find_element(*self.locator.boton_cursos_gratuitos).click()
        self.driver.find_element(*self.locator.iniciar_video).click()

        self.driver.save_screenshot("results/video_curso.png")

    