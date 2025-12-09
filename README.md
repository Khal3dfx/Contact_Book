# 📇 Contact Book (CLI)

A simple and lightweight **command-line Contact Book application** written in **Python**.  
This project allows users to store, manage, search, update, and delete contacts using a clean and interactive CLI interface.

Contacts are saved automatically in a local JSON file, ensuring data persistence between program runs.

---

## ✨ Features
- Add new contacts (Name, Phone, Email)
- View all contacts (sorted alphabetically)
- Search contacts by name
- Update existing contact details
- Remove contacts
- Data persistence using JSON file storage
- Clean and easy-to-use terminal interface

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/Khal3dfx/Contact_Book.git
cd Contact_Book
```
2. Run the program:
```bash
python3 Contact_Book.py
```
3. Follow the on-screen menu:
- Press numbers 1–6 to navigate
- Enter contact details when prompted

## ✅ Requirements
- Python 3.x
- Works on Mac, Windows, and Linux
- Uses only Python standard libraries

## 📁 Project Structure
```bash
Contact_Book/
│
├── Contact_Book.py      # Main Python script
├── contacts.json        # Auto-created contact storage file
├── README.md            # Project documentation
└── .gitignore           # Git ignore rules
```
## 💾 Data Storage
- Contacts are stored in contacts.json
- The file is created automatically when you add the first contact
- User data is ignored from version control via .gitignore

## 🚀 Future Improvements
- Input validation for phone numbers and emails
- Export contacts to CSV
- Add favorites or tags
- Improve search functionality (partial match)
- Colorized CLI output

## 👤 Author
Khaled Fahad Al-Hamad

## 📝 Notes
- The application automatically saves contacts when you add, update, or remove them
- Designed as a beginner-friendly Python CLI project
- Ideal for learning file handling and data persistence
