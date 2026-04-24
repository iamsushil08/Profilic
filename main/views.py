from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Skill, Project, Education, Contact

def index(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-date')
    education = Education.objects.all().order_by('-year_start')

    # Group skills by category
    skill_groups = {
        'Frontend': skills.filter(category='frontend'),
        'Backend': skills.filter(category='backend'),
        'Tools & Others': skills.filter(category='tool'),
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(
                name=name, email=email,
                subject=subject, message=message
            )
            messages.success(request, "Message sent successfully! I'll get back to you soon.")
            return redirect('index')
        else:
            messages.error(request, "Please fill in all required fields.")

    context = {
        'about': about,
        'skill_groups': skill_groups,
        'projects': projects,
        'education': education,
    }
    return render(request, 'main/index.html', context)