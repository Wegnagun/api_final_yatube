# api_final
api final

### Установка: 
#### Windows
`python -m venv venv `

`venv/Scripts/activate `

`python -m pip install --upgrade pip `

`pip install -r requirements.txt `

#### Linux
`python3 -m venv venv `

`source venv/bin/activate `

`python -m pip install --upgrade pip `

`pip install --upgrade setuptools ` опционально...

`pip install -r requirements.txt `

### Запуск
Перейдити в дирректорию yatube_api и выполните миграции:

`python manage.py migrate `

Запустите сервер:

`python manage.py runserver`