from pylenium.driver import Pylenium

def test_google(py: Pylenium):
    py.visit('https://google.com/')
    py.get("button[id='W0wltc']").click()
    py.get('[name="q"]').type('puppies')
    py.get('[name="btnK"]').submit()
    assert py.should().contain_title('puppies')
