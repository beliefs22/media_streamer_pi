from video_streamer.models import Video
import os
from . import find_media_files


MEDIA_ROOT = '/home/beliefs22/PycharmProjects/media'

Video.objects.all().delete()
video_types = [('mp4', 2)]
vid = 1
for video_type in video_types:
    current_videos = find_media_files.find_media_files(MEDIA_ROOT, video_type[0])
    current_videos = sorted(list(current_videos), key=lambda x: x.lower())
    if current_videos:
        for found_video in current_videos:
            video_title = os.path.basename(found_video)
            type_of_video = video_type[1]
            relative_path = "{}.{}".format(video_title, video_type[0])
            print(vid, video_title, type_of_video, relative_path)
            one_video = Video(vid, video_title, type_of_video, relative_path)
            print("Saving {}".format(found_video))
            one_video.save()
            vid += 1

