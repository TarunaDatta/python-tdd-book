from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard of a new to-do app. She checks it out in the browser
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test")

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box 

        # When she hits enter, the page updates and now the page lists 
        # "1. Buy peacock feathers" as an item in a todo list

        # There is still a text box inviting her to add another item. 
        # She enters "Use peacock feathers to create a fly"

        # Edith wonders if the list is persistent. She then notices a unique URL 
        # has been created for her -- explanatory text to that effect

        # She visits the url and her to-do list is still there

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main(warnings='ignore')