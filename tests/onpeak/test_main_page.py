import pytest
import allure
from pages.onpeak import MainPage
from xpath_elements.onpeak.main_page_elements import MainPageElements, AboutPageElements, ServicesPageElements, \
    PortfolioPageElements, BlogPageElements, SeoElements, DelopmentElements, SupportElements, ContextElements, \
    TargetAdvertisingElements, DesignElements


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


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{AboutPageElements.TITLE}\"")
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


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{ServicesPageElements.TITLE}\"")
def test_move_to_other_page_to_services(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу "Услуги" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Услуги\""):
        page.menu_nav_item_services.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == ServicesPageElements.TITLE


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{PortfolioPageElements.TITLE}\"")
def test_move_to_other_page_to_portfolio(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу "Кейсы" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Кейсы\""):
        page.menu_nav_item_portfolio.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == PortfolioPageElements.TITLE


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{BlogPageElements.TITLE}\"")
def test_move_to_other_page_to_blog(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу "Блог" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Блог\""):
        page.menu_nav_item_blog.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == BlogPageElements.TITLE


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{SeoElements.TITLE}\"")
def test_move_to_other_page_to_seo(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу
    "Заказать продвижение сайтов в Яндекс и Google, компания Onpeak" """
    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Блог\""):
        page.seo.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == SeoElements.TITLE


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{DelopmentElements.TITLE}\"")
def test_move_to_other_page_to_development(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу
    "Создание и разработка сайта под ключ в Туле, компания Onpeak" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Блог\""):
        page.development.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == DelopmentElements.TITLE


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{SupportElements.TITLE}\"")
def test_move_to_other_page_to_support(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу
    "Обслуживание сайтов, оперативная техническая поддержка. Компания Onpeak Тула" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Блог\""):
        page.support.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == SupportElements.TITLE


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{ContextElements.TITLE}\"")
def test_move_to_other_page_to_context(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу
    "Заказать настройку и ведение контекстной рекламы, маркетинговое агентство Onpeak Тула" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Блог\""):
        page.context.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == ContextElements.TITLE


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{TargetAdvertisingElements.TITLE}\"")
def test_move_to_other_page_to_target_advertising(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу
    "Таргетированная реклама в социальных сетях, заказать и разместить рекламу в социальных сетях. ' \
            'Агентство Onpeak Тула" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Блог\""):
        page.target_advertising.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == TargetAdvertisingElements.TITLE


@allure.title(f"Проверка перехода на на другую страницу: с главной на \"{DesignElements.TITLE}\"")
def test_move_to_other_page_to_design(web_browser):
    """ При нажатии на кнопку "О компании" будет произведен переход на страницу
    "Разработка дизайна сайта под ключ, услуги по редизайну web- сайта. Компания Onpeak Тула" """

    with allure.step("Открываем главную страницу"):
        page = MainPage(web_browser, "https://www.onpeak.ru")
    with allure.step("Нажимаем на кнопку \"Блог\""):
        page.design.click()
        # wait until page loaded
        page.wait_page_loaded()
    with allure.step("Проверяем, что открылась необходимая страница"):
        assert page.title() == DesignElements.TITLE
