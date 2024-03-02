# def test_search_flight_to_athens(self):
#     # Navigate to the Gulliver website
#     self.gulliver_page.navigate_to_homepage()
#     # Find and click on the "טיסות" link in the navigation menu
#     flights_link_oneWay = WebDriverWait(self.gulliver_page.driver, 20).until(
#         EC.visibility_of_element_located((By.XPATH, "//*[@id='se_form_861']/fieldset[1]/div[2]/label"))
#     )
#     flights_link_oneWay.click()
#     time.sleep(3)

    # Find and click on the "הוספת טיסה" button
    # add_flight_button_addAthens = WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, "//*[@id='se_form_861']/fieldset[1]/div[2]/label"))
    # )
    # add_flight_button_addAthens.click()
    # time.sleep(3)

    # add_flight_button_listAthens = WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, "//*[@id='typeahead-931-2813-option-0']/div"))
    # )
    # add_flight_button_listAthens.click()

    # # Fill in the departure and arrival airports
    # departure_input = WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.visibility_of_element_located((By.ID, "mat-input-0"))
    # )
    # departure_input.send_keys("תל אביב")
    #
    # arrival_input = WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.visibility_of_element_located((By.ID, "mat-input-1"))
    # )
    # arrival_input.send_keys("אתונה")
    # time.sleep(5)

    # # Select the date
    # date_input = WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='תאריך הרכבת']"))
    # )
    # date_input.click()
    # date_picker = WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.visibility_of_element_located(
    #         (By.XPATH, "//div[@class='mat-calendar-body-cell-content' and text()='7']"))
    # )
    # date_picker.click()
    #
    # # Select the number of passengers
    # passengers_input = WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='מספר נוסעים']"))
    # )
    # passengers_input.clear()
    # passengers_input.send_keys("2")
    #
    # # Click on the search button
    # search_button = WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'חיפוש')]"))
    # )
    # search_button.click()
    #
    # # Assert that the search results page is loaded
    # WebDriverWait(self.gulliver_page.driver, 20).until(
    #     EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'תוצאות חיפוש')]"))
    # )