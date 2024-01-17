# Invest Bot

## Содержание
- [Invest Bot](#invest-bot)
  - [Содержание](#содержание)
  - [Технический стек](#технический-стек)
  - [БД](#бд)
    - [Модели БД](#модели-бд)
      - [Инвестор](#инвестор)
      - [Токен](#токен)
      - [Проект](#проект)
        - [Подробное описание проекта](#подробное-описание-проекта)
        - [Ссылки проекта](#ссылки-проекта)
    - [Таблицы связей](#таблицы-связей)
      - [Инвестор-Токены](#инвестор-токены)
      - [Проект-Ссылки](#проект-ссылки)
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

#### Инвестор

|      Свойство       | Тип данных | Описание                         |
|:-------------------:|:----------:|----------------------------------|
|        `id`         |    int     | Идентификатор инвестора          |
|       `tg_id`       |    int     | Телеграм id                      |
| `registration_date` |  datetime  | Дата регистрации (utc timestamp) |
|      `surname`      |    str     | Фамилия                          |
|       `name`        |    str     | Имя                              |
|    `middle_name`    |    str     | Отчество                         |
|       `photo`       |    blob    | Фото профиля                     |
|       `level`       |    int     | Уровень инвестора                |
|       `lang`        |    str     | Язык интерфейса                  |
|      `country`      |    str     | Страна                           |

#### Токен

| Свойство | Тип данных | Описание                                     |
|:--------:|:----------:|----------------------------------------------|
|   `id`   |    int     | Идентификатор токена                         |
| `price`  |    int     | Цена токена                                  |
| `color`  |    str     | HEX представление цвета (?)                  |
| `weight` |    int     | Вес токена для формирования уровня инвестора |

#### Проект

|      Свойство      | Тип данных | Описание                             |
|:------------------:|:----------:|--------------------------------------|
|        `id`        |    int     | Идентификатор проекта                |
|       `info`       |    str     | Краткая информация о проекте         |
|      `cover`       |    blob    | Обложка проекта                      |
|      `stage`       |    int     | Стадия проекта                       |
|   `description`    |    (?)     | Ссылка на экземпляр таблицы Описание |
|   `share_price`    |    int     | Цена 1-ой акции                      |
| `shares_avalaible` |    int     | Количество доступных к покупке акций |
|   `shares_total`   |    int     | Общее количество купленных акций     |

##### Подробное описание проекта
Либо использование своего идентификатора и таблицы связей

|    Свойство    | Тип данных | Описание                |
|:--------------:|:----------:|-------------------------|
|  `project_id`  |    int     | Идентификатор проекта   |
|    `goals`     |    str     | Цели проекта            |
|     `text`     |    str     | Полное описание проекта |
| `presentation` |  blob (?)  | Презентация проекта     |

##### Ссылки проекта
|   Свойство   | Свойство |  Свойство  | Описание               |
|:------------:|:--------:|:----------:|------------------------|
| `project_id` |  `url`   | `platform` | Ссылка и вид платформы |


### Таблицы связей

#### Инвестор-Токены
|   Свойство    |  Свойство  | Свойство | Описание                      |
|:-------------:|:----------:|----------|-------------------------------|
| `инвестор.id` | `токен.id` | `amount` | Количество токена у инвестора |

#### Проект-Ссылки
|   Свойство   | Свойство |  Свойство  | Описание               |
|:------------:|:--------:|:----------:|------------------------|
| `project_id` |  `url`   | `platform` | Ссылка и вид платформы |

## Архитектура проекта

![image](https://github.com/Eytes/InvestBot/assets/67365128/e30e26a7-6020-45e6-a920-7898b138738b)

![image](https://github.com/Eytes/InvestBot/assets/67365128/4fa756f4-0c87-43c3-b361-e7c35f43e096)


