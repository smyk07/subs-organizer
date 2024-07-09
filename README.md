# Subtitle Organization Python Script

## Usage 

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/smyk07/subs-organizer/master/script.py)"
```

## Why? 

Some torrents may provide subtitles for seasons of shows in a seperate `Subs` or `Subtitles` directory, re-arranging these files manually is a very irritating process, especially if you use a media hosting software such as jellyfin or plex. What this python script does, when run in the directory of a season, automatically detects the subtitles and places them alongside the episodes' `mp4` or `mkv` files, thus making the process much easier. This is further done through a bash script, which makes handling of the script python file much easier by cleaning up after the script has done its execution, and makes the run command much shorter.
