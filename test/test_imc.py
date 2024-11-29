import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

def test_imc_normal(page):
    page.goto('http://localhost:5000')
    page.fill('#height', '170')
    page.fill('#weight', '70')
    page.click('button[type="submit"]')
    page.wait_for_selector('h3:has-text("Resultado")')
    resultado = page.locator('h3:has-text("Resultado") + p').inner_text()
    assert 'IMC' in resultado
    # page.wait_for_timeout(10000)

def test_imc_sobrepeso(page):
    page.goto('http://localhost:5000')
    page.fill('#height', '160')
    page.fill('#weight', '80')
    page.click('button[type="submit"]')
    page.wait_for_selector('h3:has-text("Resultado")')
    resultado = page.locator('h3:has-text("Resultado") + p').inner_text()
    assert 'IMC' in resultado
    # page.wait_for_timeout(10000)

def test_imc_obesidade(page):
    page.goto('http://localhost:5000')
    page.fill('#height', '150')
    page.fill('#weight', '95')
    page.click('button[type="submit"]')
    page.wait_for_selector('h3:has-text("Resultado")')
    resultado = page.locator('h3:has-text("Resultado") + p').inner_text()
    assert 'IMC' in resultado
    # page.wait_for_timeout(10000)

def test_imc_abaixo_peso(page):
    page.goto('http://localhost:5000')
    page.fill('#height', '190')
    page.fill('#weight', '60')
    page.click('button[type="submit"]')
    page.wait_for_selector('h3:has-text("Resultado")')
    resultado = page.locator('h3:has-text("Resultado") + p').inner_text()
    assert 'Abaixo ' in resultado
    # page.wait_for_timeout(10000)

def test_imc_valores_invalidos(page):
    page.goto('http://localhost:5000')
    page.fill('#height', 'abc')
    page.fill('#weight', 'xyz')
    page.click('button[type="submit"]')
    page.wait_for_selector('.alert-danger')
    erro = page.locator('.alert-danger').inner_text()
    assert 'insira valores válidos' in erro
    # page.wait_for_timeout(10000)

def test_imc_zero_altura(page):
    page.goto('http://localhost:5000')
    page.fill('#height', '0')
    page.fill('#weight', '70')
    page.click('button[type="submit"]')
    page.wait_for_selector('.alert-danger')
    erro = page.locator('.alert-danger').inner_text()
    assert 'maiores que zero' in erro
    # page.wait_for_timeout(10000)

def test_imc_zero_peso(page):
    page.goto('http://localhost:5000')
    page.fill('#height', '170')
    page.fill('#weight', '0')
    page.click('button[type="submit"]')
    page.wait_for_selector('.alert-danger')
    erro = page.locator('.alert-danger').inner_text()
    assert 'maiores que zero' in erro
    # page.wait_for_timeout(10000)
