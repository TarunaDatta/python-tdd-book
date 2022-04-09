from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the homepage and accidentally tries to submit 
        # an empty list item. She then hits ENTER on the empty input box
        
        # The home page refreshes and there is an error message saying that
        # the list items cannot be blank

        # Perversely, she tries to submit a second empty list item.

        # She recieves a similar warning on the list page 

        # And she can correct it by filling some text in
        self.fail('Write the test!')