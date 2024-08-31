from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)
driver.maximize_window()

# Test Case: TC_Login_01 - Successful Employee login to OrangeHRM portal
def test_login_successful():
    driver.get(url)
    
    # Enter username and password
    driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    
    # Click on the login button
    driver.find_element(By.ID, "btnLogin").click()
    
    # Check if login was successful
    try:
        welcome_text = driver.find_element(By.ID, "welcome").text
        assert "Welcome" in welcome_text
        print("Test Case TC_Login_01 Passed: User logged in successfully.")
    except NoSuchElementException:
        print("Test Case TC_Login_01 Failed: Login unsuccessful.")
    
    time.sleep(2)  # Optional sleep for visual confirmation

# Test Case: TC_Login_02 - Invalid Employee login to OrangeHRM portal
def test_login_invalid_password():
    driver.get(url)
    
    # Enter username and incorrect password
    driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    driver.find_element(By.ID, "txtPassword").send_keys("InvalidPassword")
    
    # Click on the login button
    driver.find_element(By.ID, "btnLogin").click()
    
    # Check for error message
    try:
        error_message = driver.find_element(By.ID, "spanMessage").text
        assert "Invalid credentials" in error_message
        print("Test Case TC_Login_02 Passed: Correct error message displayed.")
    except NoSuchElementException:
        print("Test Case TC_Login_02 Failed: Error message not displayed.")
    
    time.sleep(2)

# Test Case: TC_PIM_01 - Add a new employee in the PIM module
def test_add_employee():
    driver.get(url)
    
    # Assuming the user is already logged in
    driver.find_element(By.ID, "menu_pim_viewPimModule").click()
    driver.find_element(By.ID, "menu_pim_addEmployee").click()
    
    # Fill in employee details
    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    
    # Save the employee
    driver.find_element(By.ID, "btnSave").click()
    
    # Verify that employee is added
    try:
        success_message = driver.find_element(By.CSS_SELECTOR, ".message.success").text
        assert "Successfully Saved" in success_message
        print("Test Case TC_PIM_01 Passed: Employee added successfully.")
    except NoSuchElementException:
        print("Test Case TC_PIM_01 Failed: Employee not added.")
    
    time.sleep(2)

# Test Case: TC_PIM_02 - Edit an existing employee in the PIM module
def test_edit_employee():
    driver.get(url)
    
    # Assuming the user is already logged in
    driver.find_element(By.ID, "menu_pim_viewEmployeeList").click()
    
    # Click on an employee name to edit (assuming first employee in the list)
    driver.find_element(By.LINK_TEXT, "John Doe").click()
    
    # Edit employee details
    driver.find_element(By.ID, "btnSave").click()
    driver.find_element(By.ID, "personal_txtEmpFirstName").clear()
    driver.find_element(By.ID, "personal_txtEmpFirstName").send_keys("Johnny")
    driver.find_element(By.ID, "btnSave").click()
    
    # Verify that employee is edited
    try:
        success_message = driver.find_element(By.CSS_SELECTOR, ".message.success").text
        assert "Successfully Updated" in success_message
        print("Test Case TC_PIM_02 Passed: Employee edited successfully.")
    except NoSuchElementException:
        print("Test Case TC_PIM_02 Failed: Employee not edited.")
    
    time.sleep(2)

# Test Case: TC_PIM_03 - Delete an existing employee in the PIM module
def test_delete_employee():
    driver.get(url)
    
    # Assuming the user is already logged in
    driver.find_element(By.ID, "menu_pim_viewEmployeeList").click()
    
    # Select the checkbox for an employee (assuming first employee in the list)
    driver.find_element(By.NAME, "chkSelectRow[]").click()
    
    # Click delete
    driver.find_element(By.ID, "btnDelete").click()
    
    # Confirm deletion
    driver.find_element(By.ID, "dialogDeleteBtn").click()
    
    # Verify that employee is deleted
    try:
        success_message = driver.find_element(By.CSS_SELECTOR, ".message.success").text
        assert "Successfully Deleted" in success_message
        print("Test Case TC_PIM_03 Passed: Employee deleted successfully.")
    except NoSuchElementException:
        print("Test Case TC_PIM_03 Failed: Employee not deleted.")
    
    time.sleep(2)

# Run all tests
test_login_successful()
test_login_invalid_password()
test_add_employee()
test_edit_employee()
test_delete_employee()

# Close the browser window
driver.quit()
