# Аналитика в компании

В данном репозитории представлен проект, в котором продемонстрированы базовые задачи, с которыми может столкнуться Junior Data Analyst.
Представим, что мы устроились в стартап, объединяющий в себе ленту новостей и мессенджинг, нам нужно настроить аналитические процессы внутри нашей компании.

---

1. [**Формирование отчета по ключевым метрикам в телеграм**](https://gitlab.com/te4624/analyst_cycle/-/blob/main/telegram_bot.py): 

Аналитика начинается с вопроса ***сколько?***. Сколько пользователей пользуются нашим приложением в день, сколько они ставят лайков, какой CTR, сколько просмотров итд. Мы всегда должны получить быстрый ответ на ключевые вопросы, сформируем отчет и настроим автоматическое расписание в гитлаб(чтобы он приходил к нам каждое утро без нашего участия). 

***Стек:*** Pandas, seaborn, matplotlib, asyncio, telegram, pandahouse, os, [**CI/CD**](https://gitlab.com/te4624/analyst_cycle/-/blob/main/gitlab-ci.yml)
[***Пример отчета***](https://sun1-92.userapi.com/s/v1/if2/j985FZZhVNvKl7FnCPoB10WYhQMCjOFV1MJyCrGZnb-xsK_WdpUEWwZQADW773zc8mwZ65xQSRmpJflz-Jy_rXUa.jpg?size=972x2160&quality=95&type=album)

---

2. [**Что делать, если что-то пошло не так?**]:

Каждый переживает, когда с их метрикой происходит что-то не так. 
Но как понять и быстро среагировать на изменения? Для этого мы сделаем ***систему оповещений***, чтобы аллерт приходил к нам, когда что-то происходит не так.

Стек: Pandas, sqlalchemy, SQL, Tableau.

---

3. [**Анализируем продуктовые метрики**](https://gitlab.com/te4624/analyst_cycle/-/blob/main/product.ipynb)

С первостепенными задачами разобрались, теперь нужно углубиться в продукт, чтобы исследовать различные гипотезы. Ответим на более сложные продуктовые вопросы
Так же пример [**E-commerce работы с RFM сегментацией**](https://gitlab.com/te4624/analyst_cycle/-/blob/main/miniproject.ipynb)
Стек: SQL, matplotlib, seaborn, pandas.

---

4. [**A/B тестирование**]

Дата-сайентисты пришли к нам с новым алгоритмом рекомендаций, они считают что он увеличит наш CTR. 
Проведем исследование, является ли алгоритм удачным и сделаем вывод.


Стек: Pandas, matplotlib, seaborn, numpy.

---
