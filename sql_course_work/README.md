# Схема базы данных
Схема состоит из 4 таблиц. Три из которых соеденены связью один-много, а одна необходима для заполнения вариантов кнопок для выбора перевода.

![image](https://github.com/user-attachments/assets/1fe84b2e-7fac-4fe2-aded-f25d4100a7a1)

В userdata хранится идентификатор пользователя, получаемый при старте чата. Word_dict содержит общие слова доступные всем пользователям, у этих слов user_id = NULL, и слова конкретных пользователей, у этих слов user_id = идентификатору пользователя.
В translate хранятся переводы слов, связанные с word_dict через word_id.

# Пример работы бота

При старте чат бот отправляет привествие с описанием досутпного функционала и предлагает выбрать перевод первого слова, которое выбирается рандомно. 3 из 4 вариантов выбираются из таблицы randomwords случайно:

![image](https://github.com/user-attachments/assets/3b340ed5-0def-4bbb-9729-a3f7acb82ec0)

У пользователя сразу досутпны 4 кнопки с вариантами ответа и кнопки добавить и удалить слово:
![image](https://github.com/user-attachments/assets/d3ac966f-ae64-4de4-a3ab-ecf514b5e252)

Если пользователь выбирает неверный ответ, то чат бот показывает что ответ неверный и предлагает попробовать снова:

![image](https://github.com/user-attachments/assets/ffcee75b-0358-4a2e-8194-d937f2ff7cd0)

![image](https://github.com/user-attachments/assets/df021afb-290f-4fc4-966e-6d9da0e23619)

![image](https://github.com/user-attachments/assets/89efdbbf-830d-4b0f-ad71-b61a05546f13)

При нажатии кнопки добавить слово, чат бот просит ввести слово и его перевод и добавляет их в соотвествующую БД с указанием идентификатора пользователя:

![image](https://github.com/user-attachments/assets/bec79456-7728-4c64-a3ee-08967c64c968)

![image](https://github.com/user-attachments/assets/64cab011-1e90-48dd-a2c4-d658c9f97c55)

![image](https://github.com/user-attachments/assets/0858c18a-a12e-446e-ad45-7ce00e5074bc)

Если после добавления слова нажимать следующее слово, то добавленное слово будет доступно для изучения:

![image](https://github.com/user-attachments/assets/1f0d5cd4-b925-415c-8a60-9c2cef0457d7)

При удалении слова, слово вместе с переводом удаляется из БД:

![image](https://github.com/user-attachments/assets/0fb4b29d-c104-4d2c-bf2f-a174380bfb38)

![image](https://github.com/user-attachments/assets/abbe5eb0-98f4-46b4-b994-70683c297a77)

![image](https://github.com/user-attachments/assets/42c81475-4a3f-4563-b258-aa8306edcbe8)

Сам бот досутпен по ссылке:
https://t.me/engNetbot
