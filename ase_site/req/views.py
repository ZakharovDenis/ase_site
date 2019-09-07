from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from ase_site.auth_core.models import User
from django.http import HttpResponse
from ase_site.req.models import SendRequest
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from docx import Document
from docx.shared import Inches
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os, time
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import MakeRequestForm
from django.http import HttpResponse
#from django.contrib.auth.models import User
from datetime import date
from ase_site.req.models import SendRequest
from docx import Document
from io import BytesIO

class ViewAllRequests(ListView):
    template_name="ase_site/req/templates/posts.html"
    model = SendRequest
    def get_queryset(self):
        qs=super(ViewAllRequests,self).get_queryset()
        # qs=qs.filter(
        #     #current_level = (self.request.user.level-1 or self.request.user.level)
        #     current_level=(self.request.user.level)
        # ).filter(firm=self.request.user.firm_name)
        #queryset=SendRequest.objects.filter(current_level=self.request.user.level)
        #return super(ViewAllRequests,self).get_queryset()
        return qs

def approve(request,post_id):
    document = Document()
    document.add_picture('root_files/ase_logo.png', width=Inches(1.25))
    last_paragraph = document.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_heading('Дмитровское ш.,2,Москва', 3,)
    last_paragraph = document.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_heading('Запрос!', level=1)
    req=SendRequest.objects.get(id=post_id)
    document.add_paragraph(req.post)
    if req.status==0:
        req.title=req.title+"(обработан)"
        req.status=1
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
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    #server.login(fromaddr, "adminase2018")
    server.login(fromaddr, "temp_pass2018")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    attachment.close()
    #time.sleep(15)
    os.remove("root_files/test"+post_id+".docx")
    return render(request,'static/static_files/html/box.html', {'values':['Запрос отправлен']})

def disapprove(request,post_id):
    req=SendRequest.objects.get(id=post_id)
    req.current_level=req.current_level-1
    req.title="Запрос №"+str(req.id)+"(отклонен)"
    req.save()
    return render(request,'static/static_files/html/box.html', {'values':['Запрос отклонены']})

def fill_word(data):
    doc=Document('template.docx')
    if doc.tables!=[]:
        for table in doc.tables:
            for cell in table._cells:
                for paragraph in cell.paragraphs:
                    tmp=paragraph.text.lower()
                    for i in range(len(data)):
                        comp='var'+str(i+1)
                        if comp == tmp.lower():
                            tmp=tmp.replace(comp,data[i])
                            paragraph.text=tmp
    return doc

def CreateRequest(request):
    if request.method=="POST":
        form=MakeRequestForm(request.POST)
        if form.is_valid():
            data=[]
            for i in form.fields:
                data.append(request.POST.get(str(i)))
            doc=fill_word(data)
            form.date=date.today()
            form.save()
            data = BytesIO()
            doc.save(data)
            response = HttpResponse(data.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="reports.docx"'
            redirect('/')
            return redirect('/')
            return response
    else:   
        form=MakeRequestForm()
    return render(request, "ase_site/req/templates/index.html", {"form": form})
