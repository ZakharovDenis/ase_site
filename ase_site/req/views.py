import json
import os
import smtplib
from io import BytesIO
from datetime import date

from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers

from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from ase_site.auth_core.models import User
from ase_site.data.models import Application, GPSdata
from .forms import MakeRequestForm


class ViewAllRequests(ListView):
    template_name = "ase_site/req/templates/posts.html"
    model = Application

    def get_queryset(self):
        qs = super(ViewAllRequests, self).get_queryset()
        return qs


def approve2(request, post_id):
    document = Document()
    document.add_picture('root_files/ase_logo.png', width=Inches(1.25))
    last_paragraph = document.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_heading('Дмитровское ш.,2,Москва', 3,)
    last_paragraph = document.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_heading('Запрос!', level=1)
    req = Application.objects.get(id=post_id)
    document.add_paragraph(req.post)
    if req.status == 0:
        req.title = req.title+"(обработан)"
        req.status = 1
        req.save()
    else:
        req.save()
    document.save('root_files/test'+post_id+'.docx')
    #fromaddr = "testase@mail.ru"
    fromaddr = "test_mail_temp2018@mail.ru"
    toaddr = "dr.interned@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ЗАПРОС"
    body = "Вам пришел запрос"
    msg.attach(MIMEText(body, 'plain'))
    filename = "test.docx"
    attachment = open('root_files/test'+post_id+'.docx', "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    #server.login(fromaddr, "adminase2018")
    server.login(fromaddr, "temp_pass2018")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    attachment.close()
    # time.sleep(15)
    os.remove("root_files/test"+post_id+".docx")
    return render(request, 'static/static_files/html/box.html', {'values': ['Запрос отправлен']})


def disapprove(request, post_id):
    req = Application.objects.get(id=post_id)
    req.current_level = req.current_level-1
    req.title = "Запрос №"+str(req.id)+"(отклонен)"
    req.save()
    return render(request, 'static/static_files/html/box.html', {'values': ['Запрос отклонены']})


def fill_word(data):
    document = Document('template.docx')
    paragraphs = []
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    paragraphs.append(paragraph)

    for p in paragraphs:
        if p.text in {str(i) for i in range(len(paragraphs))}:
            p.text = data[int(p.text)]
    return document


def create_request(request, application_type):
    if request.method == "POST":
        form = MakeRequestForm(request.POST)
        if form.is_valid():
            application, _ = Application.objects.update_or_create(
                application_type=application_type,
                status=2,
                density=form.cleaned_data['density'],
                volume=form.cleaned_data['volume'],
                delivery_date=request.POST.get('delivery_date'),
                delivery_time=request.POST.get('delivery_time'),
                car=form.cleaned_data['car'],
                manufacturer_org=form.cleaned_data['manufacturer_org'],
                performing_org=form.cleaned_data['performing_org'],
                application_sender=request.user,
                application_receiver=form.cleaned_data['application_receiver'],
                ocr_specialist=form.cleaned_data['ocr_specialist']
            )
            application.save()
            return redirect('/')
            return response
    else:
        form = MakeRequestForm()
    return render(request, "ase_site/req/templates/index.html", {"form": form})


def create_tuples(request, id_):
    application = Application.objects.get(id=id_)
    fields = application._meta.get_fields()
    data = []
    for f in fields:
        if not any(str(f.name) in s for s in ['status' 'id']):
            if str(f.name) == 'application_type':
                data.append(
                    (str(f.verbose_name), application.get_application_type_display()))
            else:
                data.append((str(f.verbose_name), str(
                    getattr(application, f.name))))
    return data


def get_coord_list(id_):
    application = Application.objects.get(id=id_)
    coord_list = GPSdata.objects.filter(id_gps=application.car.gps)
    final_coord = [val.get_tuple() for val in coord_list]
    return final_coord


def create_word(request, id_):
    application = Application.objects.get(id=id_)
    fields = application._meta.get_fields()
    data = []
    for f in fields:
        if not str(f.name) == 'status':
            if str(f.name) == 'application_type':
                data.append(application.get_application_type_display())
            else:
                data.append(str(getattr(application, f.name)))
    doc = fill_word(data[1:])
    data = BytesIO()
    doc.save(data)
    response = HttpResponse(data.getvalue(),
                            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="reports.docx"'
    return response


def create_beton_request(request):
    return create_request(request, 1)


def create_sand_request(request):
    return create_request(request, 2)


def create_PGS_request(request):
    return create_request(request, 3)


def show_application(request, id_):
    app = Application.objects.get(id=id_)
    full_application = create_tuples(request, id_)
    user = request.user
    coord_list = get_coord_list(id_)
    return render(request, "ase_site/req/templates/post.html", {'user': user, "application": full_application, 'app': app, "coord_list": coord_list})


def show_all_applications(request):
    user = request.user
    if user.level == 1:
        applications = Application.objects.filter(application_sender=user)
    elif user.level == 2:
        applications = Application.objects.all()
    elif user.level == 3:
        applications = Application.objects.filter(status=3)
    else:
        applications = Application.objects.all()
    applications = applications.order_by("-delivery_date")
    return render(request, "ase_site/req/templates/posts.html", {'object_list': applications})


def approve(request, id_):
    application = Application.objects.get(id=id_)
    application.status = 3
    application.save()
    return redirect('/request/'+str(id_))
