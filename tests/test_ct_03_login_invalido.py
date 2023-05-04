import pytest
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct_03_login_invalido(self):
        driver = conftest.driver
        driver.find_element(By.ID, 'user-name').send_keys("standard_user") #login
        driver.find_element(By.ID, 'password').send_keys("zzzzz") #senha
        driver.find_element(By.ID, 'login-button').click() #clicandop botao
        assert len(driver.find_elements(By.XPATH, '//span[@class="title"')) == 0
