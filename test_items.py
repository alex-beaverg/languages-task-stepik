from selenium.webdriver.common.by import By


def test_check_add_to_basket_button(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.maximize_window()
    browser.get(link)

    list_with_one_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(list_with_one_button) > 0, "Button 'Add to basket' not found"
