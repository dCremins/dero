import sqlite3
import hashlib
import os

class DatabaseCommands:
    db = sqlite3.connect("dero.db")

    @classmethod
    def generate_salt(self) -> bytes:
        return os.urandom(32) 

    # encrypt password  
    @classmethod
    def hash_password(self, pwd:str, salt: bytes) -> str:
        hash_object = hashlib.sha512( salt + pwd.encode('utf-8') )
        hex_dig= hash_object.hexdigest()
        return hex_dig    

    @classmethod
    def create_users_table(self):
        cursor = self.db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(username VARCHAR(255),password VARCHAR(255), salt BINARY(32), name VARCHAR(255));""")


    @classmethod
    def create_user(self, username:str, password:str, name:str):
        cursor = self.db.cursor()
        salt = self.generate_salt()
        hashed = self.hash_password(password, salt)
        cursor.execute("INSERT INTO users (username, password, salt, name) VALUES(?, ?, ?, ?)",(username, hashed, salt, name))

    @classmethod
    def find_user(self, username:str) -> bool:
        cursor = self.db.cursor()
        result = cursor.execute("SELECT username FROM users WHERE username='?'",(username)).fetchone()
        return False if result is None else True

    @classmethod
    def validate_user(self, username:str, password:str) -> bool:
        cursor = self.db.cursor()
        result:tuple[str, bytes] = cursor.execute("SELECT password, salt FROM users WHERE username='?'",(username)).fetchone()
        if(result is None):
            return False
        else:
            user_password, salt = result
            return self.hash_password(password, salt) == user_password