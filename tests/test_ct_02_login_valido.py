import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login_valido(self):
        driver = conftest.driver
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "secret_sauce")
        # driver.find_element(By.ID, 'user-name').send_keys("standard_user") #login
        # driver.find_element(By.ID, 'password').send_keys("secret_sauce") #senha
        # driver.find_element(By.ID, 'login-button').click() #clicandop botao

        assert driver.find_element(By.XPATH, '//span[@class="title"]').is_displayed()

