from googleapiclient.discovery import build

def initialize_youtube(api_key):
    '''Initialize the YouTube API client'''
    return build('youtube', 'v3', developerKey=api_key)

def search_videos(youtube, query, max_results=50, order='viewCount') -> list:
    '''Search for videos based on a keyword and order by view count high to low'''
    search_response = youtube.search().list(
        q=query,
        type="video",
        part="id,snippet",
        maxResults=max_results,
        order=order
    ).execute()

    # Extract video IDs from the response
    video_ids = [item['id']['videoId'] for item in search_response['items']]

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

def get_channel_ids(video_response) -> list:
    channel_ids = set()

    if "items" in video_response:
        for item in video_response["items"]:
            channel_id = item.get("snippet", {}).get("channelId")
            if channel_id:
                channel_ids.add(channel_id)  # Using a set to ensure uniqueness

    # Convert set to list before returning
    return list(channel_ids)

def get_video_categories(youtube) -> dict:
    categories_response = youtube.videoCategories().list(part="snippet",regionCode='US').execute()
    
    return categories_response
