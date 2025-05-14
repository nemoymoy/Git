insert into tartist
values	(1, 'Metallica'), 
		(2, 'Deep Purple'), 
		(3, 'Nirvana'), 
		(4, 'The Beatles');

insert into talbum
values	(1, 'Nevermind', 1991),
		(2, 'Master of Puppets', 1986),
		(3, 'Machine Head', 1972),
		(4, 'Revolver', 1966),
		(5, 'Help', 1965),
		(6, 'Let it be', 1970),
		(7, 'Metallica', 1991),
		(8, 'The Black Album', 1991),
		(9, 'Deep Purple in Rock', 1970),
		(10, 'All apologies', 1993),
		(11, 'St. Anger', 2003),
		(12, 'Rubber Soul', 1965),
		(13, 'S&M2', 2020);

insert into tartist_talbum 
values 	(1, 2),
		(1, 7),
		(1, 8),
		(2, 3),
		(2, 9),
		(3, 1),
		(3, 10),
		(4, 4),
		(4, 5),
		(4, 6),
		(1, 11),
		(4, 12),
		(1, 13);

insert into tgenre 
values 	(1, 'rock-n-roll'),
		(2, 'heavy-metall'),
		(3, 'hard-rock'),
		(4, 'grunge'),
		(5, 'punk-rock');

insert into tartist_tgenre 
values 	(1, 2),
		(1, 3),
		(2, 3),
		(2, 2),
		(3, 4),
		(3, 5),
		(4, 1),
		(4, 3);

insert into ttrack 
values 	(1, 'Yesterday', '00:02:34', 5),
		(2, 'Let it be', '00:04:03', 6),
		(3, 'Enter Sandman', '00:05:30', 7),
		(4, 'The Unforgiven', '00:06:26', 8),
		(5, 'Smoke on the Water', '00:05:42', 3),
		(6, 'Black Night', '00:03:28', 9),
		(7, 'Smells Like Teen Spirit', '00:05:01', 1),
		(8, 'Rape me', '00:02:49', 10),
		(9, 'My word', '00:05:45', 11),
		(10, 'In my life', '00:02:28', 12),
		(11, 'Intro to Scythian Suite', '00:05:17', 13),
		(12, 'Highway Star', '00:06:05', 3),
		(13, 'Come as You Are', '00:03:38', 1);

insert into tcollection 
values 	(1, 'Sliver: The Best of the Box', 2005),
		(2, 'The Deep Purple Singles A''s and B''s', 1993),
		(3, '20 Greatest Hits', 1982),
		(4, 'The Metallica Collection', 2009),
		(5, 'Best Bester Bestest', 2019);

insert into tcollection_ttrack 
values 	(1, 7),
		(1, 8),
		(2, 5),
		(2, 6),
		(3, 1),
		(3, 2),
		(4, 3),
		(4, 4),
		(5, 3),
		(5, 4),
		(5, 5),
		(5, 6),
		(4, 9),
		(3, 10);



