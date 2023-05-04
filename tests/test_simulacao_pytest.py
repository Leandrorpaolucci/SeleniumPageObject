#pytest - v.\test_simulacao_pytest.py "PASSED" ao invés de ..
import pytest


class TestSimulacao():

    @pytest.mark.simulacao  # marcador de simulacao pytest -m simulacao
    def test_simulacao_1(self):
        assert 1 == 1

    @pytest.mark.simulacao
    @pytest.mark.skip
    def test_simulacao_2(self):
        assert 2 == 2

