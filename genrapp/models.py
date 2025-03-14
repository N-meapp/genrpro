from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Our_Products(models.Model):
    name = models.CharField(max_length=225, blank=False)
    company_name = models.CharField(max_length=225,blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to='gallery', null=True, blank=True)
    data = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20)

class Offer(models.Model):
    banner_title = models.CharField(max_length=125, default="Our Offers")
    banner_content = models.TextField(blank=True)
    image = models.ImageField(upload_to='offer')

class Our_Works(models.Model):
    title = models.CharField(max_length=225)
    work_category = models.CharField(max_length=125)
    thumbnail_img = models.ImageField(upload_to='works')
    description = models.TextField()

    def __str__(self):
        return self.title

class Addiotional_work_images(models.Model):
    work = models.ForeignKey(Our_Works,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='works')



class Enquiry(models.Model):
        name = models.CharField(max_length=225, blank=False)
        email = models.EmailField(max_length=225, blank=False)
        phone_number = models.CharField(max_length=225, blank=False)
        services = models.CharField(max_length=225,blank=False)
        message = models.TextField()

        @property
        def display_name(self):
            label = "Enquiry" 
            return f"{label}: {self.services}"
        
        def __str__(self):
            return self.display_name
        

class Career(models.Model):
        job_title = models.CharField(max_length=225, blank=False)
        job_description = models.CharField(max_length=225,blank=False)
        work_time = models.TextField()
        email = models.EmailField(max_length=225, blank=False)
        phone_number = models.CharField(max_length=225, blank=False)

        def __str__(self):
            return self.job_title
        

class JobApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    job_position = models.CharField(max_length=255)
    cv = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name





class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True, null=True)
    enquiry_type = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name









class News(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=False)
    date = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news')


    def __str__(self):
        return self.name
    
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Count(models.Model):
    happy_customers = models.IntegerField(default=0)
    projects_done = models.IntegerField(default=0)
    expert_workers = models.IntegerField(default=0)

    def __str__(self):
        return "Counts Data"