from mongoengine import Document, StringField, DateTimeField, BooleanField, IntField
from datetime import datetime, timezone
from notes.constants.default_value import Gender


class User(Document):
    email = StringField(required=True, unique=True, max_length=255)
    password = StringField(required=True, max_length=128)

    name = StringField(required=False, max_length=100)
    gender = IntField(
        choices=[(gender.value, gender.name) for gender in Gender],
        required=False
    )

    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    meta = {
        'collection': 'users'
    }

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"
