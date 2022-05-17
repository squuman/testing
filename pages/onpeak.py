from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from xpath_elements.onpeak.main_page_elements import MainPageElements

class MainPage(WebPage):
    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)

    button_show_feedback_form = WebElement(xpath=MainPageElements.BUTTON_SHOW_FEEDBACK_FORM)
    button_show_feedback_form_in_header = WebElement(xpath=MainPageElements.BUTTON_SHOW_FEEDBACK_FROM_IN_HEADER)
    menu_nav = WebElement(xpath=MainPageElements.MENU_NAV)
    menu_nav_item_about = WebElement(xpath=MainPageElements.MENU_NAV_ITEM_ABOUT)
    menu_nav_item_services = WebElement(xpath=MainPageElements.MENU_NAV_ITEM_SERVICES)
    menu_nav_dropdown_about = WebElement(xpath=MainPageElements.MENU_NAV_DROPDOWN_ABOUT)
    menu_nav_dropdown_services = WebElement(css_selector=MainPageElements.MENU_NAV_DROPDOWN_SERVICES)
    form_feedback = WebElement(css_selector=MainPageElements.FORM_FEEDBACK)
    form_feedback_from_body = WebElement()