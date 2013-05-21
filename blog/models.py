from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	content = RichTextField(blank=False)

	def __unicode__(self):
		return self.title