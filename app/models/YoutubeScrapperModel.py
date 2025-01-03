import pandas as pd
import re
import emoji
from googleapiclient.discovery import build
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
class YoutubeScrapperModel:
    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.DEVELOPER_KEY = os.getenv('YOUTUBE_API_KEY')
    
    def count_elements(self, comment):
        emoji_count = len(emoji.emoji_list(comment))
        url_count = len(re.findall(r'http\S+|www\.\S+', comment))
        char_count = len(comment)
        digit_count = len(re.findall(r'\d', comment))
        
        # Hitung jumlah whitespace (spasi, tab, baris baru)
        whitespace_count = len(re.findall(r'\s', comment))
        
        return emoji_count, url_count, char_count, digit_count, whitespace_count

    def clean_comment(self, comment):
        # Menghitung komponen yang diperlukan
        emoji_count, url_count, char_count, digit_count, whitespace_count = self.count_elements(comment)

        # Remove emoji
        comment = emoji.replace_emoji(comment, replace='')

        # Remove URLs
        comment = re.sub(r'http\S+|www\.\S+', '', comment)

        # Remove special characters and digits
        comment = re.sub(r'[^\w\s]', '', comment)
        comment = re.sub(r'\d', '', comment)

        # Remove extra spaces
        comment = re.sub(r'\s+', ' ', comment).strip()

        return comment, emoji_count, url_count, char_count, digit_count, whitespace_count

    def get_video_title(self, video_id):
        youtube = build(self.api_service_name, self.api_version, developerKey=self.DEVELOPER_KEY)
        request = youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()
        
        if response['items']:
            return response['items'][0]['snippet']['title']
        else:
            return "Unknown Title"

    def get_comments(self, youtube_link, max_comments):
        # Ensure the youtube_link is a list with one element if it's not already a list
        if isinstance(youtube_link, str):
            youtube_link = [youtube_link]

        pattern = r'(?:v=|\/|embed\/|youtu\.be\/|\/v\/|&v=)([a-zA-Z0-9_-]{11})'
        links = [re.search(pattern, link).group(1) for link in youtube_link if re.search(pattern, link)]
    
        video_ids = links
        youtube = build(self.api_service_name, self.api_version, developerKey=self.DEVELOPER_KEY)
        comments_data = []

        # Variabel untuk menghitung total jumlah yang dihapus
        total_emoji_count = 0
        total_url_count = 0
        total_char_count = 0
        total_digit_count = 0
        total_whitespace_count = 0

        for video_id in video_ids:
            # Get video title
            video_title = self.get_video_title(video_id)
            
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=max_comments
            )
            response = request.execute()

            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                # Get current date (without time)
                current_date = datetime.now().strftime('%d %B %Y')

                cleaned_comment, emoji_count, url_count, char_count, digit_count, whitespace_count = self.clean_comment(comment)
                
                # Akumulasi jumlah yang dihapus
                total_emoji_count += emoji_count
                total_url_count += url_count
                total_char_count += char_count
                total_digit_count += digit_count
                total_whitespace_count += whitespace_count

                comments_data.append(cleaned_comment)

        return {
            'platform' : 'Youtube',
            'date': current_date,
            'title': video_title,
            'scrapID' : video_ids[0], 
            'total_emoji_removed': total_emoji_count,
            'total_url_removed': total_url_count,
            'total_char_removed': total_char_count,
            'total_digit_removed': total_digit_count,
            'total_whitespace_removed': total_whitespace_count,
            'comments_data': comments_data
        }

# test = YoutubeScrapperModel()
# print(test.get_comments('https://www.youtube.com/watch?v=LFiJOqn_EYI',20))