import requests
from time import sleep
import pandas as pd

class SongCollection:

	def __init__(self, artists):
		self.search_url = 'https://itunes.apple.com/search?term='
		self.artists = artists

	def get_album_data(self, artist=None, song=None):
		if artist is not None:
			url = self.search_url+artist+"&entity=song"

		try:
			response_data = requests.get(url)
			response = response_data.json()
			if response['resultCount'] >0:
				return response
			else:
				return None

		except ValueError:
			pass

	def create_dataset(self):
		artists_id=[]
		artists=[]
		songs=[]
		song_ids=[]
		previewUrls=[]
		primaryGenre=[]

		for term in self.artists:
			data = self.get_album_data(term)

			if data is not None:
				for result in data['results']:
					try:
						if result['artistName']:
							artists.append(result['artistName'])
						else:
							artists.append("None")
						if result['artistId']:
							artists_id.append(result['artistId'])
						else:
							artists_id.append("None")
						if result['trackName']:
							songs.append(result['trackName'])
						else:
							songs.append(" ")
						if result['trackId']:
							song_ids.append(result['trackId'])
						else:
							song_ids.append(" None")
						if result['previewUrl']:
							previewUrls.append(result['previewUrl'])
						else:
							previewUrls.append("None ")
						if result['primaryGenreName']:
							primaryGenre.append(result['primaryGenreName'])
						else:
							primaryGenre.append("None")
					except:
						continue
			else:
				pass
			sleep(4)

		df = pd.DataFrame({'artist':artists, 'artist_id':artists_id, 'song':songs, 'song_id': song_ids, 'previewUrl':previewUrls, 'primaryGenre':primaryGenre})
		df = df.reset_index(drop=True)
		json_songs = df.to_json(orient="split")
		return json_songs


