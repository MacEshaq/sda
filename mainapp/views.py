from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logouts
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import CreateUserForm
from .decorators import allowed_users

# ==================================
def index(request):
  meetingSched = SchedMeeting.objects.all().last()
  allAlbum = Album.objects.all()
  allImage = UploadPhoto.objects.all()
  print(meetingSched)
  context = {'allImage':allImage, 'allAlbum':allAlbum,'home_active': 'active_page', 'meetingSched':meetingSched}
  return render(request, 'mainapp/index.html', context)
# ===========================
def gallery(request):
  allAlbum = Album.objects.all()
  # this is geeting the get from gallery, "url 'gallery' %}?album={{ album.name}}"                       
  album = request.GET.get('album')
  albumName = ''
  if album == None:
    allImage = UploadPhoto.objects.all()
    albumName = 'All Album'

  else:
    allImage = UploadPhoto.objects.filter(album__name=album)
    albumName = album

  context = {'allImage':allImage, 'allAlbum':allAlbum, 'albumName':albumName, 'gallery_active': 'active_page'}
  return render(request, 'mainapp/gallery.html', context)
# ================================
@login_required
@allowed_users(allowed_roles=['admin'])
def addPhoto(request):
  allAlbum = Album.objects.all()

  if request.method == "POST":
    data = request.POST
    image = request.FILES.get('image')

    if data['album'] != 'none':
      album = Album.objects.get(id=data['album'])
    elif data['new_album'] != '':
      album, created = Album.objects.get_or_create(
        name=data['new_album'])

    else:
      album = None

    photo = UploadPhoto.objects.create(
      album = album,
      image = image,

    )
    return redirect('gallery')

  context = {'allAlbum':allAlbum}
  return render(request, 'mainapp/add.html', context)
# ==============================
def members(request):
  allImage = UploadPhoto.objects.all()
  sda_officers = MemberList.objects.all()

  officer_list = []
  for officer in sda_officers:
    if officer.position != 'member':
      officer_list.append(officer)

  context ={'members_active': 'active_page', 'officer_list':officer_list, 'allImage':allImage}
  return render(request, 'mainapp/members.html',context)
# =========================
def about(request):

  context ={'about_active': 'active_page'}
  return render(request, 'mainapp/about.html', context)
# ============================
@login_required
def report(request):
  allReport = FileUpload.objects.all()

  context ={'report_active': 'active_page', 'allReport':allReport}
  return render(request, 'mainapp/report.html', context)

def viewReport(request, pk):
  file = FileUpload.objects.get(id=pk)

  context = {'file':file}
  return render(request, 'mainapp/view_report.html', context)  
# =================================
@login_required
@allowed_users(allowed_roles=['admin'])
def admin_user(request):

  #===create new user===
  form = CreateUserForm()
  if request.method == "POST":
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request, 'Account was created for ' +  user)
    
      return redirect('login')

  #===below is for uploading photo===
  allAlbum = Album.objects.all()
  if request.method == "POST":
    data = request.POST
    image = request.FILES.get('image')

    if data['album'] != 'none':
      album = Album.objects.get(id=data['album'])
    elif data['new_album'] != '':
      album, created = Album.objects.get_or_create(
        name=data['new_album'])

    else:
      album = None

    photo = UploadPhoto.objects.create(
      album = album,
      image = image,
    )
    return redirect('gallery')
      
  context ={'form':form, 'allAlbum':allAlbum}
  return render(request, 'registration/admin_user.html', context)
# ==============================
def logout(request):
  if request.method == "POST":
    logouts(request)
    return redirect('index')
# ===========================
# dont forget to delete this
def test(request):
  return render(request, 'mainapp/test.html')


  

