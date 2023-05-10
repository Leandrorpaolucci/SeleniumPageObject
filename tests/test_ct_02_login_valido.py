import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login_valido(self):
        login_page = LoginPage()
        home_page = HomePage()

        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.verificar_login_com_sucesso()
        #assert driver.find_element(By.XPATH, '//span[@class="title"]').is_displayed()

