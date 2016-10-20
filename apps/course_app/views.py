from django.shortcuts import render, redirect
from.models import Courses

def index(request):
	context = {
	'courses' : Courses.objects.all()
	}
	return render(request,"course_app/index.html", context)

def course(request):
	Courses.objects.create(course_name = request.POST['name'],description=request.POST['description'])
	# request.session['course_name'] = request.POST['name']
	return redirect('/')

def remove(request,id):
	 
	context = {'id' : id,
				'course_name' : Courses.objects.get(id=id),
				'description' : Courses.objects.get(id=id)
				
			 }
	return render(request,"course_app/destroy.html", context)

def destroy(request,id):
	course = Courses.objects.get(id=id)
	course.delete()
	# Courses.objects.destroy(course)
	return redirect('/')


