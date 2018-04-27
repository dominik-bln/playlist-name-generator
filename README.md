# Playlist Name Generator

This application generates names from user generated playlists based on the
ISRCs of the songs.

## Usage

To use the application you need to put the required data into the `./data`
folder. The following files are expected to be present:

- **`isrc_lookup.csv`** a tab separated value file with the columns `isrc`,
  `track_artist` and `track_title`.

The you can start the application with `docker-compose up` and find it at
[http://localhost:8080](http://localhost:8080).
