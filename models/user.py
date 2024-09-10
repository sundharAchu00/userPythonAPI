from django.db import models


class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}
