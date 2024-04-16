from pages.base_page import BasePage
from Data.locators import LoginLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class login(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/Admin/OneDrive/Escritorio/CursosYA/HTML/login.html"
        self.locator = LoginLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def make_a_login_fail(self, input_email, input_password):
        self.driver.find_element(*self.locator.escibir_email).send_keys(input_email)
        self.driver.find_element(*self.locator.escribir_contraseña).send_keys(input_password)
        self.driver.find_element(*self.locator.boton_acceder).click()

        self.driver.save_screenshot("results/login_fallido.png")

    def make_a_login_successful(self, input_email, input_password):
        self.driver.find_element(*self.locator.escibir_email).send_keys(input_email)
        self.driver.find_element(*self.locator.escribir_contraseña).send_keys(input_password)
        self.driver.find_element(*self.locator.boton_acceder).click()

        self.driver.save_screenshot("results/login_exitoso.png")


   



    