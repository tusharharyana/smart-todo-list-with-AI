from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    usage_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ContextEntry(models.Model):
    content = models.TextField()
    source_type = models.CharField(max_length=50)  # WhatsApp, email, notes
    timestamp = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priority_score = models.FloatField(default=0)
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='pending')  # pending/done
    created_at = models.DateTimeField(auto_now_add=True)
