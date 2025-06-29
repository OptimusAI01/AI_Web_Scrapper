# selenium allows us to control webbrowsers

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep

def scrap_website(website):
    print("Launching Chrome!")
    
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)
    
    try:
        driver.get(website)
        print("Page Loaded")
        html = driver.page_source
        sleep(5)
        return html
    finally:
        driver.quit()
        
def extract_body_content(html_content):
    bs = BeautifulSoup(html_content,"html.parser")
    body_content = bs.body
    if body_content:
        return str(body_content)
    return ""
    
def clean_body_contetn(body_content):
    bs = BeautifulSoup(body_content,"html.parser")
    
    for script_style in bs(["script","style"]):
        script_style.extract()
    
    cleaned_content = bs.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content
    
def split_dom_content(dom_contetn, max_length=6000):
    return [
        dom_contetn[i:i+max_length] for i in range(0,len(dom_contetn),max_length)
    ]