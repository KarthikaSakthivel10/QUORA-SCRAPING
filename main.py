from selenium import webdriver
import pandas as pd
from time import sleep

content = {'question': [], 'question_url': [], 'upvotes': []}

url = "https://www.quora.com/search?q=live%20chat%20tool"

webdrive = "/home/karthika/Downloads/chromedriver_linux64.zip"
browser = webdriver.Chrome(webdrive)
browser.get(url)

sleep(3)
for i in range(2, 99):
    try:
        question = browser.find_element('xpath', f'//*[@id="mainContent"]/div/div/div[2]/div[{i}]/span/a/div/div/div/div/span').text
        content['question'].append(question)
        url = browser.find_element('xpath', f'//*[@id="mainContent"]/div/div/div[2]/div[{i}]/span/a').get_attribute('href')
        content['question_url'].append(url)
        vote = browser.find_element('xpath',  f'//*[@id="mainContent"]/div/div/div[2]/div[{i}]/div/div[1]/div/div[2]/div/div/div/div[2]/div').click()
        sleep(2)
        a = browser.find_element('xpath', f'//*[@id="mainContent"]/div/div/div[2]/div[{i}]/div/div[1]/div/div[3]/div/span/span[4]/div').click()
        sleep(2)
        up = browser.find_element('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "qu-bold", " " ))]').text
        content['upvotes'].append(up)
        b = browser.find_element('xpath', '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/button').click()
    except:
        break

df = pd.DataFrame(content)
print(df)

df.to_csv("Quora Content.csv")
