# this is a hook in BDD and this will be executed before each scenario
# Different type of hooks are before_step(), after_step(), before_scenario(), after_scenario()
# before_all(), after_all()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, driver):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.driver.maximize_window()


def after_step(context, step):
    print()


def after_scenario(context, driver):
    context.driver.quit()
