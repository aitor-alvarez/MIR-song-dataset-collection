import requests
from time import sleep
import pandas as pd

class SongCollection:

	def __init__(self, artists=None, songs=None ):
		self.search_url = 'https://itunes.apple.com/search?term='
		self.artists = artists
		self.songs = songs

	def get_album_data(self, artist=None, song=None):
		if artist is not None:
			url = self.search_url+artist+"&entity=song"
		elif song is not None:
			url = self.search_url + song + "&entity=song"

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

		if self.artists is not None:
			keywords = self.artists
		elif self.albums is not None:
			keywords = self.albums
		for term in keywords:
			data = self.get_album_data(term)

			if data is not None:
				for result in data['results']:
					try:
						artists.append(result['artistName'])
						artists_id.append(result['artistId'])
						songs.append(result['trackName'])
						song_ids.append(result['trackId'])
						previewUrls.append(result['previewUrls'])
						primaryGenre.append(result['primaryGenreName'])
					except:
						continue
			else:
				pass
			sleep(4)

		df = pd.DataFrame({'artist':artists, 'artist_id':artists_id, 'song':songs, 'song_id': song_ids, 'previewUrls':previewUrls, 'primaryGenre':primaryGenre})

		return df


