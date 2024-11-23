import os
import yt_utils
import db_utils

QUERY = "nj striped bass surf fishing"
if __name__ == "__main__":
    api_key = os.environ['YOUTUBE_DATA_API_KEY']
    youtube = yt_utils.initialize_youtube(api_key)

    video_ids = yt_utils.search_videos(youtube, query=QUERY, max_results=50)
    video_details = yt_utils.get_video_details(youtube, video_ids)
    print(f'video details: \n {video_details} \n')

    channel_ids = yt_utils.get_channel_ids(video_details)
    channel_details = yt_utils.get_channel_details(youtube, channel_ids)
    print(f'channel details: \n {channel_details} \n')

    category_details = yt_utils.get_video_categories(youtube)
    print(f'categories: \n {category_details} \n')

    # Insert data using the context manager
    with db_utils.mongodb_connection() as db:
        db_utils.insert_data(db, 'videos', video_details, 'video_name')
        db_utils.insert_data(db, 'channels', channel_details, 'channel_name')
        db_utils.insert_categories(db, 'categories', category_details)
