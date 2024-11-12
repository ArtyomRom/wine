# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

  ## Как установить

  - ***Операционная система:***  
    - Windows 10 или новее
    - macOS 10.14 или новее
    - Linux (разные дистрибутивы)


  - ***Язык программирования:***  
    - Python 3.8 или новее


  - ***Установка окружения***
    - Создайте виртуальное окружение:
        ```bash
        python -m venv venv
        ```

    - Активируйте виртуальное окружение:
    
      - На Windows:
        ```bash
        venv\Scripts\activate
        ```
      - На macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

    - Установите зависимости:
        ```bash
        pip install -r requirements.txt
        ```

  - ***Склонируйте репозиторий***:
   [link](`https://github.com/ArtyomRom/Counting-clicks.git`)

  ## Запуск
В рабочую директорию необхдимо поместить excel файл

  ```bash
   python main.py wine.xlsx wine
  ```
wine.xlsx - файл эксель

wine - страница

  Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)
  - ## Пример данных для ecxel файла: 

    | Категория | Название | Сорт      | Цена     | Картинка | Акция       |
    |-----------|----------|-----------|----------|----------|-------------|
    | Данные 1  | Данные 2  | Данные 3 | Данные 4 | Данные 5 | Данные  6   |
    
  - ## Пример самого файла
    ![img_1.png](img_1.png)



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

 