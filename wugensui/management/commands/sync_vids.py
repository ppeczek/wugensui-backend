import os

from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

from wugensui.models import Video


class Command(BaseCommand):
    # help = ''

    def handle(self, *args, **options):
        media_listdir = default_storage.listdir('media')
        results_listdir = default_storage.listdir('results')
        for filename in media_listdir[1]:
            if filename != "":
                name, ext = os.path.splitext(filename)
                # video, created = Video.objects.get_or_create(name=name)
                # try:
                video, created = Video.objects.get_or_create(
                    name=name,
                    video_path=default_storage.url('media/{0}'.format(filename))
                )
                # except:
                #     video = Video.objects.get(name=name)
                if video.name in [
                    '1-1-1[1]', '1-1-1[2]', '1-1-1[3]', '1-1-1[4]', '1-1-1[5]', '1-1-1[6]',
                    '1-1-2[1]', '1-1-2[2]', '1-1-2[3]', '1-1-2[4]', '1-1-2[5]', '1-1-2[6]',
                    '1-1-3[1]', '1-1-3[2]', '1-1-3[3]', '1-1-3[4]', '1-1-3[5]', '1-1-3[6]',
                ]:
                    # video.corners = ((-90, 565), (788, 460), (1310, 480), (1010, 725))
                    video.assign_corners(((-90, 565), (788, 460), (1310, 480), (1010, 725)))
                elif video.name in [
                    '0001[1]', '0001[2]', '0001[3]', '0001[4]', '0001[5]', '0001[6]', '0001[7]'
                ]:
                    # video.corners = ((-90, 510), (788, 390), (1310, 400), (960, 650))
                    video.assign_corners(((-90, 510), (788, 390), (1310, 400), (960, 650)))
                elif video.name in [
                    '0005[1]', '0005[2]', '0005[3]'
                ]:
                    # video.corners = ((920, 420), (1450, 645), (-460, 625), (390, 420))
                    video.assign_corners(((920, 420), (1450, 645), (-460, 625), (390, 420)))
                elif video.name in [
                    '0005[4]', '0005[5]'
                ]:
                    # video.corners = ((955, 425), (1580, 700), (-570, 670), (390, 425))
                    video.assign_corners(((955, 425), (1580, 700), (-570, 670), (390, 425)))
                elif video.name == "PAWC-1":
                    # video.corners = ((0, 505), (880, 465), (1260, 570), (140, 700))
                    video.assign_corners(((0, 505), (880, 465), (1260, 570), (140, 700)))
                elif video.name == "PAWC-2":
                    # video.corners = ((10, 498), (880, 462), (1260, 565), (150, 695))
                    video.assign_corners(((10, 498), (880, 462), (1260, 565), (150, 695)))
                elif video.name == "PAWC-3":
                    # video.corners = ((17, 488), (880, 458), (1260, 563), (155, 680))
                    video.assign_corners(((17, 488), (880, 458), (1260, 563), (155, 680)))
                elif video.name == "PAWC-4":
                    # video.corners = ((17, 488), (880, 458), (1260, 563), (160, 685))
                    video.assign_corners(((17, 488), (880, 458), (1260, 563), (160, 685)))
                elif video.name == "PAWC-5":
                    # video.corners = ((8, 455), (875, 420), (1255, 525), (145, 650))
                    video.assign_corners(((8, 455), (875, 420), (1255, 525), (145, 650)))
                else:
                    print('NO {}'.format(video.name))
                    # raise Exception("Not transcripted video")

                if video.name in results_listdir[0]:
                    video.pattern = default_storage.url('results/{0}/pattern.png'.format(video.name))
                    video.paths = default_storage.url('results/{0}/result-imgs/paths.png'.format(video.name))
                    video.kalman_paths = default_storage.url(
                        'results/{0}/result-imgs/paths-kalman.png'.format(video.name)
                    )
                    video.result = default_storage.url('results/{0}/result.dat'.format(video.name))
                    video.kalman_result = default_storage.url('results/{0}/result-kalman.dat'.format(video.name))
                    video.state = Video.PROCESSED
                #     video.pattern = default_storage.url('results/{0}/pattern.png'.format(filename))
                #     video.save()
                # if not video.pattern and results_listdir
                # for i in range(1, 11):
                #     print()
                video.save()
