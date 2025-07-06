# DjangoProject — Task Manager

Проект создан в рамках курса **Python Advanced**.

## 📋 Описание
Это простой менеджер задач на Django, включающий категории, задачи и подзадачи. Реализована административная панель для управления.

## ⚙️ Используемые технологии
- Python 3.13
- Django 5.2
- SQLite

## 📂 Модели:
- `Category`: название категории (уникально)
- `Task`: заголовок, описание, дата создания, категория
- `SubTask`: заголовок, задача, флаг выполнения

## 🧠 Функциональность
- Панель администратора
- CRUD через Django Admin
- Уникальность по полям
- Удобный `__str__` и `Meta`

## 🔧 Запуск
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
