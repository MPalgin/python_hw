Пример работы проекта:

Страница сайта:

![image](https://github.com/user-attachments/assets/a9da3ddf-fcba-45ee-af5f-33c69b11b357)


Создание продукта:

![image](https://github.com/user-attachments/assets/4609f720-7de2-4207-9fb2-0cac8f75c902)

Создание склада:

![image](https://github.com/user-attachments/assets/6b09f6be-faf9-457d-8cbd-9c038d7e8630)

Поиск по имени:

![image](https://github.com/user-attachments/assets/b41b24bc-9d26-49c2-92dd-9b3868e078c1)

```
Сборка контейнера:
 sudo docker build --tag my-server:1.0 .

Запуск контейнера:
sudo docker run --publish 8080:8000 --detach --name test my-server:1.0

Зайти в контейнер:
sudo docker exec -it d784fbb6012cb5f15d7d149210c81766898fe1854cc2cd581b179058da544c75 bash

```
