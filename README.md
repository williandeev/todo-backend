<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,55:450a0a,100:b91c1c&height=180&section=header&text=TODO%20API&fontSize=56&fontColor=ffffff&fontAlignY=36&desc=REST%20API%20with%20Django%20and%20Django%20REST%20Framework&descSize=16&descAlignY=58" width="100%" alt="Todo API" />

<img src="https://img.shields.io/badge/Python-0d1117?style=for-the-badge&logo=python&logoColor=FFD43B" alt="Python" />
<img src="https://img.shields.io/badge/Django_4.2-0d1117?style=for-the-badge&logo=django&logoColor=44B78B" alt="Django 4.2" />
<img src="https://img.shields.io/badge/Django_REST_Framework-0d1117?style=for-the-badge&logo=django&logoColor=DC2626" alt="Django REST Framework" />
<img src="https://img.shields.io/badge/SQLite-0d1117?style=for-the-badge&logo=sqlite&logoColor=4FA3D9" alt="SQLite" />
<img src="https://img.shields.io/badge/License-MIT-b91c1c?style=for-the-badge&labelColor=0d1117" alt="MIT License" />

</div>

<br />

## ▍ABOUT

The backend half of a full-stack technical challenge: a CRUD REST API for a to-do list, built with Django and Django REST Framework. The Angular frontend lives in **[todolistangular](https://github.com/williandeev/todolistangular)**.

## ▍ENDPOINTS

Base URL: `http://localhost:8000/api/`

| Method | Route | Action |
| --- | --- | --- |
| `GET` | `/api/` | List all tasks |
| `POST` | `/api/` or `/api/create` | Create a task |
| `PUT` / `PATCH` | `/api/update/<id>/` | Update a task |
| `DELETE` | `/api/delete/<id>/` | Delete a task |

**Task payload**

```json
{
  "id": 1,
  "Title": "Study Angular",
  "Description": "Basic concepts",
  "Date": "2023-10-20",
  "Completed": false
}
```

CORS is open to all origins so the frontend can call the API during development.

## ▍GETTING STARTED

```bash
git clone https://github.com/williandeev/todo-backend.git
cd todo-backend/ToDoList

python -m venv .venv
# Windows:      .venv\Scripts\activate
# Linux/macOS:  source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API is now live at [http://localhost:8000/api/](http://localhost:8000/api/), and DRF's browsable API lets you test it right in the browser.

## ▍PROJECT STRUCTURE

```
ToDoList/
├── ToDoList/          # Project settings and root URLs
├── mainApp/           # ToDo model, serializer, generic views and routes
├── manage.py
└── requirements.txt
```

<br />

<div align="center">

<a href="https://github.com/williandeev"><img src="https://img.shields.io/badge/MADE_BY-WILLIAN_ROBSON-b91c1c?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117" alt="Made by Willian Robson" /></a>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:b91c1c,45:450a0a,100:0d1117&height=100&section=footer" width="100%" alt="" />
