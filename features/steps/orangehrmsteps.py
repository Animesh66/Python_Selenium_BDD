from behave import *
from selenium import webdriver


@given('launch Chrome browser')
def step_launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('open orangeHRM homepage')
def step_open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.set_page_load_timeout(10)


@then('Verify that the logo present on the page')
def step_verify_logo(context):
    logo_status = context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert logo_status is True  # this is assertion method


@then('close the browser')
def step_close_browser(context):
    context.driver.close()


