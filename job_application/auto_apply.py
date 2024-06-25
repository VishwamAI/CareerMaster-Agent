import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def login_to_linkedin(driver, username, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

def search_jobs(driver, job_title, location):
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Search jobs']").send_keys(job_title)
    driver.find_element(By.XPATH, "//input[@placeholder='Search location']").send_keys(location)
    driver.find_element(By.XPATH, "//button[@aria-label='Search']").click()
    time.sleep(2)

def apply_to_job(driver):
    jobs = driver.find_elements(By.XPATH, "//a[@data-control-name='job_card']")
    for job in jobs:
        job.click()
        time.sleep(2)
        try:
            apply_button = driver.find_element(By.XPATH, "//button[@data-control-name='easy_apply']")
            apply_button.click()
            time.sleep(2)
            submit_button = driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
            submit_button.click()
            time.sleep(2)
        except:
            continue

def main():
    parser = argparse.ArgumentParser(description="Automate job applications on LinkedIn.")
    parser.add_argument("username", help="LinkedIn username")
    parser.add_argument("password", help="LinkedIn password")
    parser.add_argument("job_title", help="Job title to search for")
    parser.add_argument("location", help="Location to search for jobs in")
    args = parser.parse_args()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login_to_linkedin(driver, args.username, args.password)
    search_jobs(driver, args.job_title, args.location)
    apply_to_job(driver)
    driver.quit()

if __name__ == "__main__":
    main()
