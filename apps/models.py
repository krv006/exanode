from django.db import models



class Technologies(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='technologies/')
    technology = models.CharField(max_length=100)
    technology_description = models.TextField()
    
    def __str__(self):
        return self.technology

class Service_Categories(models.Model):
    id = models.AutoField(primary_key=True)
    icon = models.ImageField(upload_to='service_category_icons/', null=True, blank=True)
    Title = models.CharField(max_length=200, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    Service_Options = models.JSONField(null=True, blank=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.category_name

class WhyChooseUs(models.Model):
    id = models.AutoField(primary_key=True)
    icon = models.ImageField(upload_to='why_choose_us_icons/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='projects/')
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Technologies = models.ManyToManyField(Technologies, related_name='projects')
    service_category = models.ForeignKey(Service_Categories,null=True, blank=True, on_delete=models.CASCADE)
    Link = models.URLField(max_length=300)
    Owner = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.Title

class TeamMembers(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='team_members/')
    Name = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
    about = models.TextField()
    SocialLink = models.URLField(max_length=300)
    
    def __str__(self):
        return self.Name

class Journeys(models.Model):
    id = models.AutoField(primary_key=True)
    Year = models.CharField(max_length=4)
    short_Description = models.CharField(max_length=255)
    Description = models.TextField()
    
    def __str__(self):
        return self.Year

class LeadershipTeamMembers(models.Model):
    id = models.AutoField(primary_key=True)
    team_member_id = models.ForeignKey(TeamMembers, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.team_member_id.Name

class AboutCompany(models.Model):
    id = models.AutoField(primary_key=True)
    social_type = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='about_company_icons/', null=True, blank=True)
    social_url = models.URLField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.social_type


    
class PortfolioProjects(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='portfolio_projects/')
    Title = models.CharField(max_length=200)
    category = models.ForeignKey(Service_Categories, on_delete=models.CASCADE)
    Link = models.URLField(max_length=300)
    Client = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Title
    
class ImpactMetrics(models.Model):
    total_projects = models.IntegerField()
    happy_clients = models.IntegerField()
    industries_served = models.IntegerField()
    success_rate = models.IntegerField()

class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Company = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    service = models.ForeignKey(Service_Categories, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.Name    
class Offices(models.Model):
    id = models.AutoField(primary_key=True)
    Location = models.CharField(max_length=100)
    Address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.Location
    
class SocialMediaLinks(models.Model):
    id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='social_media_icons/', null=True, blank=True)
    url = models.URLField(max_length=300)
    
    def __str__(self):
        return self.platform

class PartneredIndustiries(models.Model):
    id = models.AutoField(primary_key=True)
    industry_name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='partnered_industries_icons/', null=True, blank=True)
    MediaLink = models.URLField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.industry_name

class ProgressionMetrics(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    