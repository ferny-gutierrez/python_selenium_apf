from common.webdriver_factory import create_driver_instance
from pages.expedia.home_expedia_page import HomeExpediaPage

try:
    driver = create_driver_instance('chrome')
    objPagina = HomeExpediaPage(driver)
    objPagina.abrir_pagina_web()
    objPagina.esperar_hasta_que_se_cargue_elemento()
    # objPagina.hacer_click_logo()
    # objPagina.moverse_a_tab_principal()
    # objPagina.hacer_click_anunciar_una_propiedad()
    # objPagina.moverse_a_tab_principal()
    # objPagina.hacer_click_ayuda()
    # objPagina.moverse_a_tab_principal()
    # objPagina.hacer_click_viajes()
    # objPagina.moverse_a_tab_principal()

    objPagina.hospedaje.esperar_hastaque_secargue()
    objPagina.hospedaje.destino.esperar_hastaque_secargue()
    objPagina.hospedaje.destino.colocar_valor('Guadalajara')
    calendar = objPagina.hospedaje.click_check_in()
    print(f'First Month: {calendar.get_first_month()}')
    print(f'Second Month: {calendar.get_second_month()}')
    calendar.select_dates(20, 30)
    objPagina.hospedaje.search()
finally:
    driver.quit()
