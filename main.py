from WebInteractionModule import initialize_driver
from WebInteractionModule import navigate_to_url
from ValidationModule import validate_page_title


driver = initialize_driver('chrome')
navigate_to_url('https://www.wikipedia.com')
validate_page_title('Wikipdia')

