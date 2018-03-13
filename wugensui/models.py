from mongoengine import Document, fields


NOT_PROCESSED, CREATING_PATTERN, PROCESSING_VIDEO, SAVING_RESULTS, FINISHED = range(1, 6)

PROCESSING_STATES = (
    (NOT_PROCESSED, 'not processed'),
    (CREATING_PATTERN, 'creating pattern'),
    (PROCESSING_VIDEO, 'processing video'),
    (SAVING_RESULTS, 'saving results'),
    (FINISHED, 'finished')
)


class Video(Document):
    name = fields.StringField(required=True, unique=True)
    video_path = fields.StringField(verbose_name='video', required=False)
    state = fields.IntField(choices=PROCESSING_STATES)
    corners = fields.MultiPointField()
    # pattern = fields.ImageField(upload_to='results', required=False)
    # pattern_frames = fields.ListField(fields.ImageField(upload_to='results'))

    def __str__(self):
        return self.name
