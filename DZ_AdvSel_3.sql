-- 1. Количество исполнителей в каждом жанре.
select genreid, count(*)
from tartist_tgenre
group by genreid
order by genreid;

-- 2. Количество треков, вошедших в альбомы 2019–2020 годов.
select album_name, count(*)
from talbum
join ttrack on talbum.albumid = ttrack.albumid
where year_of_release between 2019 and 2020
group by album_name;

-- 3. Средняя продолжительность треков по каждому альбому.
select album_name, AVG(duration)
from talbum
join ttrack on talbum.albumid = ttrack.albumid
group by album_name;

-- 4. Все исполнители, которые не выпустили альбомы в 2020 году.
select artist_name
from tartist
join tartist_talbum on tartist.artistid = tartist_talbum.artistid
join talbum on talbum.albumid = tartist_talbum.albumid
where artist_name != (
	select artist_name 
	from tartist
	join tartist_talbum on tartist.artistid = tartist_talbum.artistid
	join talbum on talbum.albumid = tartist_talbum.albumid
	where year_of_release = 2020)
group by artist_name;

-- 5. Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
select distinct collection_name
from tcollection
join tcollection_ttrack on tcollection_ttrack.collectionid = tcollection.collectionid
join ttrack on ttrack.trackid = tcollection_ttrack.trackid
join talbum on talbum.albumid = ttrack.albumid
join tartist_talbum on tartist_talbum.albumid = talbum.albumid
join tartist on tartist.artistid = tartist_talbum.artistid
where artist_name = 'Deep Purple';









