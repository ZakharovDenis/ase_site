import smtplib
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .forms import UserForm
