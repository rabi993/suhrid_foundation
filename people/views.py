from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect


class PeopleViewset(viewsets.ModelViewSet):
    queryset = models.People.objects.all()
    serializer_class = serializers.PeopleSerializer

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

 
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            
            # confirm_link = f"https://club-1-6len.onrender.com/people/active/{uid}/{token}"
            confirm_link = f"https://club-wine.vercel.app/people/active/{uid}/{token}"
            
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('https://rabi993.github.io/umsa_frontend/login.html')
    else:
        return redirect('https://rabi993.github.io/umsa_frontend/registration.html')
    

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
         # return redirect('login')
        return Response({'success' : "logout successful"})
        


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data

        old_password = data.get('old_password')
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')

        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
        
        if new_password != confirm_new_password:
            return Response({"error": "New passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()

        try:
            send_mail(
                subject="Password Changed Successfully",
                message=(
                    f"Hi {user.username},\n\n"
                    "Your password has been changed successfully. If you did not make this change, "
                    "please contact our support team immediately.\n\n"
                    "Best regards,\nFlower's World"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
        except Exception as e:
            return Response(
                {"error": f"Password changed, but failed to send email: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Return success response
        return Response({"success": "Password changed successfully and email sent."}, status=status.HTTP_200_OK)

# from rest_framework.permissions import IsAdminUser
# from django.contrib.auth.models import User

# class ToggleUserStatusApiView(APIView):
#     permission_classes = [IsAdminUser]

#     def post(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)
#             user.is_active = not user.is_active
#             user.save()

#             status = "activated" if user.is_active else "deactivated"
#             return Response({"message": f"User successfully {status}."}, status=200)
#         except User.DoesNotExist:
#             return Response({"error": "User not found."}, status=404)
 
# from rest_framework.permissions import IsAdminUser
# from django.contrib.auth.models import User
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string

# class ToggleUserStatusApiView(APIView):
#     permission_classes = [IsAdminUser]

#     def post(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)
#             previous_status = user.is_active
#             user.is_active = not user.is_active
#             user.save()

#             # Send email notification if the status changes
#             if previous_status != user.is_active:
#                 email_subject = f"Your Account Status: {'Activated' if user.is_active else 'Deactivated'}"
#                 email_body = render_to_string('admin_email.html', {
#                     'user': user,
#                     'is_active': user.is_active,
#                 })

#                 email = EmailMultiAlternatives(
#                     email_subject,
#                     '',
#                     to=[user.email]
#                 )
#                 email.attach_alternative(email_body, "text/html")
#                 email.send()

#             status = "activated" if user.is_active else "deactivated"
#             return Response({"message": f"User successfully {status}."}, status=200)

#         except User.DoesNotExist:
#             return Response({"error": "User not found."}, status=404)


# from django.core.mail import send_mail
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt
# def send_email(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             recipient_email = data.get('email')
#             user_status = data.get('status')

#             subject = 'Account Status Update'
#             message = f'Your account status has been updated to: {user_status}'
#             sender_email = 'your-email@example.com'

#             send_mail(subject, message, sender_email, [recipient_email])

#             return JsonResponse({'message': 'Email sent successfully.'}, status=200)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request method.'}, status=400)