import pytest
from playwright.sync_api import Page


URL = "https://practicetestautomation.com/practice-test-login/"


@pytest.fixture(scope="function")
def extract_credentials(page: Page):
    page.goto(URL)  # navigam la url-ul de login
    # extragem credentialele si stergem spatiile goale
    username = page.inner_text('#login > ul > li:nth-child(2) > b:nth-child(2)').strip()
    password = page.inner_text('#login > ul > li:nth-child(2) > b:nth-child(4)').strip()
    yield username, password


def test_login_successful(page: Page, extract_credentials):
    """
    #### Test case 1: Positive LogIn test

        Open page
        Type username student into Username field
        Type password Password123 into Password field
        Puch Submit button
        Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        Verify button Log out is displayed on the new page
    """
    page.goto(URL)
    username, password = extract_credentials
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Submit").click()
    assert page.query_selector("#error") is None
    assert "practicetestautomation.com/logged-in-successfully/" in page.url


def test_wrong_username(page: Page, extract_credentials):
    """
    #### Test case 2: Negative username test

    Open page
    Type username incorrectUser into Username field
    Type password Password123 into Password field
    Puch Submit button
    Verify error message is displayed
    Verify error message text is Your username is invalid!

    :param page:
    :return:
    """
    page.goto(URL)
    _, password = extract_credentials
    page.get_by_label("Username").fill("wrong username")
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Submit").click()
    assert "practicetestautomation.com/logged-in-successfully/" not in page.url
    assert page.query_selector("#error").inner_text() == "Your username is invalid!"


def test_wrong_password(page: Page, extract_credentials):
    """
    #### Test case 3: Negative password test

    Open page
    Type username student into Username field
    Type password incorrectPassword into Password field
    Puch Submit button
    Verify error message is displayed
    Verify error message text is Your password is invalid!
    """
    page.goto(URL)
    username, _ = extract_credentials
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill("wrong password")
    page.get_by_role("button", name="Submit").click()
    assert "practicetestautomation.com/logged-in-successfully/" not in page.url
    assert page.query_selector("#error").inner_text() == "Your password is invalid!"
