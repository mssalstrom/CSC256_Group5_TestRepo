import WebInteractionModule


def validate_page_title(expected_title):
    page_title = WebInteractionModule.driver.title
    if page_title == expected_title:
        print(page_title)
        return True
    else:
        print('FALSE')
        return False

def is_element_present(locator_type, locator_value):
    pass

