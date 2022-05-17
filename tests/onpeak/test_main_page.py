import pytest
import allure
from pages.onpeak import MainPage
from xpath_elements.onpeak.main_page_elements import MainPageElements, AboutPageElements


@allure.title("Проверка открытия главной страницы")
def test_open_main_page(web_browser):
    """ Проверка открытия главной страницы """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Ожидаем пока страница откроется"):
        page.wait_page_loaded()
    with allure.step("Проверяем, чтобы ожидаемый заголовок совпадал с реальным"):
        assert page.title() == MainPageElements.TITLE


@allure.title("Проверка открытия меню \"О компании\"")
def test_show_about_menu(web_browser):
    """ При наведении на кнопку "О компании" должно открыться меню информации о компании """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Наводим курсор мыши на кнопку \"О компании\""):
        page.menu_nav_item_about.move_to_element()
    with allure.step("Ожидаем пока появится меню"):
        page.menu_nav_dropdown_about.wait_until_not_visible()
    with allure.step("Проверяем, что меню открылось"):
        assert page.menu_nav_dropdown_about.is_visible() == True


@allure.title("Проверка открытия меню \"Услуги\"")
def test_show_services_menu(web_browser):
    """ При наведении на кнопку "Услуги" открывается меню услуг """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Наводим курсор мыши на кнопку \"Услуги\""):
        page.menu_nav_item_services.move_to_element()
    with allure.step("Ожидаем пока появится меню"):
        page.menu_nav_dropdown_services.wait_until_not_visible()
    with allure.step("Проверяем, что меню открылось"):
        assert page.menu_nav_dropdown_services.is_visible() == True


@allure.title("Проверка открытия формы обратной связи в заголовке страницы")
def test_open_feedback_form_from_header(web_browser):
    """ При нажатии на кнопку "Оставить заявку" в заголовке страницы открывается форма обратной связи """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку открытия формы"):
        page.button_show_feedback_form_in_header.click()
    with allure.step("Ожидаем открытия формы"):
        page.form_feedback.wait_until_not_visible()
    with allure.step("Проверяем открытие формы"):
        assert page.form_feedback.is_visible() == True


@allure.title("Проверка открытия формы обратной связи в теле страницы")
def test_open_feedback_form_from_body(web_browser):
    """ При нажатии на кнопку "Оставить заявку" в теле страницы открывается форма обратной связи """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку открытия формы"):
        page.button_show_feedback_form.click()
    with allure.step("Ожидаем открытия формы"):
        page.form_feedback.wait_until_not_visible()
    with allure.step("Проверяем открытие формы"):
        assert page.form_feedback.is_visible() == True


@allure.title("Проверка перехода на на другую страницу: с главной на \"О компании\"")
def test_move_to_other_page_to_about(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу "О компании" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"О компании\""):
        page.menu_nav_item_about.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == AboutPageElements.TITLE