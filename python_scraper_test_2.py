import time 
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://twitter.com/yasoobkhalid")

state = ""
while state != "complete":
    print("loading not complete")
    time.sleep(randint(3, 5))
    state = driver.execute_script("return document.readyState")

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '[data-testid="tweet"]')))
except WebDriverException:
    print("Tweets did not appear!, Try setting headless=False to see what is happening")
        
bio = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserDescription"]').text
name, username = driver.find_element(By.CSS_SELECTOR,'div[data-testid="UserName"]').text.split('\n')
location = driver.find_element(By.CSS_SELECTOR,'span[data-testid="UserLocation"]').text
website = driver.find_element(By.CSS_SELECTOR,'a[data-testid="UserUrl"]').text
join_date = driver.find_element(By.CSS_SELECTOR,'span[data-testid="UserJoinDate"]').text
following = driver.find_element(By.XPATH, "//span[contains(text(), 'Following')]/ancestor::a/span").text
followers = driver.find_element(By.XPATH, "//span[contains(text(), 'Followers')]/ancestor::a/span").text

tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

for tweet in tweets:
    tag_text = tweet.find_element(By.CSS_SELECTOR,'div[data-testid="User-Names"]').text
    name, handle, _, timestamp = tag_text.split('\n')
    tweet_text = tweet.find_element(By.CSS_SELECTOR,'div[data-testid="tweetText"]').text
    retweet_count = tweet.find_element(By.CSS_SELECTOR,'div[data-testid="retweet"]').text
    like_count = tweet.find_element(By.CSS_SELECTOR,'div[data-testid="like"]').text
    reply_count = tweet.find_element(By.CSS_SELECTOR,'div[data-testid="reply"]').text
    print(name, handle)
    print(tweet_text)
    print("--------------")