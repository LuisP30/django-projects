from celery import shared_task
from django.core.mail import EmailMessage
from PIL import Image, ImageFont, ImageDraw

@shared_task
def envia_email_com_anexo(email):
    coord_nome = (533, 630)
    imagem = Image.open()
    message = EmailMessage('Assunto', 'Essa é a minha mensagem', 'pimenta.lh2@gmail.com', [email])
    message.attach_file('certificado.png')