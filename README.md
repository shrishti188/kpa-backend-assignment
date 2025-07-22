# KPA Backend Assignment 

This is a Django-based RESTful API system to manage inspection and form data for Indian Railways' KPA Division. The project supports storing and retrieving information about bogie checksheets and wheel specifications.

## 📁 Features

- ✅ POST and GET endpoints for:
  - `BogieChecksheet` (with nested data: BMBC and Wheel Assembly)
  - `WheelSpecification`
- 🔒 CSRF-exempted API views for frontend/Postman compatibility
- 🛠️ Uses Django REST Framework
- 🔄 JSON-based input and output
- 🧪 Tested via Postman

---

## 🔧 Technologies Used

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL (used via pgAdmin)
- Postman (for API testing)

---

## 🧬 API Endpoints

### 1. **POST /api/forms/bogie-checksheet**
Creates a new bogie checksheet with nested `bmbcChecksheet` and `wheelAssembly`.

**Sample JSON body:**
```json
{
  "bmbcChecksheet": {
    "adjustingTube": "DAMAGED",
    "cylinderBody": "WORN OUT",
    "bracket": "OK"
  },
  "wheelAssembly": {
    "leftWheel": "FINE",
    "rightWheel": "SCRATCHED"
  },
  "remarks": "Needs attention on right wheel",
  "inspectedBy": "Inspector Sharma"
}
````

📤 **Response**: `201 Created` with saved data.

---

### 2. **POST /api/forms/wheel-specifications**

Adds a new wheel specification.

**Sample JSON:**

```json
{
  "wheelType": "Type A",
  "diameter": 950.0,
  "material": "Carbon Steel"
}
```

📤 **Response**: `201 Created`

---

### 3. **GET /api/forms/wheel-specifications**

Retrieves all saved wheel specs.

📥 **Response**:

```json
[
  {
    "id": 1,
    "wheelType": "Type A",
    "diameter": 950.0,
    "material": "Carbon Steel"
  },
  ...
]
```

---

## ⚙️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/kpa-form-backend.git
cd kpa-form-backend
```

2. Create virtual env & install dependencies:

```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start server:

```bash
python manage.py runserver
```

---

### 🔐 Default Superuser (for demo/testing)

Use the following credentials to log in at `/admin/`:

- **Username:** `admin`
- **Password:** `shri1234`


## 🧪 API Testing (Postman)

You can import the Postman collection ("https://shrishtisharma-971044.postman.co/workspace/SHRISHTI-SHARMA's-Workspace~6c32bc03-3b41-4468-87f5-5f6c20cb6972/collection/46939097-ce11bdd3-19f2-4b74-a01d-4331a31d6998?action=share&source=copy-link&creator=46939097") and test:

* ✅ POST request to add bogie-checksheet
* ✅ POST request to add wheel specs
* ✅ GET request to fetch wheel specs



## 📂 Project Structure

```
kpa_backend/
├── forms/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── kpa_backend/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── README.md
```

---

## 👤 Author

**Shrishti Sharma**

Email:(shrishtisharma59@gmail.com)


---

## 📃 License

This project is for academic and internal submission use only.

```

