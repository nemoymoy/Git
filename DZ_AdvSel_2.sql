-- 1. Название и продолжительность самого длительного трека.
select track_name, duration
from ttrack
where duration = (select max(duration) from ttrack);

-- 2. Название треков, продолжительность которых не менее 3,5 минут.
select track_name
from ttrack
where duration >= '00:03:30';

-- 3. Названия сборников, вышедших в период с 2018 по 2020 год включительно.
select collection_name
from tcollection
where year_of_release between 2018 and 2020;

-- 4. Исполнители, чьё имя состоит из одного слова.
select artist_name
from tartist
where artist_name not like '% %';

-- 5. Название треков, которые содержат слово «мой» или «my».
select track_name
from ttrack
where track_name like '% мой %' or track_name like '% my %';