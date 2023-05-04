import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Remote
servico = Service(ChromeDriverManager().install())

@pytest.fixture
def setup_teardown():
    #setup
    global driver
    global servico
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)  # baixar chromedriver atualizado
    driver.implicitly_wait(5)  # aguarde 5s
    driver.maximize_window()  # maximiza a janela
    driver.get("https://www.saucedemo.com/")  # site

    # run no test
    yield

    #tierdown

    driver.quit()