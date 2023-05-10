import pytest
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct_03_login_invalido(self):
        mensagem_erro_esperada = "Epic sadface: Username and password do not match any user in this service"

        # instancia os objetos a serem usados no teste
        login_page = LoginPage()

        # FAZ LOGIN
        login_page.fazer_login("standard_user", "senha_incorreta")

        # Verifica se o login nao foi realizado e a mensagem de erro apareceu
        login_page.verificar_mansagem_erro_login_existe()

        #verifica o texto da mensagem de erro
        login_page.verificar_texto_mensagem_erro_login(mensagem_erro_esperada)


