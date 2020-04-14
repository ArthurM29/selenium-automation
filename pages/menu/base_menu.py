from pages.base_page import BasePage


class MenuItem:
    def __init__(self, name, locator, hover_dest, select_dest):
        self.name = name
        self.locator = locator
        self.hover_dest = hover_dest
        self.select_dest = select_dest


class BaseMenu(BasePage):
    _menu_container_locator = None
    _page_identifier_element = _menu_container_locator

    menu_items = {}

    def _get_menu_item(self, name):
        for menu_item in self.menu_items:
            if menu_item.name == name:
                return menu_item
        msg = f"'{self.__class__.__name__}' menu does not have menu item '{name}'."
        self.log.exception(msg)
        raise ValueError(msg)

    def hover_on(self, name):
        menu_item = self._get_menu_item(name)
        self.mouse_over(menu_item.locator)
        new_menu_class = menu_item.hover_dest
        if new_menu_class:
            return new_menu_class(self.driver)
        self.log.warning(f"Hovering on menu item '{self.__class__.__name__}.{name}' does not open a new menu.")

    def select(self, name):
        menu_item = self._get_menu_item(name)
        self.click_element_with_JS(menu_item.locator)
        new_page_class = menu_item.select_dest
        if new_page_class:
            return new_page_class(self.driver)
        self.log.warning(f"Clicking on menu item '{self.__class__.__name__}.{name}' does not open a new page.")
