## **TG_AutoPoster - бот, который пересылает записи из групп ВК в канал/чат/ЛС в Telegram.** 

Чтобы им воспользоваться, нужно скачать на компьютер файлы AutoPoster_bot.py, config.py или просто полностью клонировать репозиторий.
Затем в файле cofig.py вы должны задать значения переменных указанных в файле.

Переменная TOKEN - это токен бота в телеграмме, который создан с помощью BotFather. 

Переменная GROUP - краткое название группы в ВК(то, что указывается в ссылке, например, https://vk.com/test_group123 значит GROUP = 'test_group123')

Переменная CHAT_ID - это ссылка на канал/чат Telegram(например, CHAT_ID = '@channel') или это ваш ID Telegram (его можно узнать у @my_id_bot). 

Переменные LOGIN, PASSWORD - ваш логин, пароль от ВК

Переменная FILENAME_VK - название файла в котором сохраняется ID последнего отправленного поста

Переменная URLS - словарь со значинями выше (кроме значений логина и пароля). Может быть расширен для работы несколькими группами ВК и каналов Telegram

Затем просто сохраните файл config.py и запустите файл AutoPoster_bot.py Но чтобы бот отправлял сообщения в канал он должен быть администратором канала, а чтобы он отправлял вам сообщения в ЛС нужно его активировать, то есть отправить ему команду /start