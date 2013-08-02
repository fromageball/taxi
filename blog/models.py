from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class posts(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
    slug = models.SlugField(max_length = 255)
    description = models.TextField()
    
    def __unicode__(self):
    	return self.bodytext
    
    def get_absolute_url(self):
    	return reverse('blog.views.single', kwargs={'slug': self.slug})
    	
    
    
class postsImages(models.Model):
	post = models.ForeignKey(posts, related_name='postkey') 
	image = models.ImageField(upload_to='media', blank=True)
    
      	
    
	
    

    	



	
	
	
	