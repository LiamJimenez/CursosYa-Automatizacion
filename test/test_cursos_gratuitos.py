import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.cursos_gratuitos import CursosGratis

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_ver_cursos_gratuitos(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = CursosGratis(browser, wait)
    search_page.go_to_page()  
    search_page.ver_cursos_gratuitos()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Cursos Gratuitos" in browser.title



def test_ver_video(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = CursosGratis(browser, wait)
    search_page.go_to_page()  
    search_page.ver_video()
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "YouTube" in browser.title



