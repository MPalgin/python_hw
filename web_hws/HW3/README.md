## Пример выполнения запросов:

GET юзера:
```
404
{'message': 'user not found.', 'status': 'error'}
```

POST юзера:
```
200
{'id': 1, 'name': 'Ivan'}
```

GET юзера:

```
200
{'id': 1}
```

PATCH юзера:
```
200
{'id': 1}
```

DELETE юзера:

```
200
{'deleted': 'Stepan'}
```

POST объявления:

```
200
{'header': 'test advertisement', 'id': 1}

```

PATCH объявления:
```
200
{'header': 'Измененный заголовок', 'id': 1}

```
DELETE объявления:

```
200
{'deleted': 'Измененный заголовок'}

```
