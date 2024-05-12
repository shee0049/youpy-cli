from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def scrape_videos_by_channel(channel_name):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.youtube.com/@" + channel_name + "/videos")

    channel = driver.title
    driver.implicitly_wait(5)

    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "video-title-link")))

        video_titles = driver.find_elements(By.ID , "video-title-link")

        videos = []
        for title in video_titles:
            if (title.get_attribute("title") != None and title.get_attribute("href") != None):
                case = {
                    "title": title.get_attribute("title"),
                    "link": title.get_attribute("href")
                }
                videos.append(case)

        video_dict = {
            "channelname": channel,
            "videos": videos
        }

        return video_dict

    finally:
        driver.quit()

def scrape_videos_by_query(query):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    query = query.replace(' ', '+')

    driver.get("https://www.youtube.com/results?search_query=" + query)

    driver.implicitly_wait(5)

    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "video-title")))

        video_titles = driver.find_elements(By.ID , "video-title")

        videos = []
        for title in video_titles:
            if (title.get_attribute("title") != None and title.get_attribute("href") != None):
                case = {
                    "title": title.get_attribute("title"),
                    "link": title.get_attribute("href")
                }
                videos.append(case)

        video_dict = {
            "videos": videos
        }

        return video_dict

    finally:
        driver.quit()
