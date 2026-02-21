from django.contrib.auth.models import User 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [] 

# # views.py
# from django.core.mail import send_mail
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
# import json

# @csrf_exempt
# def update_user_status(request, user_id):
#     if request.method == 'PATCH':
#         try:
#             user = get_object_or_404(User, id=user_id)
#             data = json.loads(request.body)
#             new_status = data.get('is_active', user.is_active)

#             if new_status != user.is_active:
#                 user.is_active = new_status
#                 user.save()

#                 # Email content
#                 subject = "Account Status Update"
#                 message = f"Dear {user.username},\n\nYour account has been {'activated' if new_status else 'deactivated'}.\n\nThank you,\nUMSA Admin Team."
#                 recipient_list = [user.email]

#                 # Send email
#                 try:
#                     send_mail(
#                         subject=subject,
#                         message=message,
#                         from_email="rabiulislam.170113@s.pust.ac.bd", 
#                         recipient_list=recipient_list,
#                         fail_silently=False,
#                     )
#                 except Exception as e:
#                     return JsonResponse({"error": f"Failed to send email: {str(e)}"}, status=500)

#                 return JsonResponse({
#                     "message": f"User status updated to {'Active' if new_status else 'Inactive'} and email sent to the user."
#                 })

#             return JsonResponse({"message": "No status change detected."}, status=400)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     return JsonResponse({"error": "Invalid request method."}, status=405)

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


from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            recipient_email = data.get('email')
            user_status = data.get('status')

            subject = 'Account Status Update'
            message = f'Your account status has been updated to: {user_status}'
            sender_email = 'rabiulislam.170113@s.pust.ac.bd'

            send_mail(subject, message, sender_email, [recipient_email])

            return JsonResponse({'message': 'Email sent successfully.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)