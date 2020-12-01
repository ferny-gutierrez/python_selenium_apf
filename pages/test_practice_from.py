from common.webdriver_factory import create_driver_instance
from pages.demoqa.practice_form import PracticeForm
try:
    driver = create_driver_instance('chrome')
    page = PracticeForm(driver,2)
    page.open()
    page.wait_until_loaded()
    page.set_first_name('Sandra')
    page.set_last_name('Gutierrez')
    page.set_email('ferny.gutierrez@gmail.com')
    page.set_gender('Female')
    page.set_mobile('3003656382')
    page.set_hobbies('1')
    page.set_subjects('Maths')
    page.set_subjects('Computer Science')
    page.set_current_address('CRA 17 # 136 - 73')
    page.set_date_of_birth("Nov 30 2020")
    page.set_state('NCR')
    page.set_city('Delhi')

finally:
    driver.close()