from pages.base_page import BasePage
from Data.locators import nosotrosLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Nosotros(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/CursosYa.html#derechos"
        self.locator = nosotrosLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def acceder_nosotros(self):
        self.driver.find_element(*self.locator.boton_nosotros).click()

        self.driver.save_screenshot("results/nosotros.png")

    def acceder_facebook(self):
        self.driver.find_element(*self.locator.boton_nosotros).click()
        self.driver.find_element(*self.locator.boton_facebook).click()

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'fb_logo')]"))
            )
        except TimeoutException:
            # Si se produce un tiempo de espera, intentaremos capturar la pantalla de todos modos
            pass

        self.driver.save_screenshot("results/facebook.png")


    