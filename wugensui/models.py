from django.db import models


class Video(models.Model):
    NOT_PROCESSED, CREATING_PATTERN, PROCESSING_VIDEO, SAVING_RESULTS, PROCESSED = range(1, 6)

    PROCESSING_STATES = (
        (NOT_PROCESSED, 'not processed'),
        (CREATING_PATTERN, 'creating pattern'),
        (PROCESSING_VIDEO, 'processing video'),
        (SAVING_RESULTS, 'saving results'),
        (PROCESSED, 'finished')
    )

    name = models.CharField(max_length=50, unique=True)
    video_path = models.FileField(verbose_name='video', blank=True, null=True)
    state = models.IntegerField(choices=PROCESSING_STATES, default=NOT_PROCESSED)

    # provided by user
    # corners = ArrayField(ArrayField(models.IntegerField(), size=2), size=4)
    corner_a_x = models.IntegerField(verbose_name='corner A X', null=True, blank=True)
    corner_a_y = models.IntegerField(verbose_name='corner A Y', null=True, blank=True)
    corner_b_x = models.IntegerField(verbose_name='corner B X', null=True, blank=True)
    corner_b_y = models.IntegerField(verbose_name='corner B Y', null=True, blank=True)
    corner_c_x = models.IntegerField(verbose_name='corner C X', null=True, blank=True)
    corner_c_y = models.IntegerField(verbose_name='corner C Y', null=True, blank=True)
    corner_d_x = models.IntegerField(verbose_name='corner D X', null=True, blank=True)
    corner_d_y = models.IntegerField(verbose_name='corner D Y', null=True, blank=True)

    # created by analyzer
    pattern = models.ImageField(blank=True, null=True)
    # pattern_frames = ArrayField(models.ImageField(upload_to='results/frames'), size=10)

    # paths = models.ImageField(upload_to='results/paths', blank=True, null=True)
    # kalman_paths = models.ImageField(upload_to='results/paths', blank=True, null=True)
    # result = models.FileField(upload_to='', blank=True, null=True)
    # kalman_result = models.FileField(upload_to='', blank=True, null=True)

    paths = models.ImageField(blank=True, null=True)
    kalman_paths = models.ImageField(blank=True, null=True)
    result = models.FileField(blank=True, null=True)
    kalman_result = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name

    def assign_corners(self, corners):
        self.corner_a_x, self.corner_a_y = corners[0]
        self.corner_b_x, self.corner_b_y = corners[1]
        self.corner_c_x, self.corner_c_y = corners[2]
        self.corner_d_x, self.corner_d_y = corners[3]
