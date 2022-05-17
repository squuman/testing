class MainPageElements:
    """ Class keep xpath-s elements of main page """

    """ Main page title"""
    TITLE = "Onpeak - агентство интернет маркетинга в Туле"

    """ Selectors of elements """
    BUTTON_SHOW_FEEDBACK_FORM = "//button[contains(@class, 'op-button') and contains(@class, 'modal-window-form')]"
    MENU_NAV = "//div[@class='menu-nav__fixed-items']"
    MENU_NAV_ITEM_ABOUT = "//a[contains(@href,'/about/')]"
    MENU_NAV_ITEM_SERVICES = "//a[contains(@href, '/services/')]"
    MENU_NAV_ITEM_PORTFOLIO = "//a[@href='/portfolio/']"
    MENU_NAV_ITEM_BLOG = "//a[@href='/blog/']"
    BUTTON_SHOW_FEEDBACK_FROM_IN_HEADER = "//input[@class='op-button-header-form modal-window-form']"
    MENU_NAV_DROPDOWN_ABOUT = "//div[contains(@class, 'menu-nav__fixed-items-two')]"
    MENU_NAV_DROPDOWN_SERVICES = ".grey-line"
    FORM_FEEDBACK = '#comp_d2d38cbf7a6bc1ecd2c8eb0224dd05f6'
    SEO = "//div[@text='SEO-продвижение']"
    DEVELOPMENT = "//div[@text='Разработка']"
    SUPPORT = "//div[@text='Поддержка']"
    CONTEXT = "//div[@text='Контекстная реклама']"
    TARGET_ADVERTISING = "//div[@text='Таргетированная реклама']"
    DESIGN = "//div[@text='Дизайн']"


class AboutPageElements:
    """ Class keep xpath-s elements of about page """

    """ Main page title"""
    TITLE = "О компании"


class ServicesPageElements:
    """ Class keep xpath-s elements of services page """

    """ Main page title"""
    TITLE = "Услуги маркетингового агентства Onpeak"


class PortfolioPageElements:
    """ Class keep xpath-s elements of portfolio page """

    """ Main page title"""
    TITLE = "Кейсы компании Onpeak"


class BlogPageElements:
    """ Class keep xpath-s elements of blog page """

    """ Main page title"""
    TITLE = "Блог маркетингового агентства Onpeak"


class SeoElements:
    TITLE = 'Заказать продвижение сайтов в Яндекс и Google, компания Onpeak'


class DelopmentElements:
    TITLE = 'Создание и разработка сайта под ключ в Туле, компания Onpeak'


class SupportElements:
    TITLE = 'Обслуживание сайтов, оперативная техническая поддержка. Компания Onpeak Тула'


class ContextElements:
    TITLE = 'Заказать настройку и ведение контекстной рекламы, маркетинговое агентство Onpeak Тула'


class TargetAdvertisingElements:
    TITLE = 'Таргетированная реклама в социальных сетях, заказать и разместить рекламу в социальных сетях. ' \
            'Агентство Onpeak Тула'


class DesignElements:
    TITLE = 'Разработка дизайна сайта под ключ, услуги по редизайну web- сайта. Компания Onpeak Тула'
