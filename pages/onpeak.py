from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from xpath_elements.onpeak.main_page_elements import MainPageElements

""" Class of keep web elements of web-page """
class MainPage(WebPage):
    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)

    # feedback form
    form_feedback = WebElement(css_selector=MainPageElements.FORM_FEEDBACK)
    form_feedback_from_body = WebElement()
    button_show_feedback_form = WebElement(xpath=MainPageElements.BUTTON_SHOW_FEEDBACK_FORM)
    button_show_feedback_form_in_header = WebElement(xpath=MainPageElements.BUTTON_SHOW_FEEDBACK_FROM_IN_HEADER)

    # menu
    menu_nav = WebElement(xpath=MainPageElements.MENU_NAV)
    menu_nav_item_about = WebElement(xpath=MainPageElements.MENU_NAV_ITEM_ABOUT)
    menu_nav_item_services = WebElement(xpath=MainPageElements.MENU_NAV_ITEM_SERVICES)
    menu_nav_item_portfolio = WebElement(xpath=MainPageElements.MENU_NAV_ITEM_PORTFOLIO)
    menu_nav_item_blog = WebElement(xpath=MainPageElements.MENU_NAV_ITEM_BLOG)
    menu_nav_dropdown_about = WebElement(xpath=MainPageElements.MENU_NAV_DROPDOWN_ABOUT)
    menu_nav_dropdown_services = WebElement(css_selector=MainPageElements.MENU_NAV_DROPDOWN_SERVICES)

    # services
    seo = WebElement(xpath=MainPageElements.SEO)
    development = WebElement(xpath=MainPageElements.DEVELOPMENT)
    support = WebElement(xpath=MainPageElements.SUPPORT)
    context = WebElement(xpath=MainPageElements.CONTEXT)
    target_advertising = WebElement(xpath=MainPageElements.TARGET_ADVERTISING)
    design = WebElement(xpath=MainPageElements.DESIGN)