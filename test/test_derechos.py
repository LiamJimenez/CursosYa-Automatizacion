import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.derechos import Derechos
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_acceder_derechos(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Derechos(browser, wait)
    search_page.go_to_page()  
    search_page.acceder_derechos()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "CursosYa" in browser.title

def test_acceder_mas_informacion(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Derechos(browser, wait)
    search_page.go_to_page()  
    search_page.acceder_mas_informacion()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Derecho" in browser.title


