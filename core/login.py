from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time




def iniciar_driver(headless=True):
    """Inicia o Chrome (cross-platform) usando webdriver_manager.
    Retorna o objeto driver.
    """
    options = Options()
    if headless:
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        # evita erros em alguns ambientes
        options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver




def fazer_login(driver, usuario="standard_user", senha="secret_sauce"):
    """Faz login no SauceDemo. Lança exceção se falhar."""
    driver.get("https://www.saucedemo.com")
    time.sleep(1)


    user_input = driver.find_element(By.ID, "user-name")
    pass_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")


    user_input.clear()
    user_input.send_keys(usuario)
    pass_input.clear()
    pass_input.send_keys(senha)
    login_btn.click()


    time.sleep(1)
    # simples verificação se o login funcionou
    if "inventory.html" not in driver.current_url:
        raise RuntimeError("Login falhou — verifique credenciais/alterações no site")


    return True