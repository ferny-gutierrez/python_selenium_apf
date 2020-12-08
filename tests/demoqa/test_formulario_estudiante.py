import os

import pytest

from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.practice_form import PracticeForm

DATOS_FORMULARIO = [
    ('Sandra', 'Gutierrez', 'ferny.gutierrez@gmail.com', 'Female','3003656382',
     'Sports', ['Maths'], 'CRA 17 # 136 - 73',"Nov 30 2020"),
    ('Leonardo', 'Chaves', 'leonardoch2@gmail.com', 'Male', '3152258541',
     'Sports', ['Maths','Computer Science'], 'CRA 12 # 34 - 34', "Dic 30 2020")
]


@pytest.mark.parametrize("nombre, apellido, email, genero, celular, hobbies, subjects, address, birth", DATOS_FORMULARIO)
def test_uno(nombre, apellido, email, genero, celular, hobbies, subjects, address, birth):
    driver = create_driver_instance('chrome')
    driver.get('chrome://settings/')
    driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.75);')
    page = PracticeForm(driver, 20)
    page.abrir_pagina_web()
    page.esperar_hasta_que_se_cargue_elemento()
    page.set_first_name(nombre)
    page.set_last_name(apellido)
    page.set_email(email)
    page.set_gender(genero)
    page.set_mobile(celular)
    page.set_hobbies(hobbies)
    for subject in subjects:
        page.set_subjects(subject)
    page.set_current_address(address)
    page.set_date_of_birth(birth)
    file_path = os.path.join(ROOT_DIR, '.gitignore')
    # page.set_file("C:\\Users\\Usuario\\Documents\\bootcamptest\\2020_Python_Selenium-main\\.gitignore")
    # page.set_state('NCR')
    # page.set_city('Delhi')
    driver.close()
