from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.filter_dropdown = '.product_sort_container'
        self.inventory_item = '.inventory_item'
        self.inventory_item_name = '.inventory_item_name'
        self.inventory_item_price = '.inventory_item_price'

    def is_loaded(self):
        return "Products" in self.page.content()

    def select_filter_option(self, filter_option: str):
        self.page.select_option(self.filter_dropdown, label=filter_option)

    def get_product_names(self):
        product_elements = self.page.query_selector_all(self.inventory_item)
        return [element.query_selector(self.inventory_item_name).inner_text() for element in product_elements]

    def get_product_prices(self):
        product_elements = self.page.query_selector_all(self.inventory_item)
        return [float(element.query_selector(self.inventory_item_price).inner_text().strip('$')) for element in product_elements]