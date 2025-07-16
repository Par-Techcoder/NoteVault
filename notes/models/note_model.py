from mongoengine import Document, StringField, DateTimeField
from datetime import datetime, timezone

class Note(Document):
    title = StringField(required=True, max_length=200)
    content = StringField()    
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {
    'collection': 'notes'
    }

    def __str__(self):
        return self.title
