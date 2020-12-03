from common.webdriver_factory import create_driver_instance
from pages.demoqa.book_store_form import BookStore

try:
    driver = create_driver_instance('chrome')
    objetoPagina = BookStore(driver)
    objetoPagina.abrir_pagina_web()
    objetoPagina.esperar_hasta_que_se_cargue_elemento()
    objetoPagina.obtener_info_table()
    objetoPagina.buscar('Learning')
    objetoPagina.obtener_info_table()
    objetoPagina.buscar('Git')
    objetoPagina.obtener_info_table()
finally:
    driver.cerrar_navegador()