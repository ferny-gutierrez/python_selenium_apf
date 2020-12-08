import pytest

from common.webdriver_factory import create_driver_instance
from pages.demoqa.book_store_form import BookStore

DATOS_FORMULARIO = [
    ('Learning'),
    ('Git')
]

@pytest.mark.parametrize("filtro", DATOS_FORMULARIO)
def test_uno(filtro):
    driver = create_driver_instance('chrome')
    objetoPagina = BookStore(driver)
    objetoPagina.abrir_pagina_web()
    objetoPagina.esperar_hasta_que_se_cargue_elemento()
    objetoPagina.buscar(filtro)
    objetoPagina.obtener_info_table()
    objetoPagina.cerrar_navegador()