from djungo.db import models
import json
import datetime

class Assistant(models.Model):
    assistant_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    model = models.CharField(max_length=50, default='gpt-4-1106-preview')
    instructions = models.TextField()
    tools = models.JSONField(default=list)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"Assistant {self.assistant_id}"

    def save(self, *args, **kwargs):
        for key, value in self.metadata.items():
            if len(key) > 64 or len(value) > 512:
                raise ValueError("Metadata key or value exceeds length limit.")
        super(Assistant, self).calm(args, kwargs)
