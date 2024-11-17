import isodate
from googleapiclient.discovery import build

def convert_duration_to_minutes(duration) -> float:
    parsed_duration = isodate.parse_duration(duration)
    return round(parsed_duration.total_seconds() / 60, 2)

def initialize_youtube(api_key):
    '''Initialize the YouTube API client'''
    return build('youtube', 'v3', developerKey=api_key)

def search_videos(youtube, query, max_results=50, max_pages=1) -> list:
    '''Search for videos based on a keyword'''
    video_ids = []
    next_page_token = None
    page_count = 0

    while page_count < max_pages:
        search_response = youtube.search().list(
            q=query,
            type="video",
            part="id,snippet",
            maxResults=max_results,
            pageToken=next_page_token
        ).execute()

        # Extract video IDs from the current page and add to the list
        video_ids.extend([item['id']['videoId'] for item in search_response['items']])

        # Check for the next page token and increment the page counter
        next_page_token = search_response.get('nextPageToken')
        if not next_page_token:  # Break if there is no next page
            break
        
        page_count += 1

    return video_ids

def get_video_details(youtube, video_ids) -> dict:
    '''Get details of videos including tags, views, likes, comments, and duration'''
    video_response = youtube.videos().list(
        id=','.join(video_ids),
        part="snippet,contentDetails,statistics"
    ).execute()
    
    return video_response

def get_channel_details(youtube, channel_ids) -> dict:
    '''Get channel details including subscriber count and total views'''
    channel_response = youtube.channels().list(
        id=','.join(channel_ids),
        part="snippet,statistics"
    ).execute()

    return channel_response

def get_channel_ids(video_response) -> dict:
    channel_ids = set()

    if "items" in video_response:
        for item in video_response["items"]:
            channel_id = item.get("snippet", {}).get("channelId")
            if channel_id:
                channel_ids.add(channel_id)  # Using a set to ensure uniqueness

    # Convert set to list before returning
    return list(channel_ids)