from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest




@pytest.fixture()
def init():
    wd = webdriver.Firefox()
    wd.maximize_window()
    wd.implicitly_wait(5)
    yield wd
    wd.quit()


def test_open_s6(init):
    init.get("https://www.demoblaze.com/")
    galaxy= init.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy.click()
    title=init.find_element(By.XPATH, '//h2')
    assert title.text == 'Samsung galaxy s6'



