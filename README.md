# Асинхронный парсер документации PEP

## Описание проекта
Парсер документации Python c сайта https://www.python.org/
- текущие статусы всех стандартов PEP;
- авторы;
- количество PEP в каждом статусе.

## Технологии
- Python;
- Scrapy;

## Запуск парсера
- Cоздайте виртуальное окружение окружение:
    ```
    python -m venv venv
    ```
- Активируйте виртуальное окружение и установите зависимости:
    ```
    source venv/Scripts/activate
    python -r requirements.txt
    ```
- Для запуска парсера выполните команду:
    ```
    scrapy crawl pep
    ```
    
## Автор

[Yana Denisova](https://github.com/Yana-Denisova)
