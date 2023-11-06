from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
from uploadapp.models import UploadFile
# Create your views here.

def uploadimage(request):

    if request.method=="POST":
        fileobj=request.FILES['myimage']
        #print(fileobj.name)
        fs=FileSystemStorage()
        #print(fs)
        filename=fs.save(fileobj.name,fileobj) #save
        print(filename)
        url=fs.url(filename)#url fetched
        print(url)
        uobj=UploadFile.objects.create(path=url)
        uobj.save()
        return HttpResponse("Data Fetched")
    else:
        return render(request,'upload.html')


def showimage(request):
    imgs=UploadFile.objects.all()
    context={}
    context['images']=imgs

    return render(request,'showimage.html',context)
