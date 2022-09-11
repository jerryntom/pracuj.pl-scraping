from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from os import listdir

now = datetime.now()
currentDate = now.strftime("%d/%m/%Y")

# Please modify these variables
searchKeyword = "?"
searchLocation = "?"
senderAddress = "?"
senderKey = "?"
receiverAddress = "?"
adBlockPath = r"C:\Users\nazyw\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom"

# Set up AdBlock 
adBlockVersion = "\\" + listdir(adBlockPath)[0]
adBlockPath += adBlockVersion

# Set up Chrome 
chromeOptions = Options()
chromeOptions.add_experimental_option("detach", True)
chromeOptions.add_argument("load-extension=" + adBlockPath)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
driver.maximize_window()

# Go to site and show results according to given keyword and location
driver.get("https://pracuj.pl")
driver.switch_to.window(driver.window_handles[0])
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Akceptuj wszystkie')]"))).click()
advancedSearch = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div/div[3]/form/div[2]/button')

try:
    advancedSearch.click()
except Exception:
    advancedSearch = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div/div[3]/form/div[2]/button')
    advancedSearch.click()

try:
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Rozumiem')]"))).click()
except Exception:
    print("Can't find the button that contains 'Rozumiem'")

jobSearchKeyword = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/form/div[1]/div/div[1]/div[1]/div/input[1]')
jobSearchKeyword.send_keys(searchKeyword)
jobSearchPreferredLocation = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/form/div[1]/div/div[2]/div[1]/div/input[1]')
jobSearchPreferredLocation.send_keys(searchLocation)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[4]/form/div[1]/div/div[4]/div/button'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Pozostałe')]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[4]/form/div[3]/div[1]/div/ul/li[6]/div/div[2]/div[2]/fieldset[1]/ul/li[1]/label'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Pokaż oferty')]"))).click()

jobOffersList = []

# Collect each job offer from every available page of search result
while True:
    jobOffers = driver.find_elements(By.CLASS_NAME, "offer__info")

    for offer in jobOffers:
        jobLink = offer.find_element(By.CLASS_NAME, "offer-details__title-link")
        jobLinkHref = jobLink.get_attribute("href")
        jobTitle = jobLink.text
        jobCompanyName = offer.find_element(By.CLASS_NAME, "offer-company__name").text
        jobOfferListElement = {
            'link': jobLinkHref, 
            'job title': jobTitle, 
            'company name': jobCompanyName
            }
        jobOffersList.append(jobOfferListElement)
    
    # Last page detection
    try:
        nextPageButton = driver.find_element(By.CSS_SELECTOR, "li[class='pagination_element pagination_element--next']")
        nextPageButton.click()
    except Exception:
        print("End page of search result")
        break

# Create table from existing data and make export to Excel
df = pd.DataFrame(jobOffersList)
df.to_excel(r'jobOffers.xlsx', index=False)

# Build email message 
message = MIMEMultipart()
message['From'] = senderAddress
message['To'] = receiverAddress
message['Subject'] = searchKeyword + " pracuj.pl - " + searchLocation + " - najnowsze oferty pracy! " + currentDate 

# Attach jobOffers.xlsx
jobOffersExcelFile = MIMEBase('application', "octet-stream")
jobOffersExcelFile.set_payload(open("jobOffers.xlsx", "rb").read())
encoders.encode_base64(jobOffersExcelFile)
jobOffersExcelFile.add_header('Content-Disposition', 'attachment; filename="jobOffers.xlsx"')
message.attach(jobOffersExcelFile)

# Make secure connetion with smtp server through TLS and send a complete message
session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls() 
session.login(senderAddress, senderKey) 
messageAsText = message.as_string()
session.sendmail(senderAddress, receiverAddress, messageAsText)
session.quit()
print('Mail sent to ' + receiverAddress)

# Close the webdriver 
driver.quit()
