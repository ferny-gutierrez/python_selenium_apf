from common.webdriver_factory import create_driver_instance
from pages.base_page import BasePage

try:
    driver = create_driver_instance('chrome')
    page = BasePage(driver,5,'http://demoqa.com/books')
    page.abrir_pagina_web()
    page.esperar_hasta_que_se_cargue_elemento()
    page.refrescar_pagina()
finally:
    driver.cerrar_navegador()