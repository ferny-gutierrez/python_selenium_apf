from common.webdriver_factory import create_driver_instance
from pages.demoqa.login_form import LoginForm

try:
    driver = create_driver_instance('chrome')
    page = LoginForm(driver, 20)
    page.abrir_pagina_web()
    page.esperar_hasta_que_se_cargue_elemento()
    page.set_user_name('sgutierrez')
    page.set_password('123456')
    page.boton_login_click()
finally:
    # driver.close()
    print ('Finalizamos la ejecucion')