import sqlite3
import datetime

class SharedMemory:
    def __init__(self):
        self.conn = sqlite3.connect("shared_memory.db", check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            format TEXT,
            intent TEXT,
            timestamp TEXT,
            extracted_values TEXT,
            thread_id TEXT
        )
        ''')
        self.conn.commit()

    def log(self, source, format_, intent, extracted_values, thread_id="N/A"):
        timestamp = datetime.datetime.now().isoformat()
        self.conn.execute('''
            INSERT INTO memory (source, format, intent, timestamp, extracted_values, thread_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (source, format_, intent, timestamp, extracted_values, thread_id))
        self.conn.commit()
