# Пагинация

## Задание

Реализуйте пагинацию по csv-файлу с [портала открытых данных](https://data.mos.ru/datasets/752), содержащего список остановок наземного общественного транспорта.

Для этого необходимо реализовать функцию отображение `stations.views.bus_stations`, формируя контекст, как показано в примере.

Путь к файлу хранится в настройках `settings.BUS_STATION_CSV`.

Для чтения csv-файла можете использовать [DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader) и учтите, что файл в кодировке `utf-8`.

![Пример результата](./res/result.png)

## Документация по проекту

Для запуска проекта необходимо

Установить зависимости:

```bash
pip install -r requirements.txt
```

Выполнить команду:

```bash
python manage.py runserver
```

Пример работы проекта:

![image](https://github.com/user-attachments/assets/8efedd73-57f4-41ea-9b4f-eaa8980e2f10)

![image](https://github.com/user-attachments/assets/46d19397-5c75-443f-bf3d-a70a203dc2f5)
