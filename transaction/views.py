from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializer import TransactionSerializer

class TransactionListCreateAPIView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    def patch(self, request, pk):  # Use 'pk' for consistency
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

        # Allow partial updates by setting 'partial=True'
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

        transaction.delete()
        return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.mail import send_mail
# from .models import Transaction
# from .serializer import TransactionSerializer

# class TransactionListCreateAPIView(APIView):
#     def get(self, request):
#         transactions = Transaction.objects.all()
#         serializer = TransactionSerializer(transactions, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TransactionSerializer(data=request.data)
#         if serializer.is_valid():
#             transaction = serializer.save()

#             # Send email for credit approval
#             if transaction.status == "approved":  # Assuming you have a `status` field in your model
#                 self.send_credit_approval_email(transaction)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def send_credit_approval_email(self, transaction):
#         """
#         Sends an email to the user regarding credit approval.
#         """
#         user_email = transaction.user.email  # Assuming `Transaction` has a foreign key to `User`
#         subject = "Credit Approval Notification"
#         message = (
#             f"Dear {transaction.user.username},\n\n"
#             f"We are pleased to inform you that your transaction (ID: {transaction.id}) has been approved.\n\n"
#             f"Transaction Details:\n"
#             f"Amount: {transaction.amount}\n"
#             f"Status: Approved\n\n"
#             f"Thank you for choosing our services.\n\n"
#             f"Best regards,\nYour Company Team"
#         )
#         try:
#             send_mail(
#                 subject=subject,
#                 message=message,
#                 from_email="rabiulislam.170113@s.pust.ac.bd",  # Replace with your email
#                 recipient_list=[user_email],
#                 fail_silently=False,
#             )
#         except Exception as e:
#             print(f"Failed to send email: {str(e)}")  # Log the error


# class TransactionDetailAPIView(APIView):
#     def get(self, request, pk):
#         try:
#             transaction = Transaction.objects.get(pk=pk)
#         except Transaction.DoesNotExist:
#             return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = TransactionSerializer(transaction)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         try:
#             transaction = Transaction.objects.get(pk=pk)
#         except Transaction.DoesNotExist:
#             return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = TransactionSerializer(transaction, data=request.data)
#         if serializer.is_valid():
#             updated_transaction = serializer.save()

#             # Send email for credit approval
#             if updated_transaction.status == "approved":  # Assuming `status` field
#                 self.send_credit_approval_email(updated_transaction)

#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         try:
#             transaction = Transaction.objects.get(pk=pk)
#         except Transaction.DoesNotExist:
#             return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = TransactionSerializer(transaction, data=request.data, partial=True)
#         if serializer.is_valid():
#             updated_transaction = serializer.save()

#             # Send email for credit approval
#             if updated_transaction.status == "approved":  # Assuming `status` field
#                 self.send_credit_approval_email(updated_transaction)

#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             transaction = Transaction.objects.get(pk=pk)
#         except Transaction.DoesNotExist:
#             return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

#         transaction.delete()
#         return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

#     def send_credit_approval_email(self, transaction):
#         """
#         Sends an email to the user regarding credit approval.
#         """
#         user_email = transaction.user.email  # Assuming `Transaction` has a foreign key to `User`
#         subject = "Credit Approval Notification"
#         message = (
#             f"Dear {transaction.user.username},\n\n"
#             f"We are pleased to inform you that your transaction (ID: {transaction.id}) has been approved.\n\n"
#             f"Transaction Details:\n"
#             f"Amount: {transaction.amount}\n"
#             f"Status: Approved\n\n"
#             f"Thank you for choosing our services.\n\n"
#             f"Best regards,\nYour Company Team"
#         )
#         try:
#             send_mail(
#                 subject=subject,
#                 message=message,
#                 from_email="rabiulislam.170113@s.pust.ac.bd",  # Replace with your email
#                 recipient_list=[user_email],
#                 fail_silently=False,
#             )
#         except Exception as e:
#             print(f"Failed to send email: {str(e)}")  # Log the error