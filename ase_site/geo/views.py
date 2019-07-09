from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe

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