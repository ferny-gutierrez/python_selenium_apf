import pytest

from common.webdriver_factory import create_driver_instance
from pages.expedia.home_expedia_page import HomeExpediaPage

DATOS_FORMULARIO = [
    ('Guadalajara', 20, 30),
    ('Bogotá (BOG - A. Internacional El Dorado)',24, 31)
]
@pytest.mark.parametrize("destino, diaInicial, diaFinal", DATOS_FORMULARIO)
def test_uno(destino, diaInicial, diaFinal):
    driver = create_driver_instance('chrome')
    objPagina = HomeExpediaPage(driver)
    objPagina.abrir_pagina_web()
    objPagina.esperar_hasta_que_se_cargue_elemento()
    objPagina.hospedaje.esperar_hastaque_secargue()
    objPagina.hospedaje.destino.esperar_hastaque_secargue()
    objPagina.hospedaje.destino.colocar_valor(destino)
    calendar = objPagina.hospedaje.click_check_in()
    print(f'First Month: {calendar.get_first_month()}')
    print(f'Second Month: {calendar.get_second_month()}')
    calendar.select_dates(diaInicial, diaFinal)
    objPagina.hospedaje.search()
    objPagina.cerrar_navegador()