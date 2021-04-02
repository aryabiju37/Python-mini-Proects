playlist={
	'Title':"My favorite Songs",
	'Author':"Arya",
	"Songs":[
			{"track_tirtle":"Song1","artist":["Beyonce","Jay Z"],"duration":4.5},
			{"track_tirtle":"Song2","artist":["Katy Perry"],"duration":3.0},
			{"track_tirtle":"Song3","artist":["JB","Ed Sheeran"],"duration":10.0},
			{"track_tirtle":"Song4","artist":["Nathan Wagner","Tom"],"duration":9.0},
			{"track_tirtle":"Song5","artist":["Michael Buble","Kady padry"],"duration":4.25}

	]
}

for song in playlist.items():
	print(song)