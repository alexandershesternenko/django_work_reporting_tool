from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


from ReportingTool.models.directory import StructuralDivisions
from users.forms.sign_up import SignUpForm


def activateEmail(request, user, to_email):
    messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
        received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f"New account created: {user.username}. Please contact admin to activate it")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/sing_up.html', {'form': form})


def user_info(request):
    return render(request, 'user_info.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('user_info')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


# def password_reset_request(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             user_email = form.cleaned_data['email']
#             associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
#             if associated_user:
#                 subject = "Password Reset request"
#                 message = render_to_string("template_reset_password.html", {
#                     'user': associated_user,
#                     'domain': get_current_site(request).domain,
#                     'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
#                     'token': account_activation_token.make_token(associated_user),
#                     "protocol": 'https' if request.is_secure() else 'http'
#                 })
#                 email = EmailMessage(subject, message, to=[associated_user.email])
#                 if email.send():
#                     messages.success(request,
#                         """
#                         <h2>Password reset sent</h2><hr>
#                         <p>
#                             We've emailed you instructions for setting your password, if an account exists with the email you entered.
#                             You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address
#                             you registered with, and check your spam folder.
#                         </p>
#                         """
#                     )
#                 else:
#                     messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")
#
#             return redirect('homepage')
#
#         for key, error in list(form.errors.items()):
#             if key == 'captcha' and error[0] == 'This field is required.':
#                 messages.error(request, "You must pass the reCAPTCHA test")
#                 continue
#
#     form = PasswordResetForm()
#     return render(
#         request=request,
#         template_name="password_reset.html",
#         context={"form": form}
#         )
