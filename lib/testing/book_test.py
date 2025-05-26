from book import Book

import io
import sys

class TestBook:

    def test_has_title_and_page_count(self):

        book = Book("And Then There Were None", 272)
        assert(book.page_count == 272)
        assert(book.title == "And Then There Were None")

    def test_requires_int_page_count(self):
        
        book = Book("And Then There Were None", 272)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "page_count must be an integer\n"

    def test_can_turn_page(self):
        
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")