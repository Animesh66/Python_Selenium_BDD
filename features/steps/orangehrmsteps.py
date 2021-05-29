from behave import *
from selenium import webdriver


@given('launch Chrome browser')
def step_launch_browser(context):
    raise NotImplementedError(u'STEP: Given launch Chrome browser')


@when('open orangeHRM homepage')
def step_open_homepage(context):
    raise NotImplementedError(u'STEP: When open orangeHRM homepage')


@then('Verify that the logo present on the page')
def step_verify_logo(context):
    raise NotImplementedError(u'STEP: Then Verify that the logo present on the page')


@then('close the browser')
def step_close_browser(context):
    raise NotImplementedError(u'STEP: Then close the browser')

