import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
DBPath = os.path.join(base_dir, "database.db")

class DatabaseUtils:
    def create_database(self):
        """
        Creates the database and tables if they don't already exist.
        """
        try:
            # Connect to the database (it will create the database if it doesn't exist)
            conn = sqlite3.connect(DBPath)
            cursor = conn.cursor()

            # Create the 'videos' table with video_id as primary key (using TEXT instead of INTEGER)
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS videos (
                    video_id TEXT PRIMARY KEY,  -- Use video_id as primary key (TEXT)
                    date TEXT NOT NULL,
                    title TEXT NOT NULL,
                    total_emoji_removed INTEGER,
                    total_url_removed INTEGER,
                    total_char_removed INTEGER,
                    total_digit_removed INTEGER,
                    total_whitespace_removed INTEGER
                )
            ''')

            # Create the 'comments' table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS comments (
                    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    video_id TEXT,
                    cleaned_comment TEXT,
                    FOREIGN KEY(video_id) REFERENCES videos(video_id)
                )
            ''')

            conn.commit()
            print("Database and tables are ready.")

        except sqlite3.Error as e:
            print(f"Error creating database or tables: {e}")
        finally:
            conn.close()

    def save_to_database(self, video_data):
        """
        Menyimpan data video dan komentar ke database dan mengembalikan data yang telah disimpan.

        Args:
            video_data (dict): Dictionary dengan struktur berikut:
                {
                    'video_id': str,  # Video ID passed as a string
                    'date': str,
                    'video_title': str,
                    'total_emoji_removed': int,
                    'total_url_removed': int,
                    'total_char_removed': int,
                    'total_digit_removed': int,
                    'total_whitespace_removed': int,
                    'comments_data': list[str]
                }

        Returns:
            dict: Data yang telah disimpan, termasuk video_id yang baru dimasukkan.
        """
        try:
            # Membuka koneksi ke database
            conn = sqlite3.connect(DBPath)
            cursor = conn.cursor()

            # Menyimpan data video dengan video_id sebagai primary key
            cursor.execute(''' 
                INSERT OR REPLACE INTO videos (
                    video_id, date, title, total_emoji_removed,
                    total_url_removed, total_char_removed, 
                    total_digit_removed, total_whitespace_removed
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                video_data['video_id'],  # video_id passed as a key
                video_data['date'],
                video_data['video_title'],
                video_data['total_emoji_removed'],
                video_data['total_url_removed'],
                video_data['total_char_removed'],
                video_data['total_digit_removed'],
                video_data['total_whitespace_removed']
            ))

            # Menyimpan komentar yang telah dibersihkan
            for comment in video_data['comments_data']:
                if comment:  # Make sure to skip empty comments
                    cursor.execute(''' 
                        INSERT INTO comments (video_id, cleaned_comment) VALUES (?, ?)
                    ''', (video_data['video_id'], comment))

            # Commit perubahan
            conn.commit()

            # Return data yang telah disimpan, termasuk video_id
            return {
                'video_id': video_data['video_id'],  # Include video_id as the key
                'date': video_data['date'],
                'video_title': video_data['video_title'],
                'total_emoji_removed': video_data['total_emoji_removed'],
                'total_url_removed': video_data['total_url_removed'],
                'total_char_removed': video_data['total_char_removed'],
                'total_digit_removed': video_data['total_digit_removed'],
                'total_whitespace_removed': video_data['total_whitespace_removed'],
                'comments_data': video_data['comments_data']
            }

        except sqlite3.Error as e:
            print(f"Terjadi kesalahan saat menyimpan data: {e}")
            return None

        finally:
            # Menutup koneksi database
            conn.close()
