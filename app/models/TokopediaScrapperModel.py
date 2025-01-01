from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import sys
import os
import string
import random


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.utils.utils import utils


class TokopediaScrapperModel:
    def __init__(self):
        self.current_date = datetime.now().strftime('%d %B %Y')
        self.utilsinstances = utils()
        
    def generate_random_id(length=7):
        characters = string.ascii_letters + string.digits
        random_id = ''.join(random.choice(characters) for _ in range(7))
        return random_id
    def start_scrapping(self, url, pages):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-72zbc4")))

        # Variabel untuk menyimpan total metrik
        total_emoji_count = 0
        total_url_count = 0
        total_char_count = 0
        total_digit_count = 0
        total_whitespace_count = 0
        total_cleaned_text = []

        soup = BeautifulSoup(driver.page_source, "html.parser")

        product_name = soup.find('p', {'data-unify': 'Typography', 'class': 'css-1scsi0-unf-heading e1qvo2ff8'})
        current_date = datetime.now().strftime('%d %B %Y')
        scrapID = self.generate_random_id()
        for i in range(0, pages):
            
            containers = soup.find_all('article', attrs={'class': 'css-72zbc4'})
            
            for container in containers:
                review = container.find('span', attrs={'data-testid': 'lblItemUlasan'})

                if review:
                    raw_text = review.text
                    emoji_count, url_count, char_count, digit_count, whitespace_count = self.utilsinstances.count_elements(
                        raw_text
                    )
                    cleaned_text, *_ = self.utilsinstances.clean_comment(raw_text)

                    # Akumulasi total metrik
                    total_emoji_count += emoji_count
                    total_url_count += url_count
                    total_char_count += char_count
                    total_digit_count += digit_count
                    total_whitespace_count += whitespace_count

                    # Gabungkan teks yang sudah dibersihkan
                    total_cleaned_text.append(cleaned_text)

            time.sleep(2)
            try:
                driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
            except Exception as e:
                print("Tidak dapat menemukan tombol laman berikutnya:", e)
                break
            time.sleep(3)

        driver.close()

        # Gabungkan semua teks ulasan yang sudah dibersihkan menjadi satu string
        final_cleaned_text = " ".join(total_cleaned_text)

        # Return the data in the desired structure for further processing
        return {
            "platform" :'Tokopedia',
            'date': current_date,
            "title" : product_name.text,
            'scrapID' : scrapID, 
            "total_emoji_removed": total_emoji_count,
            "total_url_removed": total_url_count,
            "total_char_removed": total_char_count,
            "total_digit_removed": total_digit_count,
            "total_whitespace_removed": total_whitespace_count,
            "comments_data": total_cleaned_text   # This keeps the individual cleaned comments in a list
        }


# result = TokopediaScrapperModel().start_scrapping('https://www.tokopedia.com/sjfish2/gula-batok-aren-linggau-palembang/review', 1)
# print(result)
