import os
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.practice_form import PracticeForm
try:
    driver = create_driver_instance('chrome')
    driver.get('chrome://settings/')
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.75);')
    page = PracticeForm(driver,20)
    page.abrir_pagina_web()
    page.esperar_hasta_que_se_cargue_elemento()
    page.set_first_name('Sandra')
    page.set_last_name('Gutierrez')
    page.set_email('ferny.gutierrez@gmail.com')
    page.set_gender('Female')
    page.set_mobile('3003656382')
    page.set_hobbies('Sports')
    page.set_subjects('Maths')
    page.set_subjects('Computer Science')
    page.set_current_address('CRA 17 # 136 - 73')
    page.set_date_of_birth("Nov 30 2020")
    file_path = os.path.join(ROOT_DIR, '.gitignore')
    page.set_file("C:\\Users\\Usuario\\Documents\\bootcamptest\\2020_Python_Selenium-main\\.gitignore")
    page.set_state('NCR')
    page.set_city('Delhi')

finally:
    driver.cerrar_navegador()