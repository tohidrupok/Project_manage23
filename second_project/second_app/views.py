from django.shortcuts import render
from django.http import HttpResponse

def course(request):
    return HttpResponse('''
                        <p><h1>This is course page.</h1></p>
                        <p><a href="/second_app/feedback/">Feedback</a></p>
                        <p><a href="/first_app/contact/">Contact</a></p>
                        <p><a href="/first_app/about/">About</a></p>
                        ''')
def feedback(request):
    return HttpResponse('''
                        <h1>This is feedback page.</h1>
                        <p><a href="/second_app/course/">Course</a></p>
                        <p><a href="/first_app/contact/">Contact</a></p>
                        <p><a href="/first_app/about/">About</a></p>
                        ''')