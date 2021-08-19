# this is a hook in BDD and this will be executed before each scenario
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, driver):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.driver.maximize_window()
