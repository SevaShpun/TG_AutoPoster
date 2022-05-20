TG_AutoPoster 
=============
Бот, пересылающий записи из групп ВК в канал/чат/ЛС в Telegram.

[![License MIT](https://img.shields.io/github/license/qwertyadrian/TG_AutoPoster.svg)](/LICENCE.md) ![Python Version](https://img.shields.io/badge/python-3.7%2B-orange.svg) [![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![issues](https://img.shields.io/github/issues/qwertyadrian/TG_AutoPoster.svg)](https://github.com/qwertyadrian/TG_AutoPoster/issues) [![stars](https://img.shields.io/github/stars/qwertyadrian/TG_AutoPoster.svg)](https://github.com/qwertyadrian/TG_AutoPoster/stargazers)
[![docker](https://img.shields.io/badge/docker%20image-tg__autoposter-FF9900)](https://hub.docker.com/r/qwertyadrian/tg_autoposter)
***
### Установка
```shell script
pip3 install -U TG-AutoPoster
```
***
### Установка (классический способ)
Команды указаны для Linux

Клонируйте репозиторий и перейдите в папку с проектом
```shell script
git clone https://github.com/qwertyadrian/TG_AutoPoster
cd TG_AutoPoster
```
Инициализируйте и активируйте виртуальное окружение (при необходимости)
```shell script
python3 -m venv venv
source venv/bin/activate
```
Установите требуемые зависимости
```shell script
pip install -r requirements.txt
```
### Настройка
1. Создайте файл config.yaml, скопируйте в него содержимое файла [config.yaml.example](/config.yaml.example) и выполните настройку ключа **vk**

|                 Параметр                 |                                                                                                                                                                                                          Описание                                                                                                                                                                                                          |
|:----------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                  login                   |                                                                                                                                                                                                          Логин ВК                                                                                                                                                                                                          |
|                   pass                   |                                                                                                                                                                                                         Пароль ВК                                                                                                                                                                                                          |
|          token (необязательно)           | **Рекомендуется к использованию.** Cервисный ключ доступа или ключ доступа пользователя ([подробнее](https://vk.com/dev/access_token)). Если он задан, то логин и пароль не используются. При его использовании не будут доступны аудиозаписи (при использовании сервисного ключа доступа также не будут доступны истории). Получить ключ доступа пользователя можно с помощью [этого](https://vkhost.github.io/) сервиса. | 

2. Получите ваши api_id и api_hash на https://my.telegram.org/apps и настройте ключ **telegram** (подробнее об Telegram API Keys [здесь](https://docs.pyrogram.org/intro/setup#api-keys))

| Параметр  |                                Описание                                |
|:---------:|:----------------------------------------------------------------------:|
|  api_id   |                               App api_id                               |
| api_hash  |                              App api_hash                              |
| bot_token | Токен Telegram бота, полученный у [@BotFather](https://t.me/BotFather) |

3. Если необходимо, настройте использование SOCKS прокси, добавив ключ **proxy** со следующим содержимым:

|         Параметр         | Возможные значения |                Описание                |
|:------------------------:|:------------------:|:--------------------------------------:|
|         enabled          |    true, false     |         Использовать ли прокси         |
|         hostname         |                    |  IP адрес (или домен) прокси сервера   |
|           port           |                    |          Порт прокси сервера           |
| username (необязательно) |                    |            Имя пользователя            |
| password (необязательно) |                    |                 Пароль                 |

4. Замените название ключа с **domain1** на домен группы ВК (или на ссылку группы) и выполните соответствующую настройку этого ключа.

|           Параметр            |                                                   Описание                                                   |
|:-----------------------------:|:------------------------------------------------------------------------------------------------------------:|
|            channel            |       Список ID каналов/чатов в Telegram, разделенных пробелом, в которые отправлять посты из групп ВК       |
|    last_id (необязательно)    | ID последнего отправленного поста. Если параметр отсутствует, он будет добавлен автоматически со значением 0 |
|   pinned_id (необязательно)   |                                           ID закреплённого поста.                                            |
| last_story_id (необязательно) |                                      ID последней отправленной истории.                                      |


5. Для изменения настроек автопостинга добавьте ключ **settings** хотя бы с одним из следующих параметров

|          Параметр           |                Возможные значения                |                                                                                     Описание                                                                                      |
|:---------------------------:|:------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|         sign_posts          |                   true, false                    |                                          Указывать ли автора поста (если это возможно) и ссылку на оригинальный пост. По умолчанию: true                                          |
|        send_reposts         |              false, post_only, true              |                             Отправлять ли репосты? Подробнее в [config.yaml.example](/config.yaml.example). По умолчанию отправка репостов отключена.                             |
|        send_stories         |                   false, true                    |                                                                    Отправлять ли истории? По умолчанию: false                                                                     |
|        what_to_send         | all, text, link, photo, doc, video, music, polls |                              Какие типы вложений отправлять. Подробнее в [config.yaml.example](/config.yaml.example). По умолчанию отправляется всё.                              |
|          stop_list          |                                                  | Путь к файлу, содержащий стоп-слова (в файле должно быть по одному слову на каждой строке). Если вы не хотите использовать стоп-слова удалите этот параметр из файла конфигурации |
|          blacklist          |                                                  |                             Путь к файлу, содержащий слова, которые будут удалены из текста отправляемого поста. Поддерживаются регулярные выражения.                             |
|    disable_notification     |                   true, false                    |                                            Отправляет сообщения молча. Пользователи получат уведомление без звука. По умолчанию: false                                            |
|  disable_web_page_preview   |                   true, false                    |                                                          Отключить предпросмотр ссылок в сообщениях. По умолчанию: true                                                           |
| posts_count (необязательно) |                число от 1 до 100                 |                                                        Количество отправляемых ботом новых постов за раз. По умолчанию 11.                                                        |

Все необязательные параметры ключа **settings** могут быть заданы индивидуально для каждой группы

Также автопостинг можно настраивать через чат с ботом. Подробнее можно узнать, отправив боту команду `/help`

**Для работы с несколькими группами добавьте новые ключи в соответствии с пунктом № 4**                                                                                                                                                                                                                                                                              
### Запуск                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                      
1. Пропишите запуск файла по расписанию [TG_AutoPoster.sh](/TG_AutoPoster.sh) в crontab (Linux) (нежелательно запускать бота каждые 5-10 минут, так как за это могут заморозить ваш профиль ВК). Также возможен запуск бота в бесконечном цикле с проверкой постов через определенный промежуток времени. Подробнее `python3 -m TG_AutoPoster --help`.                
2. Активируйте бота командой /start                                                                                                                                                                                                                                                                                                                                   
3. Готово!                                                                                                                                                                                                                                                                                                                                                            
***
Дополнительно:
[Использование Docker контейнера](/Docker.md)

Вопросы и предложения:
1. Telegram: [@QwertyAdrian](https://t.me/QwertyAdrian)
2. Вконтакте: [Адриан Поляков](https://vk.com/qwertyadrian) (отвечаю там редко)

Для пожертвований на развитие проекта:
1. [Qiwi](https://qiwi.com/n/QWERTYADRIAN)
