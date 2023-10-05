from django.shortcuts import render
from .models import Attend

from django.db.models import Q

from django.http import HttpResponseRedirect, HttpResponse
import json

def homepage(request):
    context = {
        'var1': 'This is to handle input',
        'current_email': 'Not defined'
    }
    return render(request, 'homepage.html', context)

def attend(request):
    ATTN_Number = int(request.data.get('ATTN_Number', 0))
    Movie_Name = request.data.get('Movie_Name', '')
    Seat_Number = request.data.get('Seat_Number', '')
    Show_Time = request.data.get('Show_Time', '')

    if ATTN_Number <= 0 or not Movie_Name:
        return HttpResponse(f"Invalid data provided", status=400)

    # Create a new Attend record
    attend = Attend(ATTN_Number=ATTN_Number, Movie_Name=Movie_Name, Seat_Number=Seat_Number, Show_Time=Show_Time)
    attend.save()

    return HttpResponse(f"Attendance recorded successfully", status=201)

def attend_summary(request):
    attendances = Attend.objects.all()
    data = [
        f"Attendance: {attendance.ATTN_Number} for Movie: {attendance.Movie_Name}, Seat: {attendance.Seat_Number}, Show Time: {attendance.Show_Time}"
        for attendance in attendances
    ]
    response_text = "\n".join(data)
    return HttpResponse(response_text, content_type='text/plain')

