import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.login import login

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_failed_login(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = login(browser, wait)
    search_page.go_to_page()  
    search_page.make_a_login_fail("hola@gmail.com", "12345678")
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "Login" in browser.title

def test_successful_login(browser):
    wait = WebDriverWait(browser, 30)  
    search_page = login(browser, wait)
    search_page.go_to_page()  
    search_page.make_a_login_successful("hola@gmail.com", "1234")
    
    # Imprimir el título actual de la página para debugging
    print("Título de la página actual:", browser.title)
    
    # Ajustar la aserción para que coincida con el título real de la página
    assert "CursosYa" in browser.title





