from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest




@pytest.fixture()
def init():
    wd = webdriver.Firefox()
    yield wd


def test_open_s6(init):
    init.get("https://www.demoblaze.com/")
    sleep(5000)
    galaxy= init.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    galaxy.click()


