# Coffee & WiFi App

Coffee & WiFi is a web application built with Flask that allows users to view and add cafes with information on WiFi speed, coffee quality, and power socket availability. The app uses Flask-WTF for form handling, Bootstrap-Flask for styling, and stores data in a CSV file.

---

## 🚀 **How to Use the Coffee & WiFi App**

### 1. **Clone the Repository**

```bash
git clone <repository-url>
cd coffee-and-wifi-app
```

### 2. **Create and Activate a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Run the Application**

```bash
python main.py
```

### 5. **Open in Browser**

Navigate to [**http://127.0.0.1:5000**](http://127.0.0.1:5000) to use the app.

### 6. **How to Use the App**

- **Home Page:** Click "Show Me!" to view the list of cafes.
- **View Cafes:** Shows all cafes with details on WiFi, coffee, and power.
- **Add a Cafe:** Go to [**http://127.0.0.1:5000/add**](http://127.0.0.1:5000/add) to add a new cafe.

---

## 📦 **Technologies Used**

- **Flask:** Web framework for Python.
- **Flask-WTF:** Form handling and validation.
- **Bootstrap-Flask:** Simplifies Bootstrap integration with Flask.
- **WTForms:** Provides built-in form validation.
- **Python CSV Module:** For reading and writing cafe data.
- **HTML & CSS:** Frontend structure and styling.
- **Bootstrap:** Provides responsive design and styling.

---

## 🎯 **Features**

- Display cafes with WiFi, coffee, and power information.
- Add new cafes with a simple form.
- Validate form inputs to ensure correct data.
- Consistent styling with Bootstrap.

---

## 🛠 **Possible Improvements I could make, or you could make**

- Add user authentication.
- Implement a database (e.g., SQLite) instead of a CSV file.
- Allow users to rate cafes or add reviews.

---

Enjoy finding the best cafes to work at with WiFi, coffee, and power availability!

