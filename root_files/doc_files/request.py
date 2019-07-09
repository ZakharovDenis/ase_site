from docx import Document
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from docx.shared import Inches
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from docx.enum.text import WD_ALIGN_PARAGRAPH
