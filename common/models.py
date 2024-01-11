from uuid import uuid4

from django.db import models
r_choices=(("Admin","Admin"),("Student","Student"),("Teacher","Teacher"),("Parent","Parent"))
dp_choices=(("Science","Science"),("Management","Management"))
g_choices=(("M","Male"),("F","Female"),("O","Other"))
l_choices=(("11","11"),("12","12"))
class CommonInfo(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, db_index=True
    )
    created_on = models.DateTimeField("Created at", auto_now_add=True, db_index=True)
    modified_on = models.DateTimeField("Last modified at", auto_now=True, db_index=True)

    class Meta:
        abstract = True
