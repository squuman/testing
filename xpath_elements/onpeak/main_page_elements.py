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

class AboutPageElements:
    """ Class keep xpath-s elements of about page """

    """ Main page title"""
    TITLE = "О компании"

    """ Selectors of elements """