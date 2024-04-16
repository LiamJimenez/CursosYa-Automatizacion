import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.ayuda import Ayuda

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_ver_ayuda(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Ayuda(browser, wait)
    search_page.go_to_page()  
    search_page.ver_ayuda()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Ayuda" in browser.title

def test_ver_ayuda_info(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Ayuda(browser, wait)
    search_page.go_to_page()  
    search_page.ver_ayuda_info()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Más Información sobre Ayuda al Cliente" in browser.title