from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('teacher_details/',views.teacher_details,name='teacher_details'),
    path('student_details/',views.student_details,name='student_details'),
    path('generate_certificate/',views.generate_certificate,name='generate_certificate'),
    path('verify_certificate/<int:certificate_id>/',views.verify_certificate,name='verify_certificate'),
    path('verify_certificate_with_token/<int:certificate_id>/',views.verify_certificate_with_token,name='verify_certificate_with_token'),
    path('add_teacher/',views.add_teacher,name='add_teacher'),
    path('add_student/',views.add_student,name='add_student'),
    
]