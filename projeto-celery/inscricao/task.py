from celery import shared_task
from django.core.mail import EmailMessage
from PIL import Image, ImageFont, ImageDraw
import os

@shared_task
def envia_email_com_anexo(email, nome):
    # PILLOW
    coord_nome = (533, 630)
    imagem = Image.open(r'/home/luis/Área de Trabalho/django-projects/projeto-celery/templates/static/img/certificado.png')
    caminho_fonte = r'/home/luis/Área de Trabalho/django-projects/projeto-celery/templates/static/font/Montserrat/Montserrat-VariableFont_wght.ttf'
    font = ImageFont.truetype(caminho_fonte, 54)
    cor_fonte = (5, 53, 93)
    desenho = ImageDraw.Draw(imagem)
    desenho.text(coord_nome, nome, font=font, fill=cor_fonte)
    # Salvando a imagem com um novo nome para evitar conflitos
    output_path = '/home/luis/Área de Trabalho/django-projects/projeto-celery/templates/static/img/seu_certificado.png'
    imagem.save(output_path)
    # ENVIANDO EMAIL
    message = EmailMessage('Certificado', 'Aqui está o seu certificado de inscrição', 'pimenta.lh2@gmail.com', [email])
    message.attach_file(output_path)
    message.send()

    # Opcionalmente, remover o arquivo após o envio
    os.remove(output_path)