from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Template, TemplateCSSFile, TemplateHTMLFile, TemplateIMGFile, TemplateJSFile
import json
from .view_helper import jsFileData
import zipfile
from django.conf import settings
import os
# Create your views here.

def home(request):
    
    if request.method == 'POST':
        # print(Template.objects.all()
        prof_skill_data = request.POST.get('prof-skill-data')
        project_data = request.POST.get('project-data')
        education_data = request.POST.get('education-data')
        experience_data = request.POST.get('experience-data')

        image_file = request.POST.get('image-file')
        print(type(image_file))

        data = {
            'personal_data': personal_data_retriever(request),
            'link_data': link_data_retriever(request),
            'prof_skill_data': prof_skill_data,
            'project_data': project_data,
            'education_data': education_data,
            'experience_data': experience_data
        }

        js_str = jsFileData(data)
        temp = Template.objects.all()
        img_file_db = TemplateIMGFile.objects.filter(template=temp.get())
        for i in img_file_db:
            # i.filename()
            if i.filename()[0:6] == 'person':
                i.image = image_file
                

        js = TemplateJSFile.objects.filter(template=temp.get())
        jsx = TemplateJSFile.objects.get(id=js[0].pk)
        f = open(jsx.javascript.path, "r+")
 
        f.truncate(0)
        f.write(js_str)
        f.close()
        return redirect('download')

        
    return render(request, 'portfolio/home.html')


def personal_data_retriever(request):
    first_name = request.POST.get('first-name')
    last_name = request.POST.get('last-name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip = request.POST.get('zip')
    about = request.POST.get('about-yourself')

    return json.dumps({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'address2': address2,
        'city': city,
        'state': state,
        'zip': zip,
        'about': about
    })


def link_data_retriever(request):
    git = request.POST.get('git-link')
    facebook = request.POST.get('facebook-link')
    twitter = request.POST.get('twitter-link')
    linkedin = request.POST.get('linkedin-link')
    instagram = request.POST.get('instagram-link')
    resume = request.POST.get('resumeLink')
    
    return json.dumps({
        'git': git,
        'facebook':facebook,
        'twitter': twitter,
        'linkedin': linkedin,
        'instagram': instagram,
        'resume': resume
    })


def download(request):
    # return render(request, 'portfolio/download.html')
    response = HttpResponse(content_type="application/zip")
    zipfile_name = 'protfolio'


    zip_file = zipfile.ZipFile(response, 'w')
    folders = ['img', 'js', 'css', 'html']
    for file_name in folders:
        folder_path = os.path.join(settings.MEDIA_ROOT, file_name)

        files = next(os.walk(folder_path), (None, None, []))[2]
        
        for file in files:
            curr_file_path = os.path.join(settings.MEDIA_ROOT, f'{file_name}/{file}')

            file_head, file_tail = os.path.split(curr_file_path)

            if file_name == 'html':
                zip_path = os.path.join('portfolio', file_tail)
            else:
                zip_path = os.path.join(f'portfolio/{file_name}', file_tail)
            
            zip_file.write(curr_file_path, zip_path)
    zip_file.close()
    response['Content-Disposition'] = f'attachment; filename={zipfile_name}'

    return response


def templates(request):
    return render(request, 'portfolio/templates.html')