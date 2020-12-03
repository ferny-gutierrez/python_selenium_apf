from common.webdriver_factory import create_driver_instance
from pages.expedia.home_expedia_page import HomeExpediaPage

try:
    driver = create_driver_instance('chrome')
    objPagina = HomeExpediaPage(driver)
    objPagina.abrir_pagina_web()
    objPagina.esperar_hasta_que_se_cargue_elemento()
    objPagina.hacer_click_logo()
    objPagina.moverse_a_tab_principal()
    objPagina.hacer_click_anunciar_una_propiedad()
    objPagina.moverse_a_tab_principal()
    objPagina.hacer_click_ayuda()
    objPagina.moverse_a_tab_principal()
    objPagina.hacer_click_viajes()
    objPagina.moverse_a_tab_principal()
finally:
    driver.quit()
