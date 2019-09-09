import time
from selenium import webdriver
from bs4 import BeautifulSoup
from watson_developer_cloud import AssistantV1
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

assistant = AssistantV1(
    version='2019-03-08',
    iam_apikey='EbXEGoY2tr9pd1xjqrhnxGzia9re6PHznJalJPYH5D3G',
    url='watson api'
)
assistant = AssistantV1(
    version='2019-03-08',
    username='apikey',
    password='rZK80-mSnvoWXPjaZ0m4Q6U0UFHafffSujheVkJrTD0N',
    url='watsonapi'
)
assistant.set_url('watsonapi')

driver = webdriver.Chrome('/home/kadri/Desktop/pycharm/chromedriver/chromedriver');
driver.get('https://customer.onlinelic.in/LICEPS/Login/begin.do?agent');
driver.find_element_by_name('{actionForm.userName}').send_keys('userName');
driver.find_element_by_name('{actionForm.password}').send_keys('paswd');
elems = driver.find_elements_by_xpath("/html/body/table/tbody/tr[3]/td/div/form/table/tbody/tr[4]/td/span")

for e in elems:
    cap=e.get_attribute('innerHTML').encode('ascii', 'ignore').decode('unicode_escape')
inStr={'name':cap}
In_json=json.dumps(inStr)
In_json=In_json.encode('ascii', 'ignore').decode('unicode_escape')
response = assistant.message(
    workspace_id='56c39968-a440-45c6-aba9-3b32c02f798f',
    input=dict(text=In_json)
).get_result()
print(In_json);
#print(response)
#print ("entities",response['output']['text'][0]);
#print ("output",response['entities']['value'][0])
Ct=response['output']['text'][0];
driver.find_element_by_name('{actionForm.qreply}').send_keys(Ct),
time.sleep(4)
driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/div/form/table/tbody/tr[7]/td/input").click();
time.sleep(6)

#driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[7]/td/input');
#question=BeautifulSoup("#loginForm > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > span:nth-child(1)").contents.copy();

#print(question);