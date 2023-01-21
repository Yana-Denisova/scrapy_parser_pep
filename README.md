# Асинхронный парсер документации PEP


## Описание проекта
Парсер документации Python на базе фреймворка Scrapy c сайта https://www.python.org/
Проект позволяет получать список всех PEP для Python и информацию по статусам и количеству PEP, с записью полученной информации в файлы.


## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Автор](#автор)


## Технологии
- [Python](https://www.python.org/)
- [Scrapy](https://scrapy.org/)


## Использование

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/Yana-Denisova/scrapy_parser_pep.git
SSH: git clone git@github.com:Yana-Denisova/scrapy_parser_pep.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Для запуска парсера необходимо выполнить команду:
```bash
scrapy crawl pep
```

    
## Автор

[Денисова Яна](https://t.me/DenisovaYana)
