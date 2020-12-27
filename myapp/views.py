from django.shortcuts import render,HttpResponse
from .models import Contact
from .models import upload
# Create your views here.
def index(request):
    context={'file':upload.objects.all()}
    if request.method== "POST":
        contact=Contact()
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        contact.firstname=firstname
        contact.lastname=lastname
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT</h1>") 
    return render(request, 'index.html',context)

    def download(request,path):
        file_Path=os.path.join(settings.MEDIA_ROOT,path)
        if os.path.exists(file_path):
            with open(file_path,'rb') as fh:
                responce=HttpResponse(fh.read(), content_type="application/notefile")
                responce['content-Disposition']='inline;filename='+os.path.basename(file_path)
                return responce

        raise Http404