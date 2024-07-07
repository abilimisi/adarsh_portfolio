from django.db import models
from django.core.validators import RegexValidator
from tinymce.models import HTMLField

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class AboutMe(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Education(models.Model):
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=70)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.course
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # e.g., 'Backend', 'Frontend', etc.
    icon_class = models.CharField(max_length=100)  # For storing the icon class name

    def __str__(self):
        return self.name

class Projects(models.Model):
    projectname = models.CharField(max_length=100)
    projectdesc = HTMLField()  
    live_demo = models.URLField()  
    github_repo = models.URLField()
    technologies = models.CharField(max_length=50)

    def __str__(self):
        return self.projectname


class Link(models.Model):
    profile_img = models.ImageField(upload_to='profileimage')
    resume_file = models.FileField(upload_to='resume')
    linkedin_url = models.URLField()
    github_url = models.URLField()
    email_link = models.EmailField()
    mobile_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'LinkedIn: {self.linkedin_url}, GitHub: {self.github_url}, Email: {self.email_link}, Phone: {self.mobile_number}'


class Name_Details(models.Model):
    my_name = models.CharField(max_length=100)
    my_profession = models.CharField(max_length=100)
    my_profession_details = HTMLField()

    def __str__(self):
        return self.my_profession
    
class Work_Known(models.Model):
    work_name = models.CharField(max_length=100)
    work_desc = HTMLField()
    
    def __str__(self):
        return self.work_name