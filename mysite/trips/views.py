from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    # return HttpResponse("Hello World!!")
    output = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>另北的Django網頁</title>
    </head>
    <body>
      <h2>It's Works!</h2>
      <p>Hello World!! <em style="color:LightSeaGreen;">{current_time}</em></p>
    </body>
    </html>
    """.format(current_time=datetime.now())

    return HttpResponse(output)