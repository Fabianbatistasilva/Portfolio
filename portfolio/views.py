from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render


def home(request):
    return render(request, 'paginas/home.html')


def sobre(request):
    return render(request, 'paginas/sobre.html')


def healthcheck(request):
    return HttpResponse('ok', content_type='text/plain')


def oferta(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        name = request.POST.get('name', '').strip()
        descricao = request.POST.get('message', '').strip()

        if not email or not name or not descricao:
            messages.error(request, 'Erro: preencha todos os campos antes de enviar.')
            return render(request, 'paginas/form_oferta.html', {})

        from_email = settings.DEFAULT_FROM_EMAIL or settings.EMAIL_HOST_USER
        recipient = settings.DEFAULT_FROM_EMAIL or settings.EMAIL_HOST_USER

        if not from_email or not recipient:
            messages.error(request, 'O email do portfolio não está configurado no servidor.')
            return render(request, 'paginas/form_oferta.html', {})

        try:
            send_mail(
                'Contato recebido pelo portfolio',
                f'A/O {name} entrou em contato com {email}.\n\nMensagem:\n{descricao}',
                from_email,
                [recipient],
                fail_silently=False,
            )
        except Exception:
            messages.error(request, 'Não foi possível enviar sua mensagem agora. Tente novamente mais tarde.')
            return render(request, 'paginas/form_oferta.html', {})

        messages.success(request, 'Mensagem enviada com sucesso.')

    return render(request, 'paginas/form_oferta.html', {})
