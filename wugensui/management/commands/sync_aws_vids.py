from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

from mongoengine.errors import NotUniqueError

from wugensui.models import Video


class Command(BaseCommand):
    # help = ''

    def handle(self, *args, **options):
        media_listdir = default_storage.listdir('media')
        results_listdir = default_storage.listdir('results')
        print(media_listdir[1])
        for filename in media_listdir[1]:
            print(filename)
            if filename != "":
                print(default_storage.url('media/{0}'.format(filename)))
                try:
                    video, created = Video.objects.create(
                        name=filename,
                        video_path=default_storage.url('media/{0}'.format(filename))
                    )
                    print('{0} {1}'.format(video, created))
                # except NotUniqueError:
                except:
                    # print("Already exists")
                    print("failed")

                # if not video.pattern and filename in results_listdir[0]:
                #     video.pattern = default_storage.url('results/{0}/pattern.png'.format(filename))
                #     video.save()
                # if not video.pattern and results_listdir
                # for i in range(1, 11):
                #     print()
