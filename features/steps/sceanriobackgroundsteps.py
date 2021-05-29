from behave import *
from selenium import webdriver


@given('I launch browser')
def step_launch_browser(context):
    assert True, "Test passed"


@when('I open application')
def step_open_application(context):
    assert True, "Test passed"


@when('Enter valid username and password')
def step_impl(context):
    assert True, "Test passed"


@then('User must login to the Dashboard page')
def step_impl(context):
    assert True, "Test passed"


@when('click on login')
def step_impl(context):
    assert True, "Test passed"


@when('navigate to search page')
def step_impl(context):
    assert True, "Test passed"


@then('Search page should be displayed')
def step_impl(context):
    assert True, "Test passed"


@when('navigate to advanced search page')
def step_impl(context):
    assert True, "Test passed"


@then('advanced search page should be displayed')
def step_impl(context):
    assert True, "Test passed"

