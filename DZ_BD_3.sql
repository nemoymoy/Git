-- создаем таблицу Исполнителей

CREATE TABLE IF NOT EXISTS tArtist (
	artistID SERIAL PRIMARY KEY,
	artist_name VARCHAR(40) NOT NULL
);

-- создаем таблицу Жанров

CREATE TABLE IF NOT EXISTS tGenre (
	genreID SERIAL PRIMARY KEY,
	genre_name VARCHAR(40) NOT NULL
);

-- создаем таблицу Исполнителей и Жанров (многие ко многим)

CREATE TABLE IF NOT EXISTS tArtist_tGenre (
	artistID INTEGER REFERENCES tArtist(artistID),
	genreID INTEGER REFERENCES tGenre(genreID),
	CONSTRAINT artist_genre PRIMARY KEY (artistID, genreID)
);

-- создаем таблицу Альбомов

CREATE TABLE IF NOT EXISTS tAlbum (
	albumID SERIAL PRIMARY KEY,
	album_name VARCHAR(100) NOT NULL,
	year_of_release INTEGER NOT NULL
);

-- создаем таблицу Исполнителей и Альбомов (многие ко многим)

CREATE TABLE IF NOT EXISTS tArtist_tAlbum (
	artistID INTEGER REFERENCES tArtist(artistID),
	albumID INTEGER REFERENCES tAlbum(albumID),
	CONSTRAINT artist_album PRIMARY KEY (artistID, albumID)
);

-- создаем таблицу Треков (один ко многим)

CREATE TABLE IF NOT EXISTS tTrack (
	trackID SERIAL PRIMARY KEY,
	track_name VARCHAR(100) NOT NULL,
	duration TIME NOT NULL,
	albumID INTEGER NOT NULL REFERENCES tAlbum(albumID)
);

-- создаем таблицу Сборников

CREATE TABLE IF NOT EXISTS tCollection (
	collectionID SERIAL PRIMARY KEY,
	collection_name VARCHAR(100) NOT NULL,
	year_of_release INTEGER NOT NULL
);

-- создаем таблицу Сборников и Треков (многие ко многим)

CREATE TABLE IF NOT EXISTS tCollection_tTrack (
	collectionID INTEGER REFERENCES tCollection(collectionID),
	trackID INTEGER REFERENCES tTrack(trackID),
	CONSTRAINT collection_track PRIMARY KEY (collectionID, trackID)
);