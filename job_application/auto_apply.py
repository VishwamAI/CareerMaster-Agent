import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import argparse
import json
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from notifications.notifications import send_email_notification
import traceback
from dotenv import load_dotenv
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def login_to_linkedin(driver, username, password, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            logging.info(f"Login attempt {attempt + 1} - Navigating to LinkedIn login page.")
            driver.get("https://www.linkedin.com/login")

            logging.info("Waiting for username field to be present.")
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)

            logging.info("Entering password.")
            driver.find_element(By.ID, "password").send_keys(password)

            logging.info("Clicking submit button.")
            driver.find_element(By.XPATH, "//button[@type='submit']").click()

            logging.info("Waiting for user's profile link to confirm successful login.")
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/in/kasinadhsarma/')]")))

            logging.info("Successfully logged in to LinkedIn.")
            return
        except Exception as e:
            logging.error(f"Login attempt {attempt + 1} failed: {str(e)}")
            logging.error(traceback.format_exc())
            logging.info("Page source at the time of failure:")
            logging.info(driver.page_source)
            driver.save_screenshot(f"linkedin_login_failure_attempt_{attempt + 1}.png")

            # Check for CAPTCHA challenge
            if "Security Verification | LinkedIn" in driver.title:
                logging.info("CAPTCHA challenge detected. Please solve the CAPTCHA manually.")
                input("Press Enter after solving the CAPTCHA to continue...")
                continue

            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                raise Exception("Failed to log in to LinkedIn after multiple attempts.")

def search_jobs(driver, job_title, location, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            driver.get("https://www.linkedin.com/jobs/")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search jobs']"))).send_keys(job_title)
            driver.find_element(By.XPATH, "//input[@placeholder='Search location']").send_keys(location)
            driver.find_element(By.XPATH, "//button[@aria-label='Search']").click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'jobs-search__results-list')]")))
            logging.info("Successfully searched for jobs.")
            return
        except Exception as e:
            logging.error(f"Job search attempt {attempt + 1} failed: {str(e)}")
            logging.error(traceback.format_exc())
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                raise Exception("Failed to search for jobs after multiple attempts.")

def apply_to_job(driver, smtp_details, user_email, max_retries=3, delay=5):
    jobs = driver.find_elements(By.XPATH, "//a[@data-control-name='job_card']")
    for job in jobs:
        job.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-control-name='easy_apply']")))
        job_details = {
            "title": job.text,
            "link": job.get_attribute("href")
        }
        for attempt in range(max_retries):
            try:
                apply_button = driver.find_element(By.XPATH, "//button[@data-control-name='easy_apply']")
                apply_button.click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Submit application']"))).click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'application submitted')]")))
                send_email_notification(
                    to_email=user_email,
                    subject="Job Application Submitted",
                    message="Your job application has been successfully submitted.",
                    smtp_server=smtp_details['server'],
                    smtp_port=smtp_details['port'],
                    smtp_username=smtp_details['username'],
                    smtp_password=smtp_details['password']
                )
                job_details["status"] = "Submitted"
                logging.info(f"Successfully applied to job: {job_details['title']}")
                break
            except Exception as e:
                logging.error(f"Job application attempt {attempt + 1} failed: {str(e)}")
                logging.error(traceback.format_exc())
                if attempt < max_retries - 1:
                    time.sleep(delay)
                else:
                    send_email_notification(
                        to_email=user_email,
                        subject="Job Application Failed",
                        message=f"Failed to submit job application. Error: {str(e)}",
                        smtp_server=smtp_details['server'],
                        smtp_port=smtp_details['port'],
                        smtp_username=smtp_details['username'],
                        smtp_password=smtp_details['password']
                    )
                    job_details["status"] = "Failed"
                    logging.error(f"Failed to apply to job: {job_details['title']}. Error: {str(e)}")
                    logging.error(traceback.format_exc())

        # Log the job details to applied_jobs.json
        with open("applied_jobs.json", "r+") as file:
            applied_jobs = json.load(file)
            applied_jobs.append(job_details)
            file.seek(0)
            json.dump(applied_jobs, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Automate job applications on LinkedIn.")
    parser.add_argument("job_title", help="Job title to search for")
    parser.add_argument("location", help="Location to search for jobs in")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode")
    args = parser.parse_args()

    smtp_details = {
        'server': os.getenv('SMTP_SERVER'),
        'port': int(os.getenv('SMTP_PORT')),
        'username': os.getenv('SMTP_USERNAME'),
        'password': os.getenv('SMTP_PASSWORD')
    }

    linkedin_username = os.getenv('LINKEDIN_USERNAME')
    linkedin_password = os.getenv('LINKEDIN_PASSWORD')
    user_email = os.getenv('USER_EMAIL')

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    options.add_argument("--log-level=0")
    options.add_argument("--v=1")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        login_to_linkedin(driver, linkedin_username, linkedin_password)
        search_jobs(driver, args.job_title, args.location)
        apply_to_job(driver, smtp_details, user_email)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
