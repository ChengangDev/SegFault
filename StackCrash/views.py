from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from StackCrash.models import History
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from StackCrash.serializers import HistorySerializer

def index(request):
    return HttpResponse("Great.")

@csrf_exempt
@api_view(['GET', 'POST'])
def history(request):
    print(request)
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            # Redirect to a success page.
            print(username +  ' auth success.')
        else:
            print(username + ' auth failed.')
            return Response(status=401)
        start = request.GET.get('start', '')
        end = request.GET.get('end', '')
        history = History.objects.all()
        if start != '':
            start_time = timezone.datetime.strptime(start, '%Y-%m-%d')
            history = history.filter(date__gte=start_time)
        if end != '':
            end_time = timezone.datetime.strptime(end, '%Y-%m-%d') + timezone.timedelta(days=1)
            history = history.filter(date__lt=end_time)
        #history.reverse()
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            # Redirect to a success page.
            print(username + ' auth success.')
        else:
            print(username + ' auth failed.')
            return Response(status=401)

        print(request.POST.get('title'))

        title = request.POST.get('title', '')
        url = request.POST.get('url', '')
        if url == '':
            return Response(status=406)

        count = History.objects.filter(
            date__date=timezone.datetime.today()
        ).filter(
            url=url
        ).count()

        if count > 0:
            print('Url is already visited today.')
            return Response(status=208)

        hist = History(date=timezone.now(), title=title, url=url)
        hist.save()

        return Response(status=200)

    return Response(status=406)

@api_view(['POST'])
def history_search(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

    return