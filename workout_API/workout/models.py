from django.db import models


class Muscles(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=100)
    can_be_used_for = models.ManyToManyField(Muscles, related_name='item_muscles')

    def __str__(self):
        return self.name


class Exercises(models.Model):
    name = models.CharField(max_length=200)
    level = models.CharField(choices=[(1, 'easy'), (2, 'medium'), (3, 'hard')], default=1, max_length=6)
    description = models.TextField(default='No description')
    instruction = models.TextField(default='No instruction, be carefully')
    target_muscle = models.ManyToManyField(Muscles, related_name='target_muscle')
    items = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='items')
    number_of_sets = models.IntegerField(blank=True, null=True)
    number_of_reps = models.IntegerField(blank=True, null=True)
    avg_time = models.IntegerField(blank=True, null=True, help_text='average time for exercise in minutes')

    def __str__(self):
        return f"{self.name} - {self.level}"

    class Meta:
        ordering = ['level']
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercises'
