import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from ase_site.data.models import GPS, GPSdata

# @csrf_exempt
# def index(request):
#     if request.method=="POST":
#         data = str(request.body)[2:-1]
#         with open('log.txt','a') as file:
#             file.write(data+'\n')
#             file.close()
#         return HttpResponse(data)
#     else:
#         try:
#             with open('log.txt','r') as file:
#                 try:
#                     for line in file:
#                         outline=line.split(',')
#                 except:
#                     return HttpResponse('empty file')
#                 file.close()
#         except:
#             return HttpResponse('no file(thats fine, just send POST)')
#         print(outline[0], outline[1])
#]         return render(request,'ase_site/geo/templates/map.html',{'x':outline[0],'y':outline[1]})


@csrf_exempt
def post_data(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            gps = GPS(id=json_data['id_gps'])
            json_data['id_gps'] = gps
            gps_data = GPSdata(
                **json_data
            )
            gps_data.save()
            return JsonResponse({'message': 'saved'})
        except KeyError:
            return JsonResponse({'message': 'invalid json'})
    return HttpResponse(status=200)


def get_data(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            gps_data = GPSdata.objects.all().filter(id_gps=json_data['id_gps'])
            gps_data = serializers.serialize('python', gps_data)
            return JsonResponse(gps_data, safe=False)
        except KeyError:
            return JsonResponse({'message': 'invalid json'})
        except ObjectDoesNotExist:
            return JsonResponse({'message': 'No such GPS'})
    return HttpResponse(status=200)
    
@csrf_exempt
def index(request):
    if request.method=="POST":
        data = str(request.body)[2:-1]
        with open('log.txt','a') as file:
            file.write(data+'\n')
            file.close()
        return HttpResponse(data)
    else:
        try:
            with open('log.txt','r') as file:
                try:
                    for line in file:
                        outline=line.split(',')
                except:
                    return HttpResponse('empty file')
                file.close()
        except:
            return HttpResponse('no file(thats fine, just send POST)')
        print(outline[0], outline[1])
        return render(request,'ase_site/geo/templates/map.html',{'x':outline[0],'y':outline[1]})
