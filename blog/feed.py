from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import posts

class RSSFeed(Feed):

	title = "Blog Entries"
	link = "/rss/"
	description = "description"
	
	def items(self):
		return posts.objects.order_by('timestamp')[:3]
	
	def item_title(self, item):
		return item.title
	
	def item_description(self, item):
		return item.description
	
	
	
	

		

