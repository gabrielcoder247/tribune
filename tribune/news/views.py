from django.http  import HttpResponse
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
import datetime as dt

# Create your views here.
def welcome(request):

    return render(request, 'welcome.html')
    # return HttpResponse('Welcome to the Moringa Tribune')

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def news_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def past_days_news(request,past_date):


    try:
            # Converts data from the string Url
            date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
            # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    return render(request, 'all-news/past-news.html', {"date": date})    