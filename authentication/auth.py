import sqlite3
import bcrypt
import argparse

# Database setup
def create_user_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# User registration
def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print(f"User {username} registered successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Username {username} is already taken.")
    conn.close()

# User login
def login_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        print(f"User {username} logged in successfully.")
        return True
    else:
        print("Error: Invalid username or password.")
        return False

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="User authentication system.")
    parser.add_argument('action', choices=['register', 'login'], help="Action to perform: register or login")
    parser.add_argument('username', help="Username")
    parser.add_argument('password', help="Password")
    args = parser.parse_args()

    create_user_table()

    if args.action == 'register':
        register_user(args.username, args.password)
    elif args.action == 'login':
        login_user(args.username, args.password)

if __name__ == '__main__':
    main()
