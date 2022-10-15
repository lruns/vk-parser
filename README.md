# vk-parser
## Получение данных об интересах пользователей ВКонтакте

Это небольшой репозиторий, предназначенный для получения следующих данных по URL страницы пользователя (https://vk.com/some_nick):
- понравившейся посты
- созданные пользователем посты
- посты, которые сохранил пользователь у себя на странице
- комментарии пользователя

Чтобы загрузить данные определенного пользователя, нужно создать в корне проекта файл `config.py` со следующей структурой:
```python
token = "token"
url_for_search_user = "https://vk.com/some_nick"
```
где `token` - токен для доступа к API ВКонтакте, инструкция по его получению https://dvmn.org/encyclopedia/qna/63/kak-poluchit-token-polzovatelja-dlja-vkontakte/.
И затем запустить parser.ipynb (не забыв про requirements.txt).

Для создания отчета нужно использовать generate_report.py, перед этим добавив также в config.py` следующее:
```python
user_nick = "nick"
user_name = "Ivan Ivanov"
```