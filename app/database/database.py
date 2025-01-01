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

            # Create the 'videos' table with scrapID as primary key (using TEXT instead of INTEGER)
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS videos (
                    scrapID TEXT PRIMARY KEY,
                    platform TEXT NOT NULL,
                    title TEXT NOT NULL,
                    date TEXT NOT NULL,
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
                    ScrapID TEXT,
                    cleaned_comment TEXT,
                    FOREIGN KEY(scrapID) REFERENCES videos(scrapID)
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
                    'scrapID': str,  # Video ID passed as a string
                    'date': str,
                    'title': str,
                    'total_emoji_removed': int,
                    'total_url_removed': int,
                    'total_char_removed': int,
                    'total_digit_removed': int,
                    'total_whitespace_removed': int,
                    'comments_data': list[str]
                }

        Returns:
            dict: Data yang telah disimpan, termasuk scrapID yang baru dimasukkan.
        """
        try:
            # Membuka koneksi ke database
            conn = sqlite3.connect(DBPath)
            cursor = conn.cursor()

            # Menyimpan data video dengan scrapID sebagai primary key
            cursor.execute(''' 
                INSERT OR REPLACE INTO videos (
                    scrapID, platform ,title,date,  total_emoji_removed,
                    total_url_removed, total_char_removed, 
                    total_digit_removed, total_whitespace_removed
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                video_data['scrapID'],  # scrapID passed as a key
                video_data['platform'],
                video_data['title'],
                video_data['date'],
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
                        INSERT INTO comments (scrapID, cleaned_comment) VALUES (?, ?)
                    ''', (video_data['scrapID'], comment))

            # Commit perubahan
            conn.commit()

            # Return data yang telah disimpan, termasuk scrapID
            return {
                'scrapID': video_data['scrapID'],  # Include scrapID as the key
                'date': video_data['date'],
                'title': video_data['title'],
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

    def GetData(self):
        conn = sqlite3.connect(DBPath)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT v.platform,v.scrapID, v.title, v.date
            FROM videos v
            LEFT JOIN comments c ON v.scrapID = c.scrapID
            GROUP BY v.scrapID
        ''')
        rows = cursor.fetchall()

        conn.close()
        return rows
    
    def fetch_data_by_scrapID(self, scrapID):
        """
        Mengambil data video dan seluruh komentar yang terkait dengan scrapID tertentu.
        """
        # Koneksi ke database
        connection = sqlite3.connect(DBPath)  # Ganti dengan nama database Anda
        cursor = connection.cursor()

        # Query untuk mengambil data video dan komentar
        cursor.execute('''
            SELECT 
                v.scrapID, 
                v.platform, 
                v.title, 
                v.date, 
                v.total_emoji_removed, 
                v.total_url_removed, 
                v.total_char_removed, 
                v.total_digit_removed, 
                v.total_whitespace_removed, 
                c.cleaned_comment
            FROM 
                videos v
            LEFT JOIN 
                comments c 
            ON 
                v.scrapID = c.scrapID
            WHERE 
                v.scrapID = ?
        ''', (scrapID,))

        # Mengambil hasil query
        rows = cursor.fetchall()

        # Tutup koneksi database
        connection.close()

        # Mengolah hasil query
        video_data = {
            "scrapID": scrapID,
            "platform": rows[0][1] if rows else None,  # Pastikan data video ada
            "title": rows[0][2] if rows else None,
            "date": rows[0][3] if rows else None,
            "total_emoji_removed": rows[0][4] if rows else None,
            "total_url_removed": rows[0][5] if rows else None,
            "total_char_removed": rows[0][6] if rows else None,
            "total_digit_removed": rows[0][7] if rows else None,
            "total_whitespace_removed": rows[0][8] if rows else None,
            "comments": [row[9] for row in rows if row[9] is not None]  # Ambil hanya komentar
        }

        return video_data

        

# cls = DatabaseUtils()
# print(cls.fetch_data_by_scrapID('i_UgZjGFV9o'))
