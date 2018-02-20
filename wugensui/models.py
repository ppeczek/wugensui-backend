from mongoengine import Document, fields


class Video(Document):
    name = fields.StringField(required=True, unique=True)
    video_path = fields.StringField(verbose_name='video', required=False)
    # state = fields.
    # pattern = fields.ImageField(upload_to='results', required=False)
    # pattern_frames = fields.ListField(fields.ImageField(upload_to='results'))

    def __str__(self):
        return self.name
