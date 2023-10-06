# MIR-song-dataset-collection

The current scripts searches in iTunes API for the artists that you have selected in your list (see step 1 under instructions) and downloads a 30 second preview of each song from those artists.

The resulting dataset could be used for training Deep Learning models in singer identification tasks.

## Instructions

1. Clone the current repository: git clone https://github.com/aitor-alvarez/MIR-song-dataset-collection.git 
2. Create a file with the artists/performers list. The file should be named artists.txt and contain a single column with the first row (as header) named artist. Place all your artists' names below this header.
3. Execute the following command to parse the list of artists and search iTunes API for their songs: python main.py -a artists.txt This will result in the creation of a file named dataset.csv that will contain all songs from those artists.
4. Feel free to edit dataset.csv if you want to exclude songs.
5. To download the 30 second previews execute: python main.py -d
6. All previews will be downloaded into a subfolder within this repository named songs/

   
