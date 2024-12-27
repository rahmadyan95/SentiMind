import os
import sys
import subprocess
import re
import emoji

class utils: 
    def __init__(self):
        pass
    
    def connection_check(self):
        try:
            # Try to connect to Google's website (www.google.com) using the `ping` command
            subprocess.check_output(["ping", "-c", "1", "www.google.com"])
            return True  # Internet connection is available
        except subprocess.CalledProcessError:
            return False  # No internet connection
        
    def count_elements(self, comments):
        if isinstance(comments, list):
            results = []
            for comment in comments:
                emoji_count = len(emoji.emoji_list(comment))
                url_count = len(re.findall(r'http\S+|www\.\S+', comment))
                char_count = len(comment)
                digit_count = len(re.findall(r'\d', comment))
                whitespace_count = len(re.findall(r'\s', comment))
                results.append((emoji_count, url_count, char_count, digit_count, whitespace_count))
            return results
        else:
            emoji_count = len(emoji.emoji_list(comments))
            url_count = len(re.findall(r'http\S+|www\.\S+', comments))
            char_count = len(comments)
            digit_count = len(re.findall(r'\d', comments))
            whitespace_count = len(re.findall(r'\s', comments))
            return emoji_count, url_count, char_count, digit_count, whitespace_count


    def clean_comment(self, comments):
        if isinstance(comments, list):
            results = []
            for comment in comments:
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

                # Tambahkan hasil pembersihan dan metrik ke hasil
                results.append((comment, emoji_count, url_count, char_count, digit_count, whitespace_count))
            return results
        else:
            # Menghitung komponen yang diperlukan
            emoji_count, url_count, char_count, digit_count, whitespace_count = self.count_elements(comments)

            # Remove emoji
            comments = emoji.replace_emoji(comments, replace='')

            # Remove URLs
            comments = re.sub(r'http\S+|www\.\S+', '', comments)

            # Remove special characters and digits
            comments = re.sub(r'[^\w\s]', '', comments)
            comments = re.sub(r'\d', '', comments)

            # Remove extra spaces
            comments = re.sub(r'\s+', ' ', comments).strip()

            return comments, emoji_count, url_count, char_count, digit_count, whitespace_count
