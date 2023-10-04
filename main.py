from song_collection import SongCollection
import argparse
import pandas as pd
import json
import os, requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--artists', type=str, default=None, help='path to txt file with a list of artists name to create dataset file.')
    parser.add_argument('-d', '--download_previews', type=str, default=None, help='You will need to create first the songs.json file by '
                                                                                  'executing the -a command')
    parser.add_argument('-j', '--convert_to_excel', help='Convert songs.json file to excel')

    args = parser.parse_args()
    if args.artists:
        df = pd.read_table(args.artists)
        artists = df["artist"].to_list()
        songs = SongCollection(artists)
        dataset = songs.create_dataset()
        json_file = json.loads(dataset)
        with open('songs.json', 'w', encoding='utf-8') as f:
            json.dump(json_file, f, ensure_ascii=False, indent=4)
        print("The dataset has been created and saved to the file songs.json")
    if args.download_previews:
        if os.path.isfile('./songs.json'):
            json_data = json.load('./songs.json')
            if not os.path.exists('./songs/'):
                os.makedirs('songs')
                print("directory songs created")
            for j in json_data['data']:
                audio = requests.get(j['previewUrl'])
                with open('songs/'+j['song_id']+".m4a", 'wb') as f:
                    f.write(audio.content)

        else:
            print("The file songs.json is missing. Make sure the file exists with the songs that need to be downloaded. See -h for help")

if __name__ == '__main__':
    main()
