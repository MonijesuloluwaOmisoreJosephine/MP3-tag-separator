# MP3 Tag Separator

This Python script allows you to update the separator used in the tags (e.g., artist, genre, composer) of MP3 files in bulk. It replaces the current separator with a new separator specified by the user.

## Why I Created This:

I made this script to solve a common problem I faced with music tags. When I downloaded music, the tags often used a separator that didn't work well with Last.fm scrobbling. Last.fm prefers certain separators, and this mismatch caused issues with scrobbling accuracy. To make things easier and ensure smooth integration with Last.fm, I created this script to replace the problematic separators with ones that Last.fm recognizes, improving the overall music listening experience.

## Features

- Update the separator in specified tags of MP3 files in bulk.
- Supports updating multiple tags in a single run.
- Flexible input for tags, current separator, and new separator.
- Process multiple directories without restarting the program.

## Getting Started


### Prerequisites

- Python 3 installed on your system.
- Required Python libraries:
  ```sh
  pip install mutagen


### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/MonijesuloluwaOmisoreJosephine/MP3-tag-separator.git
   
2.Run CMD
```sh cd mp3-tag-separator-updater
3. python MP3-Tag-Separator.py

