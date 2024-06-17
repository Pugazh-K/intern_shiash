import mysql.connector
from tkinter import *
from tkinter import messagebox

# Database connection configuration
db_config = {
    'user': 'root',  # Default username for WAMPServer
    'password': '',  # Default password (empty string)
    'host': 'localhost',
    'database': 'user_auth',
}


# Connect to the database
def connect_to_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", f"Error: {err}")
        return None


def register():
    conn = connect_to_db()
    if conn is None:
        return

    cursor = conn.cursor()
    username = entry_username.get()


    cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        messagebox.showinfo("Registration Failed", "Username already exists. Please choose a different username.")
    else:
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()
        if password == confirm_password:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            messagebox.showinfo("Registration Successful", "User registered successfully!")
            clear_entries()
        else:
            messagebox.showwarning("Registration Failed", "Passwords do not match. Please try again.")

    cursor.close()
    conn.close()


def login():
    conn = connect_to_db()
    if conn is None:
        return

    cursor = conn.cursor()
    username = entry_username.get()

    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result:
        stored_password = result[0]
        password = entry_password.get()
        if password == stored_password:
            messagebox.showinfo("Login Successful", "Login successful!")
            clear_entries()
        else:
            messagebox.showwarning("Login Failed", "Incorrect password. Please try again.")
    else:
        messagebox.showwarning("Login Failed", "Username not found. Please register first.")

    cursor.close()
    conn.close()

def clear_entries():
    entry_username.delete(0, END)
    entry_password.delete(0, END)
    entry_confirm_password.delete(0, END)

def main():
    global entry_username, entry_password, entry_confirm_password

    root = Tk()
    root.title("Authentication System")

    Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    entry_username = Entry(root)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    entry_password = Entry(root, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    Label(root, text="Confirm Password:").grid(row=2, column=0, padx=10, pady=10)
    entry_confirm_password = Entry(root, show="*")
    entry_confirm_password.grid(row=2, column=1, padx=10, pady=10)

    Button(root, text="Register", command=register).grid(row=3, column=0, padx=10, pady=10)
    Button(root, text="Login", command=login).grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
