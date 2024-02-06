# Invest Bot

## Содержание
- [Invest Bot](#invest-bot)
  - [Содержание](#содержание)
  - [Технический стек](#технический-стек)
  - [БД](#бд)
    - [Модели БД](#модели-бд)
      - [Пользователи (Users)](#пользователи-users)
      - [Токен (Tokens)](#токен-tokens)
      - [Проект (Projects)](#проект-projects)
    - [Таблицы связей](#таблицы-связей)
      - [](#)
  - [Архитектура проекта](#архитектура-проекта)


## Технический стек

- Бэкенд
    * ЯП - `Python 3.11`
    * Пакетный менедженр `Poetry`
    * Фреймворк `FastAPI`
    * Работа с БД с помощью `SQLAlchemy`
    * БД - `SQLite3` -> `PostgreSQL`
- Фронтенд
    * Telegram-бот `Python3.9` + `aiogram2`
    * Web App с использованием `React`
- Разворачивание проекта
    * `docker-compose`


## БД

### Модели БД

#### Пользователи (Users)

|      Свойство       |   Тип данных   | Описание                           |
|:-------------------:|:--------------:|------------------------------------|
|        `id`         | uuid (Primary) | Идентификатор инвестора            |
| `registration_date` |    datetime    | Дата регистрации (utc timestamp)   |
|       `level`       |      int       | Уровень инвестора                  |
|       `tg_id`       |      int       | Телеграм id                        |
|       `email`       |      str       | Email                              |
|   `phone_number`    |      str       | Номер телефона                     |
|      `surname`      |      str       | Фамилия                            |
|       `name`        |      str       | Имя                                |
|    `middle_name`    |   str / None   | Отчество                           |
|  `donation_amount`  |      int       | Количество пожертвований в проекты |
| `investment_amount` |      int       | Количество инвестиций в проекты    |
|       `photo`       |   (?) / None   | Фото профиля                       |
<!--- Пока страна и язык не важны. 
|       `lang`        |    str     | Язык интерфейса                  |
|      `country`      |    str     | Страна                           |
-->
   (?) - пока не определились

#### Токен (Tokens)

|   Свойство   |   Тип данных   | Описание                                                   |
|:------------:|:--------------:|------------------------------------------------------------|
|     `id`     | uuid (Primary) | Идентификатор токена                                       |
|   `level`    |      int       | Уровень токена                                             |
| `project_id` |      uuid      | Идентификатор проекта (Внешний ключ к таблице Projects.id) |
|  `user_id`   |   uuid/None    | Идентификатор инвестора (Внешний ключ к таблице Users.id)  |
|   `weight`   |      int       | Вес токена для формирования уровня инвестора               |
|   `price`    |      int       | Цена токена (цена будет указана в копейках/центах и т.п.)  |
<!--- Реализация цвета токена уходит на фронт
|   `color`    |    str     | HEX представление цвета (?)                  |
-->

#### Проект (Projects)

|      Свойство       |   Тип данных   | Описание                                         |
|:-------------------:|:--------------:|--------------------------------------------------|
|        `id`         | uuid (Primary) | Идентификатор проекта                            |
| `registration_date` |    datetime    | Дата создания проекта (utc timestamp)            |
|       `level`       |      int       | Уровень проекта                                  |
|       `cover`       |      (?)       | Обложка проекта (ссылка на файл)                 |
|    `short_info`     |      str       | Краткая информация о проекте                     |
|       `stage`       |    str/None    | Стадия проекта (на усмотрение владельца)         |
|     `full_info`     |      str       | Полная информация о проекте                      |
|      `targets`      |      str       | Цели проекта (нужно определиться с разделителем) |
|       `links`       |      json      | Словарь ссылок на соцсети формата "vk": "link"   |
| `tokens_avalaible`  |      int       | Количество доступных к покупке токенов           |
|   `tokens_total`    |      int       | Общее количество купленных акций                 |
|   `presentation`    |      (?)       | Презентация проекта (файл)                       |

   (?) - пока не определились

> Необходимо будет сделать триггер, который будет перезаписывать значение tokens_avalaible в таблице проектов

### Таблицы связей
#### 

> Пока вопрос, нужны ли таблицы связей в принципе

## Архитектура проекта

![image](https://github.com/Eytes/InvestBot/assets/67365128/e30e26a7-6020-45e6-a920-7898b138738b)

![image](https://github.com/Eytes/InvestBot/assets/67365128/4fa756f4-0c87-43c3-b361-e7c35f43e096)


