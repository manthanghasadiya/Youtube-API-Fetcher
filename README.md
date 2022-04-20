# Youtube-API-Fetcher

## Objective
* Make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
* Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
* A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
* A basic search API to search the stored videos using their title and description.
* Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.

## Screen recording
* Screen recording of the projct 


https://github.com/manthanghasadiya/Youtube-API-Fetcher/blob/main/Media/How%20to%20run%20server.webm

## How to run
```bash
# Clone the Youtub-API-Feetcher repo with git
git clone https://github.com/manthanghasadiya/Youtube-API-Fetcher.git

# Switch to project directory
cd Youtube-API-Fetcher

# Install required files
pip install -r requirements.txt

# Run the server
python manage.py runserver

# Open this url in browser
http://127.0.0.1:8000
```
