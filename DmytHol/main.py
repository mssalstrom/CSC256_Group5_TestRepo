from WebInteractionModule import initialize_driver, navigate_to_url, find_element
from ValidationModule import validate_page_title, validate_element_presence
from ReportGenerationModule import log_result, capture_screenshot, initialize_report
if __name__ == "__main__":
    report = initialize_report()


    print(driver = initialize_driver('chrome'))
    # navigate_to_url('http://127.0.0.1:5000/')
    # print(validate_page_title('Hello')+ ' World!')


    # if validate_page_title("Sample Website"):
    #     search_box = find_element("ID", "searchBoxId")
    #     search_box.send_keys("Test")

    #     if validate_element_presence("ID", "resultId"):
    #         log_result("Search Functionality", "Pass", report)
    #     else:
    #         log_result("Search Functionality", "Fail", report)
    #         capture_screenshot("Search_Fail.png")
    # else:
    #     log_result("Navigation to Sample Website", "Fail", report)

    # driver.quit()

    # print(report)
