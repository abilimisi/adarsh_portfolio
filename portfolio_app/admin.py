from django.contrib import admin
from .models import Contact,AboutMe,Education,Skill,Projects,Link,Name_Details,Work_Known

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'desc')
    search_fields = ('name', 'email')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('course','year','institution','location')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon_class')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('projectname','projectdesc', 'live_demo','github_repo','technologies')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('profile_img','resume_file','linkedin_url','github_url','email_link','mobile_number')

@admin.register(Name_Details)
class Name_DetailsAdmin(admin.ModelAdmin):
    list_display = ('my_name', 'my_profession', 'my_profession_details')

@admin.register(Work_Known)
class Work_KnownAdmin(admin.ModelAdmin):
    list_display = ('work_name', 'work_desc')


admin.site.register(AboutMe)
admin.site.register(Education,EducationAdmin)