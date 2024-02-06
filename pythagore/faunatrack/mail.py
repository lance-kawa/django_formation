# def send_my_email(request):
#     subject = 'Salut de Django'
#     message = 'Ceci est un message test envoyé par Django.'
#     email_from = 'your-email@example.com'
#     recipient_list = ['recipient1@example.com', 'recipient2@example.com']
#     send_mail(subject, message, email_from, recipient_list)
    
#     return HttpResponse("Email envoyé !")



# def send_html_email(request):
#     subject = "Salut de Django avec HTML"
#     body = """
#     <html>
#         <body>
#             <h1>Ceci est un test d'email HTML envoyé depuis Django</h1>
#             <p>C'est beaucoup plus joli avec du HTML, n'est-ce pas ?</p>
#         </body>
#     </html>
#     """
#     email = EmailMessage(
#         subject=subject,
#         body=body,
#         from_email='your-email@example.com',
#         to=['recipient@example.com'],
#         reply_to=['another@example.com'],
#         headers={'Content-Type': 'text/html'},  # Cet en-tête n'est pas nécessaire pour les e-mails HTML
#     )
#     email.content_subtype = 'html'  # Indique à Django que le corps du message est du HTML
#     email.send()

#     return HttpResponse("Email HTML envoyé !")

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.example.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'
