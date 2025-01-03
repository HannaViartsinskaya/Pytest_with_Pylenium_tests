from pylenium.driver import Pylenium

def test_check_first_item (py: Pylenium):
    py.visit("https://practice.expandtesting.com/checkboxes")
    checkbox= py.get("input[id='checkbox1']")
    checkbox.click()
    checkbox2= py.get("input[id='checkbox2']")
    assert checkbox.should().be_checked()
    assert checkbox2.should().be_checked()

