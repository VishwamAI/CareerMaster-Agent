import time
import argparse
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from notifications.notifications import send_email_notification

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

def apply_to_job(driver, smtp_details, user_email):
    jobs = driver.find_elements(By.XPATH, "//a[@data-control-name='job_card']")
    for job in jobs:
        job.click()
        time.sleep(2)
        job_details = {
            "title": job.text,
            "link": job.get_attribute("href")
        }
        try:
            apply_button = driver.find_element(By.XPATH, "//button[@data-control-name='easy_apply']")
            apply_button.click()
            time.sleep(2)
            submit_button = driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
            submit_button.click()
            time.sleep(2)
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
        except Exception as e:
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

        # Log the job details to applied_jobs.json
        with open("applied_jobs.json", "r+") as file:
            applied_jobs = json.load(file)
            applied_jobs.append(job_details)
            file.seek(0)
            json.dump(applied_jobs, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Automate job applications on LinkedIn.")
    parser.add_argument("username", help="LinkedIn username")
    parser.add_argument("password", help="LinkedIn password")
    parser.add_argument("job_title", help="Job title to search for")
    parser.add_argument("location", help="Location to search for jobs in")
    parser.add_argument("user_email", help="User email for notifications")
    parser.add_argument("smtp_server", help="SMTP server for sending email notifications")
    parser.add_argument("smtp_port", type=int, help="SMTP port for sending email notifications")
    parser.add_argument("smtp_username", help="SMTP username for sending email notifications")
    parser.add_argument("smtp_password", help="SMTP password for sending email notifications")
    args = parser.parse_args()

    smtp_details = {
        'server': args.smtp_server,
        'port': args.smtp_port,
        'username': args.smtp_username,
        'password': args.smtp_password
    }

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login_to_linkedin(driver, args.username, args.password)
    search_jobs(driver, args.job_title, args.location)
    apply_to_job(driver, smtp_details, args.user_email)
    driver.quit()

if __name__ == "__main__":
    main()
