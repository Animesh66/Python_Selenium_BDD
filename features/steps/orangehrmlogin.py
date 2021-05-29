import time
from behave import *
from selenium import webdriver


@given('I launch Chrome browser')
def step_launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('I open OrangeHRM homepage')
def step_open_orangehrm(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.set_page_load_timeout(10)


@when('Enter username "{user_name}" and password "{password}"')
def step_enter_credential(context, user_name, password):
    context.driver.find_element_by_id("txtUsername").send_keys(user_name)
    context.driver.find_element_by_id("txtPassword").send_keys(password)
    time.sleep(3)


@when('Click on Login button')
def step_click_login(context):
    context.driver.find_element_by_id("txtPassword").submit()


@then('User must successfully login to the Dashboard Page')
def step_verify_login(context):
    try:
        dashboard = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Login attempt failed"
    if dashboard == "Dashboard":
        context.driver.close()
        assert True, "Login Successful"
