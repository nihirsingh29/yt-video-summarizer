from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import json

app = Flask(__name__)


def get_transcript_from_video(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id=video_id)
    transcript = ""
    for i in transcript_list:
        transcript += i['text']
    print(transcript)

def get_yt_video_id(url):
    """Returns Video_ID extracting from the given url of Youtube

    Examples of URLs:
      Valid:
        'http://youtu.be/_lOT2p_FCvA',
        'www.youtube.com/watch?v=_lOT2p_FCvA&feature=feedu',
        'http://www.youtube.com/embed/_lOT2p_FCvA',
        'http://www.youtube.com/v/_lOT2p_FCvA?version=3&amp;hl=en_US',
        'https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6',
        'youtube.com/watch?v=_lOT2p_FCvA',

      Invalid:
        'youtu.be/watch?v=_lOT2p_FCvA',
    """

    if url.startswith(('youtu', 'www')):
        url = 'http://' + url

    query = urlparse(url)

    if 'youtube' in query.hostname:
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    elif 'youtu.be' in query.hostname:
        return query.path[1:]
    else:
        raise ValueError


# video_url = input("Enter youtube video url: ")
video_url = "https://www.youtube.com/watch?v=BQBMbwfC6TY&ab_channel=Fireship"
main_video_id = get_yt_video_id(video_url)
get_transcript_from_video(main_video_id)
