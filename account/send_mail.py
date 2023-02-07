from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    full_link_server = f'http://34.16.136.138/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: \n{full_link} \n{full_link_server} ',
        'baialinovsultan@gmail.com',
        [user],
        fail_silently=False
    )


# def send_reset_email(user):
#     code = user.activation_code
#     email = user.email
#     send_mail('Letter with password reset code!', f"Your reset code {code}", 'from@eample.com',
#               [email, ], fail_silently=False)

def send_notification(user_email, order_id, price):
    send_mail(
        'uvedomlenie o sozdanii zakaza!',
        f"""vi sozdaly zakaz №{order_id}, \n polnaya stoimost' vashego zakaza: {price}. \nSpasibo za to chto vibraly nas!""",
        'from@example.com',
        [user_email],
        fail_silently=False
    )