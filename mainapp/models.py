from django.db import models


# Create your models here.

class Album(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)

  def __str__(self):
    return self.name


class UploadPhoto(models.Model):
  album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
  image = models.ImageField(upload_to='images/', null=False)
 
  def __str__(self):
    return self.album.name

class MemberList(models.Model):
  position_choices = (
    ('member', 'MEMBER'),
    ('president', 'PRESIDENT'),
    ('vice president', 'VICE PRESIDENT'),
    ('secretary', 'SECRETARY'),
    ('treasurer', 'TREASURER'),
    ('auditor', 'AUDITOR'),
    ('adviser', 'ADVISER'),
    ('coordinator', 'COORDINATOR'),
    ('collector', 'COLLECTOR'),
  )
  
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  position = models.CharField(max_length=20, choices=position_choices)
  contact = models.CharField(max_length=15)
  image = models.ImageField(upload_to='images/', null=False)

  def __str__(self):
    return self.position + '-' + self.first_name

class FileUpload(models.Model):
    title = models.CharField(max_length=50)
    file = models.ImageField(upload_to='report/')


    def __str__(self):
        return self.title

class SchedMeeting(models.Model):
  agenda = models.CharField(max_length=500)
  when = models.CharField(max_length=20)
  where = models.CharField(max_length=100)

  date_created = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.agenda + ' (' + self.when +')'

