from song_collection import SongCollection
import argparse
import pandas as pd
import os, requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--artists', type=str, default=None, help='path to txt file with a list of artists name to create dataset file.')
    parser.add_argument('-d', '--download_previews', type=str, default=None, help='You will need to create first the dataset.csv file by '
                                                                                  'executing the -a command')

    args = parser.parse_args()
    if args.artists:
        df = pd.read_table(args.artists)
        artists = df["artist"].to_list()
        songs = SongCollection(artists)
        dataset = songs.create_dataset()
        dataset.to_csv('dataset.csv', index=False)
        print("The dataset has been created and saved to the file songs.json")
    if args.download_previews:
        if os.path.isfile('dataset.csv'):
            data = pd.read_csv('./dataset.csv')
            if not os.path.exists('./songs/'):
                os.makedirs('songs')
                print("directory songs created")
            for index, d in data.iterrows():
                audio = requests.get(d['previewUrl'])
                with open('songs/'+d['song_id']+".m4a", 'wb') as f:
                    f.write(audio.content)

        else:
            print("The file dataset.csv is missing. Make sure the file exists with the songs that need to be downloaded. See -h for help")

if __name__ == '__main__':
    main()
