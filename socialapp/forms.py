from django import forms
from website.models import Event

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = (
			'name', 'organisator', 'location'
			'from_date', 'to_date', 'expectations'
			'provided', 'event_type',
			)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = (
			'content', 'image',
		)