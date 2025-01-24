from django.db import models


class GameVersion(models.Model):
    version = models.CharField(max_length=20, blank=False, null=False)


class Seed(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    seed_id = models.CharField(max_length=30, blank=False, null=False)
    game_version = models.ForeignKey(GameVersion, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(blank=False, null=False)