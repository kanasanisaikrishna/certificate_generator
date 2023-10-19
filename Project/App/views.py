from django.shortcuts import render,redirect, HttpResponse
from . models import *
from .forms import *

# myapp/views.py
import jwt
def home(request):
    return render(request,'home.html')
def verify(request):
    return render(request,'verify.html')

def certificate(request):
    pass


def add_teacher(request):
    if request.method == 'POST':
        form =TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.cleaned_data['tname']
            subject = form.cleaned_data['subject']
            t = Teacher(tname=teacher, subject=subject)
            t.save()
            return redirect('/')
    else:
        form = TeacherForm()

    return render(request, 'add_teacher.html', {'form': form})

def add_student(request):
    if request.method == 'POST':
        form =StudentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['sname']
            group = form.cleaned_data['group']
            teachers=form.cleaned_data['teachers']
            s = Student(sname=student, group=group,teachers=teachers)
            s.save()
            return redirect('/')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})

def teacher_details(request):
    teachers = Teacher.objects.all()
    selected_teacher = request.GET.get('teacher', None)
    students = []

    if selected_teacher:
        selected_teacher = int(selected_teacher)
        teacher = Teacher.objects.get(pk=selected_teacher)
        students = teacher.students.all()

    return render(request, 'teacher_details.html', {'teachers': teachers, 'students': students})

def student_details(request):
    students = Student.objects.all()
    selected_student = request.GET.get('student', None)
    teachers = []

    if selected_student:
        selected_student = int(selected_student)
        student = Student.objects.get(pk=selected_student)
        teachers = student.teachers.all()
    return render(request, 'student_details.html', {'students': students, 'teachers': teachers})


def generate_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            teacher = form.cleaned_data['teacher']
            student = form.cleaned_data['student']
            certificate = Certificate(teacher=teacher, student=student)
            certificate.save()
            return render(request, 'certificate.html', {'certificate': certificate})
    else:
        form = CertificateForm()

    return render(request, 'generate_certificate.html', {'form': form})

def verify_certificate(request, certificate_id):
    try:
        certificate = Certificate.objects.get(id=certificate_id)
        data = {
            'teacher_id': certificate.teacher.id,
            'student_id': certificate.student.id,
            
        }
        token = jwt.encode(data, 'django-insecure-n%7-+m4z#a%^u(g84ms(rjk$p7d&k@pd4=hlen7+&5cg(#j)e(', algorithm='HS256')
        return render(request, 'verify_certificate.html', {'token': token, 'certificate_id': certificate_id})
    except Certificate.DoesNotExist:
        return render(request, 'certificate_not_found.html')

def verify_certificate_with_token(request, certificate_id):
    if request.method == 'POST':
        token = request.POST.get('token')
        try:
            certificate = Certificate.objects.get(id=certificate_id)
            data = {
            'teacher_id': certificate.teacher.id,
            'student_id': certificate.student.id,
            
        }
            data = jwt.decode(token, 'django-insecure-n%7-+m4z#a%^u(g84ms(rjk$p7d&k@pd4=hlen7+&5cg(#j)e(', algorithms=['HS256'])
            teacher_id = data['teacher_id']
            student_id = data['student_id']

            # You can now use these values to verify the certificate as needed

            return HttpResponse(f'Certificate Verified for Teacher ID: {teacher_id} and Student ID: {student_id}')
        except jwt.ExpiredSignatureError:
            return HttpResponse('Token has expired. Certificate verification failed.')
        except jwt.DecodeError:
            return HttpResponse('Invalid token. Certificate verification failed')

    return render(request, 'verify_certificate_with_token.html')


