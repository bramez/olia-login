from behave import *

from tests.feature.pageobjects.login_page import LoginPage
from tests.feature.pageobjects.profile_page import ProfilePage

use_step_matcher("re")


@given("I am on the login page")
def step_impl(context):
    context.login_page = LoginPage(context.driver)


@when("I enter valid credentials")
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.write_username("olia")
    context.login_page.write_password("olia88")


@step("I click on the login button")
def step_impl(context):
    context.login_page.click_submit()


@then("I should be redirected to the profile page")
def step_impl(context):
    context.profile_page = ProfilePage(context.driver)
    assert context.profile_page.is_user_profile_name_displayed(), "The element you are looking for is not displayed"
