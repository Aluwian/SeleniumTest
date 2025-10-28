import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    ("username", "password", "expected_message"), [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!\n×"),
        ("tomsmith", "12234445", "Your password is invalid!\n×")
    ]
)
def test_login_form(driver, username, password, expected_message):
    driver.get("https://the-internet.herokuapp.com/login")

    # Введение данных uaername
    username_input = driver.find_element(By.NAME, "username")
    username_input.clear()
    username_input.send_keys(username)

    # Введение данных password
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(password)

    # Нажатие кнопки login
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    message = driver.find_element(By.ID, "flash")
    assert message.text == expected_message

#
# def test_successful_login(driver):
#     data = {
#         "username": "tomsmith",
#         "password": "SuperSecretPassword!"
#     }
#
#     driver.get("https://the-internet.herokuapp.com/login")
#     username_input = driver.find_element(By.NAME, "username")
#     username_input.clear()
#     username_input.send_keys(data["username"])
#
#     password_input = driver.find_element(By.NAME, "password")
#     password_input.clear()
#     password_input.send_keys(data["password"])
#
#     submit_button = driver.find_element(By.TAG_NAME, "button")
#     submit_button.click()
#
#     success = driver.find_element(By.ID, "flash")
#     assert success.text == "You logged into a secure area!\n×"
#
#
# def test_unsuccessful_login(driver):
#     data = {
#         "username": "tomsmith",
#         "password": "12234445"
#     }
#
#     driver.get("https://the-internet.herokuapp.com/login")
#     username_input = driver.find_element(By.NAME, "username")
#     username_input.clear()
#     username_input.send_keys(data["username"])
#
#     password_input = driver.find_element(By.NAME, "password")
#     password_input.clear()
#     password_input.send_keys(data["password"])
#
#     submit_button = driver.find_element(By.TAG_NAME, "button")
#     submit_button.click()
#
#     success = driver.find_element(By.ID, "flash")
#     assert success.text == "Your password is invalid!\n×"
