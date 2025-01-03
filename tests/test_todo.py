import pytest
from pylenium.driver import Pylenium
from pylenium.element import Element, Elements



class TodoPage:
    def __init__(self, py: Pylenium):
        self.py=py

    def goto(self)-> 'TodoPage':
        self.py.visit('https://lambdatest.github.io/sample-todo-app/')
        return self

    def get_todo_by_name(self, name: str)-> Element:
        return self.py.getx(f"//*[text()='{name}']").parent().get("input")
    
    def get_all_checkboxes(self) -> Elements:
        return self.py.find("li[ng-repeat*='todo'] > input")
    
    def add_checkbox(self, name:str) -> "TodoPage":
        self.py.get("#sampletodotext").type(name)
        self.py.get("#addbutton").click()
        return self
    
@pytest.fixture
def page(py: Pylenium):
    return TodoPage(py).goto()
        

def test_first_item(page: TodoPage):
    checkbox=page.get_todo_by_name('First Item')
    checkbox.click()
    assert checkbox.should().be_checked()

def test_check_many_items(py: Pylenium, page: TodoPage):
    checkboxes=page.get_all_checkboxes()
    checkbox1, checkbox3=checkboxes[1], checkboxes[3]
    checkbox1.click()
    checkbox3.click()
    assert py.contains('3 of 5 remaining')

def test_check_all_checkboxes(py: Pylenium, page: TodoPage):
    for checkbox in page.get_all_checkboxes():
        checkbox.click()
    assert py.contains('0 of 5 remaining')

def test_add_new_item(py: Pylenium, page: TodoPage):
    page.add_checkbox("Finish the course")
    assert page.get_all_checkboxes().should().have_length(6)
    assert py.contains('6 of 6 remaining')
    