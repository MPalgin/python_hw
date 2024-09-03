create table if not exists genre (
	genre_id SERIAL primary key,
	genre_name VARCHAR(60) not NULL
);

create table if not exists author (
	author_id SERIAL primary key,
	author_name VARCHAR(60) not NULL
);

create table if not exists albom (
	albom_id SERIAL primary key,
	albom_name VARCHAR(60) not null,
	issue_year INTEGER not null
);

create table if not exists track (
	track_id SERIAL primary key,
	track_name VARCHAR(60) not null,
	duration INTEGER not null,
	albom_id INTEGER not null references albom(albom_id)
);

create table if not exists compilation (
	compilation_id SERIAL primary key,
	compilation_name VARCHAR(60) not null,
	issue_year INTEGER not null
);

create table if not exists genre_by_author(
	genre_id INTEGER references genre(genre_id),
	author_id INTEGER references author(author_id),
	constraint PK primary key(genre_id, author_id)
);

create table if not exists albom_by_author(
	albom_id INTEGER references albom(albom_id),
	author_id INTEGER references author(author_id),
	constraint Albom_Author primary key(albom_id, author_id)
);

create table if not exists tracks_in_compilation(
	compilation_id INTEGER references compilation(compilation_id),
	track_id INTEGER references track(track_id),
	constraint Tracks primary key(compilation_id, track_id)
);

insert into genre(genre_id, genre_name)
values(1, 'Rock'), (2, 'Classic'), (3, 'Pop');

insert into author(author_id, author_name)
values(1, 'AcDC'), (2, 'Bethoven'), (3, 'Foals'), (4, 'Stromae');

insert into genre_by_author(genre_id, author_id)
values(1, 1), (2, 2), (1, 3), (3, 4);

insert into albom(albom_id, albom_name, issue_year)
values(1, 'Classic music compilation', 1987), (2, 'Classic rock', 2020), (3, 'French music', 2005);

insert into albom_by_author(albom_id, author_id)
values(1, 2), (2, 1), (2, 3), (3, 4);

insert into track(track_id, albom_id, track_name, duration)
values(1, 1, 'Sonata 3', 120), (2, 1, 'Libreto for opera', 183), (3, 2, 'Highway to Hell', 200), (4, 2, 'Spanish sahara', 100), (5, 3,'Papaute', 320), (6, 2, 'My Moonlight', 168);

insert into compilation(compilation_id, compilation_name, issue_year)
values(1, 'Europian music', 2000), (2, 'World classic', 2005), (3, 'Songs of 2000', 2020), (4, 'Rock songs', 2012);

insert into tracks_in_compilation(compilation_id, track_id)
values(1, 1), (1, 2), (1, 5), (2, 1), (2,2), (3, 4), (3, 5), (3, 6), (4, 3), (4, 4);

--Название и продолжительность самого длительного трека

select max(duration), track_name from track
group by track_name
limit 1;

--Название треков, продолжительность которых больше 3.5 минут
select track_name from track
where duration/60 >= 3.5;

--Названия сборников, вышедших в период с 2018 по 2020 год включительно
select compilation_name from compilation
where issue_year between '2018' and '2020';

--Исполнители, чьё имя состоит из одного слова
select author_name from author
where author_name not like ' %';

--Название треков, которые содержат слово «мой» или «my»
select track_name from track
where lower(track_name) like '%my%' or lower(track_name) like '%мой%';

--Количество исполнителей в каждом жанре
select genre_name, count(a.author_name) from genre g 
left join genre_by_author gba on g.genre_id = gba.genre_id 
left join author a on gba.author_id = a.author_id 
group by genre_name
order by count(a.author_name) desc;

--Количество треков, вошедших в альбомы 2019-2020 годов
select count(track_name) from track t 
left join albom a on t.albom_id = a.albom_id 
where issue_year between 2019 and 2020;

--Средняя продолжительность треков по каждому альбому
select a.albom_name, avg(duration) from track t 
left join albom a on t.albom_id = a.albom_id 
group by albom_name
order by avg(duration);

--Все исполнители которые не выпустили альбомы в 2020 году
select author_name from author a 
left join albom_by_author aba on a.author_id = aba.author_id 
left join albom a2 on a2.albom_id = aba.albom_id 
where author_name not in (select author_name from albom_by_author where issue_year between 2020 and 2021);

--Названия сборников, в которых присутствует конкретный исполнитель
select compilation_name from compilation c
left join tracks_in_compilation tic on tic.compilation_id = c.compilation_id 
left join track t on t.track_id = tic.track_id 
left join albom a on t.albom_id = a.albom_id 
left join albom_by_author aba on aba.albom_id = a.albom_id 
left join author a2 on aba.author_id = a2.author_id 
where author_name like 'Foals';
