def get_channel_url(channel_id, key):
    return f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={channel_id}&key={key}'

def get_video_url(video_id, key):
    return f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={video_id}&key={key}'

def get_comment_url(video_id, key):
    return f'https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&maxResults=100&videoId={video_id}&key={key}'