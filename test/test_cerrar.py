import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.cerrar import Cerrar

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_no_cerrar_sesion(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Cerrar(browser, wait)
    search_page.go_to_page()  
    search_page.no_cerrar_sesion()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "CursosYa" in browser.title

def test_si_cerrar_sesion(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = Cerrar(browser, wait)
    search_page.go_to_page()  
    search_page.si_cerrar_sesion()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Login" in browser.title