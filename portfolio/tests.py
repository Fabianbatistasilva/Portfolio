from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    DEFAULT_FROM_EMAIL='portfolio@example.com',
    EMAIL_HOST_USER='portfolio@example.com',
    SECURE_SSL_REDIRECT=False,
    STORAGES={
        'default': {
            'BACKEND': 'django.core.files.storage.FileSystemStorage',
        },
        'staticfiles': {
            'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
        },
    },
)
class PortfolioViewTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contact_form_requires_all_fields(self):
        response = self.client.post(reverse('contato'), {
            'name': '',
            'email': '',
            'message': '',
        })
        self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertTrue(any('preencha todos os campos' in str(message) for message in messages))

    def test_contact_form_sends_email(self):
        response = self.client.post(reverse('contato'), {
            'name': 'Fabian',
            'email': 'fabian@example.com',
            'message': 'Olá, tudo bem?',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Fabian', mail.outbox[0].body)
