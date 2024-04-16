import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.nosotros import Nosotros

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_acceder_nosotros(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Nosotros(browser, wait)
    search_page.go_to_page()  
    search_page.acceder_nosotros()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Presentacion" in browser.title

def test_acceder_facebook(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Nosotros(browser, wait)
    search_page.go_to_page()  
    search_page.acceder_facebook()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Facebook" in browser.title
