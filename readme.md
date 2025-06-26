x# Contact Manager Web App

A simple CRUD web application for managing a list of contacts (Create, Read, Update, Delete).

##  Live Features

-  Add new contacts
-  Edit or delete existing contacts
-  Display contacts in a clean user interface
-  Responsive and modern front-end design (HTML/CSS/JS)
-  Built with Django (Python) and SQLite

## Technologies

- **Backend:** Django, SQLite
- **Frontend:** HTML, CSS, JavaScript (custom UI)
- **Other:** Bootstrap-like layout, Webflow templates

##  How to run locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/contact-manager.git
cd contact-manager
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      #  Linux/macOS
venv\Scripts\activate         #  Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

6. Access the app at: `http://127.0.0.1:8000/`

## Folder Structure

```
├── contacts/               # Django app
├── static/                 # CSS/JS assets
├── templates/              # HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

## Author

**Thienel Bocar Kane**  
📧 thienelkane7@gmail.com
📞 +221 77 427 32 81

---

## Screenshots of the app

![Contact list](images\contact_list.jpg)

![Contact register form](images\contact_register_form.jpg)
