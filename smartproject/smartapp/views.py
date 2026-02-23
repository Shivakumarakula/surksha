from multiprocessing.connection import Client
from django.shortcuts import render

# Create your views here.
def openingpage(request):
    # Upload the audio file and send the WhatsApp message
    # file_path = "C:/Users/akula/OneDrive/Desktop/projects/smart_Device_project/smartproject/media/audio_history/2025/03/20/recording_1742486562251.webm"  # Replace with your local file path
    # audio_url = upload_file(file_path)
    # num="9390370155"
    # # msg="bvjabdpbj"
    # # sw(num,msg)
    # msg="bhvlajbvjbds;j"
    # num = "9390370155"  # Phone number without country code
    # send_audio_via_whatsapp(num,msg)
    # if audio_url:
    #     send_whatsapp_message(audio_url)
    #     print("success...!!!!!!!!!!!!!111")
    # else:
    #     print("File upload failed.")
    # testing()
    # subject = "Your Recorded Audio File"
    # body = "Please find the attached audio file recorded on your device."
    # mail="akulashivaakulashiva@gmail.com"
    # send_email(mail,body,subject)
    # gcd(7)
    # Define the latitude and longitude for the map location
    # latitude = "18.530304"  # Replace with your desired latitude
    # longitude = "79.627217"  # Replace with your desired longitude

    #             # Create a Google Maps link using the latitude and longitude
    # maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

    #             # Send email to each contact
    # subject1 = "SMART-RING Alert"
    # message = f"This is an emergency alert. Your friend needs your help! Please see the location on the map: {maps_link}"
    # send_email_static(subject1,message)

    # Send the SMS
    # send_sms()
    # sms()
    # sms1()
    # make_phone_call(+918688591249)
    # whtas()
    # testing()
    return render(request,'openingpage.html')

def homepage2(request):
    return render(request, 'homepage2.html')

def login(request):
    return render(request, 'loginpage.html')


def signup(request):
    return render(request, 'signup.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Device, mainuser

def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    try:
        current_user = mainuser.objects.get(user_id=user_id)
        # Fetch only devices associated with the current user
        devices = Device.objects.filter(user=current_user)
        return render(request, 'dashboard1.html', {'devices': devices})
    except mainuser.DoesNotExist:
        return redirect('login')

# def device_detail2(request, device_id):
#     user_id = request.session.get('user_id')
#     if not user_id:
#         return redirect('login')

#     try:
#         current_user = mainuser.objects.get(user_id=user_id)
#         device = get_object_or_404(Device, device_id=device_id, user=current_user)
#         return render(request, 'device_details2.html', {'device': device, 'user':current_user.user_name})
#     except mainuser.DoesNotExist:
#         return redirect('login')

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Device, mainuser, History
import os

def device_detail2(request, device_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    try:
        current_user = mainuser.objects.get(user_id=user_id)
        device = get_object_or_404(Device, device_id=device_id, user=current_user)
        # Store device_id in session for the voice assistant
        request.session['device_id'] = device_id
        return render(request, 'device_details2.html', {'device': device, 'user':current_user.user_name})
    except mainuser.DoesNotExist:
        return redirect('login')
    



from pydub import AudioSegment
import os

# @csrf_exempt
# def handle_voice_assistant(request):
#     print("1111111")
#     if request.method == 'POST':
#         print("22222222222")
#         user_id = request.session.get('user_id')
#         device_id = request.session.get('device_id')
#         audio_file = request.FILES.get('audio')

#         if not user_id or not device_id or not audio_file:
#             return JsonResponse({'error': 'Missing data'}, status=400)
#         print("3333333333")
#         current_user = mainuser.objects.get(user_id=user_id)
#         device = Device.objects.get(device_id=device_id, user=current_user)
#         print("444444444")
#         # Save temporarily as WebM, then convert to MP3
#         temp_path = os.path.join(settings.MEDIA_ROOT, 'temp.webm')
#         with open(temp_path, 'wb') as f:
#             for chunk in audio_file.chunks():
#                 f.write(chunk)
#         audio = AudioSegment.from_file(temp_path)
#         mp3_path = os.path.join(settings.MEDIA_ROOT, 'audio_history', f'recording_{device_id}.mp3')
#         audio.export(mp3_path, format='mp3')
#         os.remove(temp_path)
#         print("55555555555555")

#         # Save to History
#         with open(mp3_path, 'rb') as f:
#             history_entry = History(user=current_user, device=device)
#             history_entry.audio_file.save(f'recording_{device_id}.mp3', f)
#             history_entry.save()
#         print("66666666666")

#         return JsonResponse({'message': 'Audio saved', 'id': history_entry.id})
#     print("777777777777777")
#     return JsonResponse({'error': 'Invalid request'}, status=400)

# views.py (unchanged, just for reference)
# @csrf_exempt
# def handle_voice_assistant(request):
#     if request.method == 'POST':
#         user_id = request.session.get('user_id')
#         device_id = request.session.get('device_id')
#         audio_file = request.FILES.get('audio')

#         if not user_id or not device_id or not audio_file:
#             return JsonResponse({'error': 'Missing user_id, device_id, or audio file'}, status=400)

#         try:
#             current_user = mainuser.objects.get(user_id=user_id)
#             device = Device.objects.get(device_id=device_id, user=current_user)
#             history_entry = History(user=current_user, device=device, audio_file=audio_file)
#             history_entry.save()
#             return JsonResponse({
#                 'message': 'Audio recorded and saved successfully',
#                 'id': history_entry.id,
#                 'file_path': history_entry.audio_file.url,
#                 'timestamp': history_entry.recorded_at.isoformat()
#             })
#         except (mainuser.DoesNotExist, Device.DoesNotExist):
#             return JsonResponse({'error': 'Invalid user or device'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': f'Error saving audio: {str(e)}'}, status=500)
#     return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def handle_voice_assistant(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        device_id = request.session.get('device_id')
        audio_file = request.FILES.get('audio')

        if not user_id or not device_id or not audio_file:
            return JsonResponse({'error': 'Missing user_id, device_id, or audio file'}, status=400)

        try:
            current_user = mainuser.objects.get(user_id=user_id)
            device = Device.objects.get(device_id=device_id, user=current_user)

            # Save the WebM file directly
            history_entry = History(user=current_user, device=device, audio_file=audio_file)
            history_entry.save()

            return JsonResponse({
                'message': 'Audio recorded and saved successfully as WebM',
                'id': history_entry.id,
                'file_path': history_entry.audio_file.url,
                'timestamp': history_entry.recorded_at.isoformat()
            })
        except (mainuser.DoesNotExist, Device.DoesNotExist):
            return JsonResponse({'error': 'Invalid user or device'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error saving audio: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# @csrf_exempt
# def handle_voice_assistant(request):
#     if request.method == 'POST':
#         user_id = request.session.get('user_id')
#         device_id = request.session.get('device_id')
#         audio_file = request.FILES.get('audio')

#         if not user_id or not device_id or not audio_file:
#             return JsonResponse({'error': 'Missing user_id, device_id, or audio file'}, status=400)

#         try:
#             # Get user and device from session data
#             current_user = mainuser.objects.get(user_id=user_id)
#             device = Device.objects.get(device_id=device_id, user=current_user)

#             # Save the audio file to the History table
#             history_entry = History(user=current_user, device=device, audio_file=audio_file)
#             history_entry.save()

#             return JsonResponse({
#                 'message': 'Audio recorded and saved successfully',
#                 'id': history_entry.id,
#                 'file_path': history_entry.audio_file.url
#             })
#         except (mainuser.DoesNotExist, Device.DoesNotExist):
#             return JsonResponse({'error': 'Invalid user or device'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': f'Error saving audio: {str(e)}'}, status=500)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)

# def dashboard(request):
#     # Ensure the device_id is in the session
#     user_id = request.session.get('user_id')
#     if  user_id:
        
#     # Get the device associated with the device_id
#         # device = Device.objects.get(user_id=user_id)
#         devices = Device.objects.all()  # Fetch all devices
#         return render(request, 'dashboard1.html', {'devices': devices})
   
def forgotpass(request):
    return render(request,'password_reset_form.html')

def about(request):
    return render(request, 'aboutpage.html')

def services(request):
    return render(request, 'services.html')


import base64

def encode_password(password):
    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    return encoded_password




def decode_password(encoded_password):
    try:
        decoded_password = base64.b64decode(encoded_password).decode('utf-8')
    except UnicodeDecodeError:
        # Handle the case where decoding fails due to invalid characters
        decoded_password = "Unable to decode password"
    return decoded_password


from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import mainuser 
from django.conf import settings
# def user_register(request):
#     if request.method == 'POST':
#         user_name = request.POST['username']
#         print(user_name)
#         # user_lname = request.POST['lname']
#         user_mail = request.POST['email']
#         user_password = request.POST['password']
#         # user_dob = request.POST['dob']
#         user_phonenumber = request.POST['phone']
#         # en_password = encode_password(user_password)
#         en_password=encode_password(user_password)
#         print(user_password)
#         print(en_password)
#         # Check if a user with the same email already exists
#         if mainuser.objects.filter(user_mail=user_mail).exists():
#             error_message = "A user with this email already exists. Please use a different email."
#             return render(request, 'signup.html', {'error_message': error_message})

#         # Create a new User instance
#         user = User.objects.create_user(username=user_name, email=user_mail, password=user_password)
#         user.user_name = user_name
#         # user.last_name = user_lname
#         user.is_active = False  # User is inactive until email confirmation
#         user.save()

#         # Create a new MainUser instance
#         new_user = mainuser(
          
#             # user_fname=user_fname,
#             # user_lname=user_lname,
#             user_name=user_name,
#             user_mail=user_mail,
#             user_password=en_password,
#             # user_dob=user_dob,
#             user_phonenumber=user_phonenumber
#         )
#         new_user.save()

#         # Send confirmation email
#         current_site = get_current_site(request)
#         mail_subject = 'Activate your account.'
#         message = render_to_string('acc_active_email.html', {
#             'user': user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             'token': default_token_generator.make_token(user),
#         })
#         # send_mail(mail_subject, message, 'settings.EMAIL_HOST_USER', [user_mail])
#         email_from = settings.EMAIL_HOST_USER
#             # subject = 'Feedback from User'
#         html_message = f"""
#             {message}
#             """
#         sendemail = EmailMessage(mail_subject, html_message, email_from, [user_mail])
#         sendemail.content_subtype = 'html'  # Set the content type to HTML
#         sendemail.send()
#         return render(request,'requestdone.html',{'user':new_user})
#         # return HttpResponse('Please confirm your email address to complete the registration')
#         # return render(request, 'acc_active_email.html', {'newuser': new_user})

#     else:
#         return render(request, 'signup.html')



# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return render(request, 'gotologin.html')
#         # return HttpResponse('Thank you for your email confirmation. Your account is now active. You can log in.')
#     else:
#         return HttpResponse('Activation link is invalid!')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

def user_register(request):
    if request.method == 'POST':
        # Get user data from form
        user_name = request.POST.get('username')
        user_mail = request.POST.get('email')
        user_password = request.POST.get('password')
        user_phonenumber = request.POST.get('phone')
        
        # Encode password function (assuming you have this function defined)
        en_password = encode_password(user_password)
        
        # Check if a user with the same email already exists
        if mainuser.objects.filter(user_mail=user_mail).exists():
            error_message = "A user with this email already exists. Please use a different email."
            return render(request, 'signup.html', {'error_message': error_message})

        # Create User instance in auth system and mainuser in custom model
        user = User.objects.create_user(username=user_name, email=user_mail, password=user_password)
        user.is_active = False  # Set inactive until email confirmation
        user.save()

        # Create a new MainUser instance
        new_user = mainuser(
            user_name=user_name,
            user_mail=user_mail,
            user_password=en_password,
            user_phonenumber=user_phonenumber
        )
        new_user.save()

        # Prepare and send confirmation email
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        
        email_from = settings.EMAIL_HOST_USER
        sendemail = EmailMessage(mail_subject, message, email_from, [user_mail])
        sendemail.content_subtype = 'html'  # Set the content type to HTML
        sendemail.send()

        # Render a confirmation page
        return render(request, 'requestdone.html', {'user': new_user})

    else:
        return render(request, 'signup.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # mainuser.is_active=True
        # mainuser.save()
        return render(request, 'gotologin.html')
    else:
        return HttpResponse('Activation link is invalid!')




def login_operation(request):
    error_message1 = None
    error_message2 = None
    
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_pass = request.POST.get('password')

        try:
            # Retrieve user based on email
            user = mainuser.objects.get(user_mail=user_email)
            authuser=User.objects.get(email=user_email)
            stored_password=decode_password(user.user_password)
            # stored_password= base64.b64decode(user.user_password).decode('utf-8')
            # stored_password=decode_password(user.user_password)
            print(stored_password)
            if user_pass == stored_password:
                request.session['user_id'] = user.user_id
            
            else:
                 error_message1 = "Invalid password."
                 return render(request, 'loginpage.html', {'error_message1': error_message1})
            if authuser.is_active==True:
                
                # return redirect('home')
                success_message = "Successfully logged in."
                # return render(request, 'dashboard1.html',{'success_message': success_message, 'username':user.user_name})
                return redirect('dashboard')
            else:
                 error_message1 = "Invalid user details."
                 return render(request, 'loginpage.html', {'error_message1': error_message1})
            # Check if the email and password match
            # if check_password(user_pass, user.user_password):
            #     # Authentication succeeds, store user ID in session and redirect to profile page
            #     request.session['user_id'] = user.user_id
            #     return redirect('home')
            # else:
                # Password does not match, render the login page with error message
                # error_message1 = "Invalid password."
                # return render(request, 'login.html', {'error_message1': error_message1})
          
        except mainuser.DoesNotExist:
            # User with provided email does not exist, render the login page with error message
            error_message2 = "User with this email does not exist."
            return render(request, 'loginpage.html', {'error_message2': error_message2})

    else:
        # GET request, render the login page
        return render(request, 'loginpage.html')



from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from .models import mainuser
from .tokens import account_activation_token
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature

def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = mainuser.objects.get(user_mail=email)
            signer = TimestampSigner()
            token = signer.sign(account_activation_token.make_token(user))
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))
            mail_subject = 'Reset your password'
            message = f"""\
            <html>
            <body>
            <p>Hi { user.user_name }</p>
            <p>Click the link below to reset your password:</p>
            <p><a href="{reset_link }">{ reset_link }</a></p>
            </body>
            </html>
            """
            emailm = EmailMessage(
                mail_subject,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            emailm.content_subtype = 'html'
            emailm.send(fail_silently=False)
            return redirect('password_reset_done')
        except mainuser.DoesNotExist:
            return render(request, "password_reset_form.html", {'error': 'Email does not exist'})
    return render(request, "password_reset_form.html")

def password_reset_done(request):
    return render(request, "password_reset_done.html")

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = mainuser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, mainuser.DoesNotExist):
        user = None
    
    if user is not None:
        signer = TimestampSigner()
        try:
            # Check if token is valid and not expired (2-minute limit)
            original_token = signer.unsign(token, max_age=300)  # 120 seconds = 2 minutes
            if account_activation_token.check_token(user, original_token):
                if request.method == "POST":
                    new_password = request.POST.get("new_password")
                    en_password=encode_password(new_password)
                    user.user_password = en_password  # Hash the password before saving
                    user.save()
                    return redirect('password_reset_complete')
                return render(request, 'password_reset_confirm.html', {'uidb64': uidb64, 'token': token})
        except (SignatureExpired, BadSignature):
            return redirect('password_reset_invalid')
    return redirect('password_reset_invalid')

def password_reset_complete(request):
    return render(request, "password_reset_complete.html")

def password_reset_invalid(request):
    return render(request, "password_reset_invalid.html")



# from django.shortcuts import render, redirect

# def dashboard(request):
#     # Check if device has been activated, or set False if not set
#     device_activated = request.session.get('device_activated', False)
#     return render(request, 'dashboard1.html', {'device_activated': device_activated})

def activate_device(request):
    # Logic to activate the device, e.g., calling an API, etc.
    request.session['device_activated'] = True
    return redirect('dashboard')


import vonage
def sms():
    client = vonage.Client(key="7d0a83d9", secret="IynPfYVbLGQbygJ4")
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": "SmartRing-device",
            "to": "917093810932",
            "text": "A text message sent using the Nexmo SMS API",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        
        
        
        
        from twilio.rest import Client

# Your Twilio credentials
def sms1():
    account_sid = ''    # Replace with your Account SID
    auth_token = ''      # Replace with your Auth Token
    client = Client(account_sid, auth_token)

    # Sending the SMS
    message = client.messages.create(
        body="Hello from Python!",       # The message text
        from_='+919390370155',             # Replace with your Twilio number
        to='+919390370155'                 # Replace with the recipient’s number
    )

    print("Message sent! SID:", message.sid)





# # views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Device, Contact

# def search_device(request):
#     device = None
#     contacts = None
#     if request.method == "POST":
#         device_name = request.POST.get("device_name")
#         device = Device.objects.filter(name=device_name).first()
#         if device:
#             contacts = device.contacts.all()
    
#     return render(request, "search_device.html", {"device": device, "contacts": contacts})

# def edit_contact(request, contact_id):
#     contact = get_object_or_404(Contact, id=contact_id)
#     if request.method == "POST":
#         contact.email = request.POST.get("email")
#         contact.phone = request.POST.get("phone")
#         contact.save()
#         return redirect("search_device")
    
#     return render(request, "edit_contact.html", {"contact": contact})

# def add_contact_to_device(request, device_id):
#     device = get_object_or_404(Device, id=device_id)
#     if request.method == "POST":
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         Contact.objects.create(device=device, email=email, phone=phone)
#         return redirect("search_device")
    
#     return render(request, "add_contact.html", {"device": device})


# from django.shortcuts import render, redirect
# from .models import Device
# from django.contrib import messages

# def add_device(request):
#     if request.method == 'POST':
#         device_name = request.POST.get('device_name')
#         device_type = request.POST.get('device_type')

#         # Check if device name is unique
#         if Device.objects.filter(name=device_name).exists():
#             messages.error(request, 'Device name must be unique.')
#         else:
#             # Create a new Device instance and save it
#             new_device = Device(name=device_name, type=device_type)
#             new_device.save()
#             messages.success(request, 'Device added successfully.')
#             return redirect('add_device')  # Redirect to the same page or another page after saving

#     devices = Device.objects.all()  # Fetch all devices for display
#     return render(request, 'dashboard1.html', {'devices': devices})


# from django.shortcuts import render, redirect
# from .models import Device, Contact
# from django.contrib import messages

# def add_device(request):
#     if request.method == 'POST':
#         device_name = request.POST.get('device_name')
#         device_type = request.POST.get('device_type')

#         # Check if device name is unique
#         if Device.objects.filter(name=device_name).exists():
#             messages.error(request, 'Device name must be unique.')
#         else:
#             # Create a new Device instance and save it
#             new_device = Device(name=device_name, type=device_type)
#             new_device.save()
#             request.session['device_name'] = new_device.name
#             messages.success(request, 'Device added successfully.')
#             return render(request, 'dashboard1.html') # Redirect to the add device page

#     return render(request, 'dashboard1.html')


# def add_contact(request):
#     if request.method == 'POST':
#         contact_email = request.POST.get('contact_email')
#         contact_phone = request.POST.get('contact_phone')
#         device_name = request.session.get('device_name')

#         if device_name:
#             # Retrieve the device using the session data
#             device = Device.objects.get(name=device_name)
#             # Check if the contact already exists
#             if Contact.objects.filter(email=contact_email).exists():
#                 messages.error(request, 'Contact email must be unique.')
#             else:
#                 # Create a new Contact instance and save it
#                 new_contact = Contact(device=device, email=contact_email, phone=contact_phone)
#                 new_contact.save()
#                 messages.success(request, 'Contact added successfully.')
#         else:
#             messages.error(request, 'No device selected. Please add a device first.')

#     return render(request, 'add_contact.html')


from django.shortcuts import render, redirect
from .models import Device

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Device

# @login_required  # Ensure only logged-in users can access this view
from django.shortcuts import render, redirect
from .models import Device, mainuser

from django.shortcuts import render, redirect
from .models import Device, mainuser

def add_device(request):
    warning_message = None
    device_id = None

    # Sample catalog of available devices with prices
    available_devices = [
        {
            'name': 'Smart Sensor X1',
            'type': 'sensor',
            'image': 'images/ring.webp',
            'description': 'A high-precision sensor for real-time monitoring.',
            'price': 2500  # Price in rupees
        },
        {
            'name': 'Actuator Pro',
            'type': 'actuator',
            'image': 'images/ring2.jpg',
            'description': 'A robust actuator for automated control systems.',
            'price': 3500
        },
        {
            'name': 'Controller Hub',
            'type': 'controller',
            'image': 'images/ring3.jpg',
            'description': 'A central hub to manage your IoT devices.',
            'price': 5000
        }
    ]

    # Get user_id from session
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    try:
        current_user = mainuser.objects.get(user_id=user_id)
        existing_device = Device.objects.filter(user=current_user).first()
        if existing_device:
            device_id = existing_device.device_id
            warning_message = f"You already have a device (ID: {device_id}). Manage it from the dashboard."
            return render(request, 'add_device.html', {
                'warning_message': warning_message,
                'device_id': device_id
            })
    except mainuser.DoesNotExist:
        return redirect('login')

    return render(request, 'add_device.html', {
        'available_devices': available_devices
    })
    

from django.shortcuts import render, redirect
from .models import Device, mainuser

import razorpay
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Device, mainuser
import hmac
import hashlib

# # Initialize Razorpay client (replace with your test/live keys)
# RAZORPAY_KEY_ID = 'your_razorpay_key_id'  # Replace with your Razorpay Key ID
# RAZORPAY_KEY_SECRET = 'your_razorpay_key_secret'  # Replace with your Razorpay Key Secret
# client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

from django.conf import settings
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def device_details(request, device_name):
    # Sample device details (could be replaced with a database model)
    device_data = {
        'Smart Sensor X1': {
            'name': 'Smart Sensor X1',
            'type': 'sensor',
            'image': 'images/ring.webp',
            'description': 'A high-precision sensor for real-time monitoring with advanced features.',
            'price': 2500,  # Price in rupees
            'customizations': ['Red', 'Blue', 'Black']
        },
        'Actuator Pro': {
            'name': 'Actuator Pro',
            'type': 'actuator',
            'image': 'images/ring2.jpg',
            'description': 'A robust actuator for automated control systems with durable build.',
            'price': 3500,
            'customizations': ['Silver', 'Gold']
        },
        'Controller Hub': {
            'name': 'Controller Hub',
            'type': 'controller',
            'image': 'images/ring3.jpg',
            'description': 'A central hub to manage your IoT devices with seamless integration.',
            'price': 5000,
            'customizations': ['White', 'Gray']
        }
    }

    # Check if user is logged in
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    # Verify user exists and doesn't already have a device
    try:
        current_user = mainuser.objects.get(user_id=user_id)
        if Device.objects.filter(user=current_user).exists():
            return redirect('add_device')  # Redirect if user already has a device
    except mainuser.DoesNotExist:
        return redirect('login')

    # Get device details or redirect if not found
    device = device_data.get(device_name)
    if not device:
        return redirect('add_device')

    # Handle form submission (customization, address, and payment initiation)
    if request.method == 'POST' and 'customization' in request.POST:
        customization = request.POST.get('customization')
        address = request.POST.get('address')

        if not address:
            return render(request, 'device_details.html', {
                'device': device,
                'error_message': 'Please provide a delivery address.'
            })

        # Validate customization
        if customization not in device['customizations']:
            return render(request, 'device_details.html', {
                'device': device,
                'error_message': 'Invalid customization option selected.'
            })

        # Store customization and address in session for use after payment
        request.session['device_name'] = device['name']
        request.session['device_type'] = device['type']
        request.session['customization'] = customization
        request.session['address'] = address

        # Create Razorpay order
        order_amount = device['price'] * 100  # Convert rupees to paise
        order_currency = 'INR'
        order_data = {
            'amount': order_amount,
            'currency': order_currency,
            'payment_capture': 1  # Auto-capture payment
        }
        razorpay_order = client.order.create(data=order_data)
        razorpay_order_id = razorpay_order['id']

        # Render template with Razorpay Checkout details
        return render(request, 'device_details.html', {
            'device': device,
            'customization': customization,
            'address': address,
            'razorpay_order_id': razorpay_order_id,
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'razorpay_amount': order_amount,
            'callback_url': request.build_absolute_uri('/payment/verify/')
        })

    # Initial page load: Show device details and form
    return render(request, 'device_details.html', {
        'device': device
    })

@csrf_exempt
def payment_verify(request):
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_signature = request.POST.get('razorpay_signature')

        # Verify payment signature
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': razorpay_signature
        }
        try:
            client.utility.verify_payment_signature(params_dict)
        except razorpay.errors.SignatureVerificationError:
            return render(request, 'payment_failure.html', {
                'error': 'Payment verification failed. Please try again.'
            })

        # Payment successful: Add device to user's account
        user_id = request.session.get('user_id')
        current_user = mainuser.objects.get(user_id=user_id)
        device_name = request.session.get('device_name')
        device_type = request.session.get('device_type')
        customization = request.session.get('customization')
        address = request.session.get('address')

        # Create and save the device
        new_device = Device(
            name=device_name,
            type=device_type,
            user=current_user
        )
        new_device.save()
        request.session['device_id'] = new_device.device_id
        
        # Redirect to success page with order details
        return render(request, 'payment_success.html', {
            'device_name': device_name,
            'customization': customization,
            'address': address,
            'amount': new_device.price if hasattr(new_device, 'price') else request.session.get('device_price', 0) / 100,  # Assuming price stored elsewhere or passed
            'payment_id': razorpay_payment_id
        })

        # Optionally, clear session data or store in an Order model
        # del request.session['device_name']
        # del request.session['device_type']
        # del request.session['customization']
        # del request.session['address']

        # return redirect('dashboard')

    return redirect('add_device')

# def device_details(request, device_name):
#     # Sample device details (in practice, fetch from available_devices or a model)
#     device_data = {
#         'Smart Sensor X1': {
#             'name': 'Smart Sensor X1',
#             'type': 'sensor',
#             'image': 'images/sensor_x1.webp',
#             'description': 'A high-precision sensor for real-time monitoring with advanced features.',
#             'price': 2500,
#             'customizations': ['Red', 'Blue', 'Black']
#         },
#         'Actuator Pro': {
#             'name': 'Actuator Pro',
#             'type': 'actuator',
#             'image': 'images/actuator_pro.webp',
#             'description': 'A robust actuator for automated control systems with durable build.',
#             'price': 3500,
#             'customizations': ['Silver', 'Gold']
#         },
#         'Controller Hub': {
#             'name': 'Controller Hub',
#             'type': 'controller',
#             'image': 'images/controller_hub.webp',
#             'description': 'A central hub to manage your IoT devices with seamless integration.',
#             'price': 5000,
#             'customizations': ['White', 'Gray']
#         }
#     }

#     user_id = request.session.get('user_id')
#     if not user_id:
#         return redirect('login')

#     try:
#         current_user = mainuser.objects.get(user_id=user_id)
#         if Device.objects.filter(user=current_user).exists():
#             return redirect('add_device')  # Redirect if user already has a device
#     except mainuser.DoesNotExist:
#         return redirect('login')

#     device = device_data.get(device_name)
#     if not device:
#         return redirect('add_device')  # Redirect if device not found

#     if request.method == 'POST':
#         customization = request.POST.get('customization')
#         address = request.POST.get('address')

#         if not address:
#             return render(request, 'device_details.html', {
#                 'device': device,
#                 'error_message': 'Please provide a delivery address.'
#             })

#         # Add device to user's account
#         new_device = Device(
#             name=device['name'],
#             type=device['type'],
#             user=current_user
#         )
#         new_device.save()
#         request.session['device_id'] = new_device.device_id
#         # Here you could save customization and address to an Order model if needed
#         return redirect('dashboard')

#     return render(request, 'device_details.html', {'device': device})
# def add_device(request):
#     error_message = None
#     warning_message = None

#     # Get user_id from session
#     user_id = request.session.get('user_id')
#     if not user_id:
#         # Redirect to login if no user_id in session (assuming you have a login view)
#         return redirect('login')  # Replace 'login' with your login URL name

#     # Check if the user already has a device
#     try:
#         current_user = mainuser.objects.get(user_id=user_id)
#         if Device.objects.filter(user=current_user).exists():
#             warning_message = "You can only add one device. Please manage your existing device from the dashboard."
#             return render(request, 'add_device.html', {'warning_message': warning_message})
#     except mainuser.DoesNotExist:
#         # If user_id in session is invalid, redirect to login
#         return redirect('login')

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         device_type = request.POST.get('type')

#         # Check if device name already exists (across all users)
#         if Device.objects.filter(name=name).exists():
#             error_message = "Device name must be unique. This name is already taken."
#         else:
#             # Create and save the device with the current user from session
#             new_device = Device(name=name, type=device_type, user=current_user)
#             new_device.save()
#             request.session['device_id'] = new_device.device_id
#             return redirect('dashboard')  # Redirect to dashboard after success

#     return render(request, 'add_device.html', {'error_message': error_message})
# def add_device(request):
#     error_message = None

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         device_type = request.POST.get('type')

#         # Check if device name already exists
#         if Device.objects.filter(name=name).exists():
#             error_message = "Device name must be unique. This name is already taken."
#         else:
#             # Create and save the device
#             # Device.objects.create(name=name, type=device_type)
#             new_device = Device(name=name, type=device_type)
#             new_device.save()
#             request.session['device_id'] = new_device.device_id
#             return redirect('dashboard')  # Redirect to the homepage or another page after adding the device

#     return render(request, 'add_device.html', {'error_message': error_message})



from django.shortcuts import render, redirect
from .models import Device, Contact

from django.shortcuts import render, redirect
from .models import Device, mainuser, Contact

def add_contact(request):
    error_message = None
    success_message = None
    device = None

    # Get user_id from session
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if no user_id in session

    try:
        current_user = mainuser.objects.get(user_id=user_id)
    except mainuser.DoesNotExist:
        return redirect('login')

    # Check if a device is already selected in the session
    device_id = request.session.get('device_id')

    if request.method == 'POST':
        if 'device_name' in request.POST:
            # Step 1: User submits device name
            device_name = request.POST.get('device_name')
            try:
                device = Device.objects.get(name=device_name, user=current_user)
                request.session['device_id'] = device.device_id  # Store device_id in session
                return render(request, 'add_contact.html', {'device': device})
            except Device.DoesNotExist:
                error_message = "Device not found or does not belong to you."
                return render(request, 'add_contact.html', {'error_message': error_message})

        elif 'email' in request.POST and device_id:
            # Step 2: User submits contact details
            device = Device.objects.get(device_id=device_id)
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            # Validate unique email and phone for this device
            if Contact.objects.filter(email=email, device=device).exists():
                error_message = "This email is already associated with a contact for this device."
            elif Contact.objects.filter(phone=phone, device=device).exists():
                error_message = "This phone number is already associated with a contact for this device."
            else:
                # Create and save the contact
                Contact.objects.create(device=device, email=email, phone=phone)
                success_message = "Contact added successfully!"
                return redirect('dashboard')  # Redirect to dashboard after success

    # If no device_id in session or no POST request, show device name input form
    if device_id:
        try:
            device = Device.objects.get(device_id=device_id)
        except Device.DoesNotExist:
            del request.session['device_id']  # Clear invalid device_id
            device = None

    return render(request, 'add_contact.html', {
        'device': device,
        'error_message': error_message,
        'success_message': success_message
    })
# def add_contact(request):
#     error_message = None
#     success_message = None

#     # Ensure the device_id is in the session
#     user_id=request.session.get('user_id')
#     current_user = mainuser.objects.get(user_id=user_id)
#     existing_device = Device.objects.filter(user=current_user).first()  # Get the first (and only) device
#     device_id = request.session.get('device_id')
#     if not user_id:
#         return redirect('login')  # Redirect to index if no device is selected
#     if not device_id:
#         return redirect('dashboard')  # 

#     # Get the device associated with the device_id
#     device = Device.objects.get(device_id=device_id)

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')

#         # Validate unique email for contacts associated with the device
#         if Contact.objects.filter(email=email, device=device).exists():
#             error_message = "This email is already associated with a contact for this device."
#         elif Contact.objects.filter(phone=phone, device=device).exists():
#             error_message = "This phone number is already associated with a contact for this device."
#         else:
#             # Create and save the contact
#             Contact.objects.create(device=device, email=email, phone=phone)
#             success_message = "Contact added successfully!"
#             return redirect('dashboard')  # Redirect to the index page after adding the contact

#     return render(request, 'add_contact.html', {
#         'device': device,
#         'error_message': error_message,
#         'success_message': success_message
#     })



from django.shortcuts import render, redirect, get_object_or_404
from .models import Device, Contact

def manage_contacts(request):
    error_message = None
    device = None
    contacts = []

    if request.method == 'POST':
        device_name = request.POST.get('device_name')
        user_id=request.session.get('user_id')
        # Get the device associated with the entered name
        device = Device.objects.filter(name=device_name, user=user_id).first()

        if not device:
            error_message = "No device found with that name."
        else:
            contacts = Contact.objects.filter(device=device)

    # Handle delete action
    if 'delete_contact_id' in request.POST:
        contact_id = request.POST.get('delete_contact_id')
        contact = get_object_or_404(Contact, id=contact_id)
        contact.delete()
        return redirect('manage_contacts')  # Redirect to refresh the contact list

    # Handle edit action
    if 'edit_contact_id' in request.POST:
        contact_id = request.POST.get('edit_contact_id')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        contact = get_object_or_404(Contact, id=contact_id)
        contact.email = email
        contact.phone = phone
        contact.save()
        return redirect('manage_contacts')  # Redirect to refresh the contact list

    return render(request, 'manage_contacts.html', {
        'error_message': error_message,
        'device': device,
        'contacts': contacts,
    })



from django.http import JsonResponse
from .models import Device, Contact

# def get_contact_details(request, device_id):
#     if request.method == 'GET':
#         device = Device.objects.filter(device_id=device_id).first()
#         if device:
#             contacts = Contact.objects.filter(device=device)
#             contact_list = [{'email': contact.email, 'phone': contact.phone} for contact in contacts]
#             return JsonResponse(contact_list, safe=False)
#         return JsonResponse({'error': 'Device not found'}, status=404)


#****************
# from django.http import JsonResponse
# from .models import Contact

# def get_contact_details(request, device_id):
#     if request.method == 'GET':
#         try:
#             contacts = Contact.objects.filter(device_id=device_id).values()
#             return JsonResponse(list(contacts), safe=False)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)

#****************







# from django.http import JsonResponse
# from .models import Contact

# def get_contact_details(request, device_id):
#     if request.method == 'GET':
#         try:
#             # Fetch only the email field for contacts associated with the specific device
#             contacts = Contact.objects.filter(device_id=device_id).values('email')  # Include only 'email'
#             return JsonResponse(list(contacts), safe=False)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)



# from django.http import JsonResponse
# from .models import Contact
# from django.core.mail import send_mail
# from django.conf import settings

# def get_contact_details(request, device_id):
#     if request.method == 'GET':
#         try:
#             # Fetch only the email field for contacts associated with the specific device
#             contacts = Contact.objects.filter(device_id=device_id).values('email')
#             phone=Contact.objects.filter(device_id=device_id).values('phone')
#             emails = [contact['email'] for contact in contacts]
#             numbers=[co['phone'] for co in contacts]
#             # Send email to each contact
#             subject = "SMART-RING"
#             message = "This is a test email message."  # Customize your message

#             for email in emails:
#                 send_email(email, subject, message)
#                 print("email sended to-"+email)
                
                
#             for num in numbers:
#                 send_sms(num)
#                 print("sms sended to-"+num)

#             return JsonResponse(emails, safe=False)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)

# def send_email(to_email, subject, message):
#     try:
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,  # Sender's email
#             [to_email],  # Recipient's email
#             fail_silently=False,
#         )
#         return True
#     except Exception as e:
#         print(f"Error sending email: {e}")
#         return False

# # from django.http import JsonResponse

# # def get_contact_details(request, device_id):
# #     # Logic to retrieve contact details based on device_id
# #     contacts = Contact.objects.filter(device__id=device_id).first()  # Adjust to your needs
# #     return JsonResponse(list(contacts), safe=False)



# from twilio.rest import Client

# # Function to send SMS
# def send_sms(receiver_phone_number) :
    
#     # Twilio credentials
#     account_sid = ''       # Replace with your Account SID
#     auth_token = ''         # Replace with your Auth Token
#     twilio_phone_number = '+13218004216'    # Replace with your Twilio phone number
#     # receiver_phone_number = '+919573171351' # Replace with the recipient's phone number
#     receiver_phone_number = '+91'+receiver_phone_number
#     print("receiver_phone_number"+receiver_phone_number)
#     # Initialize Twilio Client
#     client = Client(account_sid, auth_token)

#     message_body = "T emergency alert your friend need you help."
#     message = client.messages.create(
#         body=message_body,
#         from_=twilio_phone_number,
#         to=receiver_phone_number
#     )
#     print(f"Message sent with SID: {message.sid}")


# # Import necessary modules
# from django.http import JsonResponse
# from django.core.mail import send_mail
# from django.conf import settings
# from .models import Contact
# from twilio.rest import Client

# # Function to retrieve contact details and send email and SMS
# def get_contact_details(request, device_id):
#     if request.method == 'GET':
#         try:
#             # Fetch email and phone for contacts associated with the device
#             contacts = Contact.objects.filter(device_id=device_id).values('email', 'phone')
        
#             emails = [contact['email'] for contact in contacts]
#             numbers = [contact['phone'] for contact in contacts]
            
#             latitude = "18.643648"  # Replace with your desired latitude
#             longitude = "79.547525"  # Replace with your desired longitude

#             # Create a Google Maps link using the latitude and longitude
#             maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

#             # Send email to each contact
#             subject = "SMART-RING Alert"
#             message = f"This is an emergency alert. Your friend needs your help! Please see the location on the map: {maps_link}"

          
#             for email in emails:
#                 send_email(email, subject, message)
#                 print("Email sent to:", email)

#             # Send SMS to each phone number
#             for num in numbers:
#                 send_sms(num,message)
#                 print("SMS sent to:", num)
                
#             for num in numbers:
#                 make_phone_call(num)
#                 print("SMS sent to:", num)
                
            

#             return JsonResponse({"status": "success", "emails": emails, "phone_numbers": numbers}, safe=False)
        
#         except Exception as e:
#             print(f"Error: {e}")
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=400)


# # Helper function to send email
# def send_email(to_email, subject, message):
#     try:
#         send_mail(
#             subject,
#             message,
#             settings.EMAIL_HOST_USER,  # Ensure this is configured in settings.py
#             [to_email],
#             fail_silently=False,
#         )
#         print("Email sent successfully to:", to_email)
#         return True
#     except Exception as e:
#         print(f"Error sending email: {e}")
#         return False


# account_sid = ''       # Replace with your Account SID
# auth_token = ''         # Replace with your Auth Token
# twilio_phone_number = '+13218004216'
        
# # Function to send SMS using Twilio
# def send_sms(receiver_phone_number,message):
#     try:
        
#         # Ensure the receiver's phone number is in the correct format
#         receiver_phone_number = f'+91{receiver_phone_number}'
        
#         # Initialize Twilio Client
#         client = Client(account_sid, auth_token)
#         message_body = message
#         # message_body = "Emergency alert: Your friend needs your help."
#         message = client.messages.create(
#             body=message_body,
#             from_=twilio_phone_number,
#             to=receiver_phone_number
#         )
#         print(f"Message sent with SID: {message.sid}")
#     except Exception as e:
#         print(f"Error sending SMS: {e}")



# from twilio.rest import Client
# from django.conf import settings
# # receiver_phone_number1="+919573171351"
# def make_phone_call(receiver_phone_number1):
#     try:
#         # Initialize Twilio Client
#         client = Client(account_sid,auth_token)
#         receiver_phone_number = f'+91{receiver_phone_number1}'
#         # Initiate the phone call
#         call = client.calls.create(
#             to=receiver_phone_number,         # Receiver's phone number
#             from_=twilio_phone_number, # Your Twilio number
#             url="http://demo.twilio.com/docs/voice.xml"  # URL to TwiML (XML instructions for the call)
            
#         )
        
#         print(f"Call initiated with SID: {call.sid}")
#         return call.sid  # Optionally return the call SID for reference
#     except Exception as e:
#         print(f"Error making call: {e}")
#         return None
import pyaudio
import wave
import os
from django.http import JsonResponse
from django.core.mail import send_mail
from twilio.rest import Client
from .models import Contact, History, Device, mainuser



from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from twilio.rest import Client

# Twilio Credentials
# account_sid = ''  # Replace with your Account SID
# auth_token = ''  # Replace with your Auth Token


account_sid = ''  # Replace with your Account SID
auth_token = ''  # Replace with your Auth Token
twilio_phone_number = '+1 857 598 7634'
# Function to Retrieve Contact Details and Send Alerts
def get_contact_details(request, device_id):
    if request.method == 'GET':
        try:
            # device_detail2(request,device_id)
            contacts = Contact.objects.filter(device_id=device_id).values('email', 'phone')
            emails = [contact['email'] for contact in contacts]
            numbers = [contact['phone'] for contact in contacts]
            
            
            latest_audio = History.objects.latest('recorded_at')
            audio_file_path = latest_audio.audio_file.path  # Absolute path on server
            audio_file_name = os.path.basename(audio_file_path)  # e.g., "recording_164xxxx.webm"


            latitude = "18.643648"
            longitude = "79.547525"
            maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

            subject = "SMART-RING Alert"
            message = f"This is an emergency alert. Your friend needs your help! See location: {maps_link}"

            # Send Email Alerts
            for email in emails:
                send_email(email, subject, message)

            # Send SMS Alerts
            for num in numbers:
                send_sms(num, message)

            # Make Phone Calls
            for num in numbers:
                make_phone_call(num)
            
            # testing()
            # for num in numbers:
                # sw(num,message)
                

            return JsonResponse({"status": "success"}, safe=False)

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"status": "fail", "error": str(e)}, status=400)

    return JsonResponse({"status": "fail", "error": "Invalid request method"}, status=400)


# def gcd(device_id):
#     if device_id:
#         try:
#             contacts = Contact.objects.filter(device_id=device_id).values('email', 'phone')
#             emails = [contact['email'] for contact in contacts]
#             numbers = [contact['phone'] for contact in contacts]

#             latitude = "18.643648"
#             longitude = "79.547525"
#             maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

#             subject = "SMART-RING Alert"
#             message = f"This is an emergency alert. Your friend needs your help! See location: {maps_link}"

#             # Send Email Alerts
#             for email in emails:
#                 send_email(email, subject, message)

#             # Send SMS Alerts
#             for num in numbers:
#                 send_sms(num, message)

#             # Make Phone Calls
#             for num in numbers:
#                 make_phone_call(num)
#             print("1111111111111111111111111111111")
#             testing()
#             print("222222222222222222")

#             return JsonResponse({"status": "success"}, safe=False)

#         except Exception as e:
#             print(f"Error: {e}")
#             return JsonResponse({"status": "fail", "error": str(e)}, status=400)

#     return JsonResponse({"status": "fail", "error": "Invalid request method"}, status=400)


# try:
#             # Get the latest audio file from History
#             latest_audio = History.objects.latest('recorded_at')
#             audio_file_path = latest_audio.audio_file.path  # Absolute path on server
#             audio_file_name = os.path.basename(audio_file_path)  # e.g., "recording_164xxxx.webm"

#             # Create the email
#             subject = "Your Recorded Audio File"
#             body = "Please find the attached audio file recorded on your device."
#             email = EmailMessage(
#                 subject=subject,
#                 body=body,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=[to_email],
#             )

#             # Attach the audio file
#             with open(audio_file_path, 'rb') as f:
#                 email.attach(audio_file_name, f.read(), 'audio/webm')

#             # Send the email
#             email.send(fail_silently=False)

#             return JsonResponse({
#                 'message': 'Audio sent successfully via email',
#                 'audio_path': audio_file_path,
#                 'timestamp': latest_audio.recorded_at.isoformat()
#             })

#         except History.DoesNotExist:
#             return JsonResponse({'error': 'No audio files found in History'}, status=404)
#         except Exception as e:
#             return JsonResponse({'error': f'Failed to send email: {str(e)}'}, status=500)
# Helper Function to Send Email
def send_email(to_email, subject, message):
    try:
        
            # Get the latest audio file from History
        latest_audio = History.objects.latest('recorded_at')
        audio_file_path = latest_audio.audio_file.path  # Absolute path on server
        audio_file_name = os.path.basename(audio_file_path)  # e.g., "recording_164xxxx.webm"

            # Create the email
    
        email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[to_email],
            )

            # Attach the audio file
        with open(audio_file_path, 'rb') as f:
            email.attach(audio_file_name, f.read(), 'audio/webm')

            # Send the email
        email.send(fail_silently=False)
        # send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)
        print(f"Email sent to: {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to Send SMS Using Twilio
def send_sms(receiver_phone_number, message):
    try:
        client = Client(account_sid, auth_token)
        receiver_phone_number = f'+91{receiver_phone_number}'
        message = client.messages.create(body=message, from_=twilio_phone_number, to=receiver_phone_number)
        print(f"SMS sent to: {receiver_phone_number} (SID: {message.sid})")
    except Exception as e:
        print(f"Error sending SMS: {e}")


from twilio.rest import Client

def sw(num, msg):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    
    # Convert num to string and construct the WhatsApp number
    whatsapp_number = 'whatsapp:+91' + str(num)  # Correct concatenation
    
    # Send WhatsApp message
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio Sandbox/Business Number
        body=msg,                       # Custom message text
        to=whatsapp_number              # Constructed recipient WhatsApp number
    )
    
    return message.sid  # Optional: Return the message SID for confirmation
    
# Function to Make Phone Calls Using Twilio
def make_phone_call(receiver_phone_number):
    try:
        client = Client(account_sid, auth_token)
        receiver_phone_number = f'+91{receiver_phone_number}'
        call = client.calls.create(to=receiver_phone_number, from_=twilio_phone_number,
                                   url="http://demo.twilio.com/docs/voice.xml")
        print(f"Call initiated to: {receiver_phone_number} (SID: {call.sid})")
    except Exception as e:
        print(f"Error making call: {e}")
        

import requests
from twilio.rest import Client

# def upload_file(file_path):
#     """Uploads the file to file.io and returns a public URL."""
#     url = "https://file.io/"
#     with open(file_path, "rb") as file:
#         response = requests.post(url, files={"file": file})
#     return response.json().get("link")

# def send_whatsapp_message(audio_url):
#     """Sends a WhatsApp message with the uploaded audio file."""
    
#     
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#         from_="whatsapp:",
#         to="whatsapp:+919390370155",
#         body="🔊 Listen to this emergency audio message:",
#         media_url=[audio_url]  # Use the uploaded file's URL
#     )
    
#     print(f"WhatsApp Message SID: {message.sid}")





def testing():
    
    latitude = "18.643648"
    longitude = "79.547525"
    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

    message = f"This is an emergency alert. Your friend needs your help! See location: {maps_link}"
    # num="+919441448075"
    # make_phone_call(num)

    account_sid = '...'
    auth_token = '...'
    client = Client(account_sid, auth_token)
    # Send WhatsApp message
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio Sandbox/Business Number
        body=message,  # Custom message text
        to='whatsapp:+919573171351'  # Replace with the recipient's WhatsApp number
    )
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     from_='whatsapp:+14155238886',  # Twilio Sandbox/Business Number
    #     body=message,  # Custom message text
    #     to='whatsapp:+919390370155'  # Replace with the recipient's WhatsApp number
    # )

    # print(f"WhatsApp Message SID: {message.sid}")
    # make_phone_call(num)
    # send_sms(num, message)
    
# # views.py
# from django.http import HttpResponse
# from twilio.twiml.voice_response import VoiceResponse

# def call_response(request):
#     response = VoiceResponse()

#     # Gather a single digit from the user
#     gather = response.gather(num_digits=1, action="/handle-keypress/", method="POST")
#     gather.say("Hello! This is a critical alert from your Friend. If you need further assistance, please press 1.")
    
#     # If no input is received
#     response.say("We didn't receive any input. Goodbye!")

#     return HttpResponse(str(response), content_type='text/xml')



# # views.py
# def handle_keypress(request):
#     # Retrieve the digit pressed by the user
#     digit_pressed = request.POST.get('Digits', None)
#     response = VoiceResponse()
    
#     if digit_pressed == '1':
#         response.say("Thank you for your response. Help is on the way!")
#     else:
#         response.say("You pressed an invalid option. anyway, Help is on the way!")
    
#     return HttpResponse(str(response), content_type='text/xml')


# from django.http import HttpResponse
# from twilio.twiml.voice_response import VoiceResponse

# def call_response(request):
#     response = VoiceResponse()
    
#     # Step 1: Customize the voice message
#     custom_message = "Hello! This is an alert from your system. If you need assistance, please press 1 now."
    
#     # Step 2: Configure the Gather action to capture keypresses
#     gather = response.gather(num_digits=1, action="/handle-keypress/", method="POST")
#     gather.say(custom_message)  # Set your custom message here

#     # Step 3: Provide an alternate message if no input is received
#     response.say("We didn't receive any input. Goodbye!")  

#     # Return the TwiML response
#     return HttpResponse(response, content_type='text/xml')


# def handle_keypress(request):
#     response = VoiceResponse()
    
#     # Check which key was pressed
#     digit_pressed = request.POST.get('Digits')
    
#     if digit_pressed == '1':
#         response.say("Thank you for acknowledging the alert. Help is on the way.")
#     else:
#         response.say("Invalid selection. Please listen carefully to the message.")

#     return HttpResponse(response, content_type='text/xml')


# to_mail="akulashivaakulashiva@gmail.com"
# # Define the latitude and longitude for the map location
# latitude = "18.530304"  # Replace with your desired latitude
# longitude = "79.627217"  # Replace with your desired longitude

#             # Create a Google Maps link using the latitude and longitude
# maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

#             # Send email to each contact
# subject1 = "SMART-RING Alert"
# message = f"This is an emergency alert. Your friend needs your help! Please see the location on the map: {maps_link}"

# Helper function to send email
# def send_email_static( subject1, message):
#     try:
#         send_mail(
#             subject1,
#             message,
#             settings.EMAIL_HOST_USER,  # Ensure this is configured in settings.py
#             [to_mail],
#             fail_silently=False,
#         )
#         print("Email sent successfully to:", to_mail)
#         return True
#     except Exception as e:
#         print(f"Error sending email: {e}")
#         return False


# def whtas():
#     print("entered..")
#     sid="AC87c2a7f0187439b6c1e08ee06c74025f"
#     auth="a771922a4ceff468d85871853f052242"
#     client=Client(sid,auth)
    
#     message=client.messages.create(
#         to='whatsapp:+919390370155',
#         from_='whatsapp:+13218004216',
#         body='alert from your friend'
#     )
#     print("exited....")

# New logout view
def logout(request):
    request.session.flush()  # Clear all session data
    return redirect('homepage2')  # Redirect to login page after logout



# def send_audio_via_whatsapp(num, msg):
#     # Twilio credentials
#     account_sid = 'AC87c2a7f0187439b6c1e08ee06c74025f'
#     auth_token = 'a771922a4ceff468d85871853f052242'
#     client = Client(account_sid, auth_token)

#     try:
#         # Get the latest audio file from History
#         latest_audio = History.objects.latest('recorded_at')
        
#         # Manually construct the audio URL (replace BASE_URL with your public URL)
#         BASE_URL = "http://127.0.0.1:8000"  # Replace with ngrok URL or deployed server URL
#         audio_url = f"{BASE_URL}{latest_audio.audio_file.url}"  # e.g., http://127.0.0.1:8000/media/...

#         # Construct WhatsApp number
#         whatsapp_number = 'whatsapp:+91' + str(num)

#         # Send WhatsApp message with audio
#         message = client.messages.create(
#             from_='whatsapp:+14155238886',  # Twilio Sandbox/Business Number
#             body=msg,
#             media_url=[audio_url],
#             to=whatsapp_number
#         )

#         print(f"Audio sent successfully! Message SID: {message.sid}, Audio URL: {audio_url}")
#         return message.sid

#     except History.DoesNotExist:
#         print("Error: No audio files found in History")
#         return None
#     except Exception as e:
#         print(f"Error sending audio: {str(e)}")
#         return None