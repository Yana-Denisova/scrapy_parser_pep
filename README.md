# Асинхронный парсер документации PEP


## Описание проекта
Парсер документации Python на базе фреймворка Scrapy c сайта https://www.python.org/
- текущие статусы всех стандартов PEP;
- авторы;
- количество PEP в каждом статусе.


## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Автор](#автор)


## Технологии
- [Python](https://www.python.org/)
- [Scrapy](https://scrapy.org/)


## Использование
Склонируйте репозиторий  
Создайте виртуальное окружение 
```
python -m venv venv
```
Активируйте виртуальное окружение  
Установите зависимости 
```
pip install -r requirements.txt
```
Запустите парсинг
```
scrapy crawl pep
```

    
## Автор

[Денисова Яна](https://t.me/DenisovaYana)
