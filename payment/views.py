from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from sslcommerz_lib import SSLCOMMERZ
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User
from account.models import Account
from transaction.models import Transaction
import uuid
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)
from rest_framework import viewsets

class PaymentViewSet(viewsets.ViewSet):
    # queryset = Payment.objects.all()
    # serializer_class = PaymentSerializer

    # @action(detail=False, methods=['post'])
    # def create_payment(self, request):
    def create(self, request):
        # print("rabiul")
        logger.info(f"Received data: {request.data}")
        store_id = 'phitr67adeab8132c8'
        store_pass = 'phitr67adeab8132c8@ssl'

        # sslcz_settings = {
        #     'store_id': 'phitr67adeab8132c8',
        #     'store_pass': 'phitr67adeab8132c8@ssl',
        #     'issandbox': True
        # }
        # sslcz = SSLCOMMERZ(sslcz_settings)

        trx_id = str(uuid.uuid4())[:10].replace('-', '').upper()

        user_id = request.data.get('user')
        amount = request.data.get('amount') 
        # print(amount)
        
        reference = request.data.get('reference')
        accountNo = request.data.get('accountNo')
        typys = request.data.get('typys')
        source_people = request.data.get('source_people')
        media = request.data.get('media' )
        purpose = request.data.get('purpose')
        comment = request.data.get('comment')
        approved = request.data.get('approved')
        
         
        settings = {'store_id': store_id,
                    'store_pass': store_pass, 'issandbox': True}
        
        
        sslcommez = SSLCOMMERZ(settings)
        print(sslcommez)
        post_body = {}
        post_body['total_amount'] = amount
        post_body['currency'] = "BDT"
        post_body['tran_id'] = trx_id
        # post_body['success_url'] = f'https://github.com/rabi993'
        post_body['success_url'] = request.build_absolute_uri(f'success/?trx_id={trx_id}&user_id={user_id}&reference={reference}&amount={amount}&accountNo={accountNo}&typys={typys}&source_people={source_people}&media={media}&purpose={purpose}&comment={comment}&approved={approved}')
        # post_body['success_url'] = f'http://127.0.0.1:5501/MyDonateHistory.html'
        post_body['fail_url'] = request.build_absolute_uri(f'fail/')

        post_body['cancel_url'] = request.build_absolute_uri(f'cancle/')
        post_body['emi_option'] = 0
        post_body['cus_email'] = "test@test.com"
        post_body['cus_phone'] = "01700000000"
        post_body['cus_add1'] = 'Dhaka' 
        post_body['cus_city'] = 'Uttara'
        post_body['cus_country'] = 'Bangladesh'
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = "Test"
        post_body['product_category'] = "Test Category"
        post_body['product_profile'] = "general"


        response = sslcommez.createSession(post_body)
        print(response)

        return Response(response['GatewayPageURL'])
    @csrf_exempt
    @action(detail=False, methods=['post'])
    def success(self, request):
        print('rabiul')
        try:
            account_instance = Account.objects.get(id=1)
            user_id = request.query_params.get('user_id')  
            trx_id = request.query_params.get('trx_id')
            reference = request.query_params.get('reference')
            amount = request.query_params.get('amount')
            accountNo = request.query_params.get('accountNo')
            typys = request.query_params.get('typys')
            source_people = request.query_params.get('source_people')
            media = request.query_params.get('media')
            purpose = request.query_params.get('purpose')
            comment = request.query_params.get('comment')
            approved = False 

            print(f"Received transaction details: {request.query_params}")
        
            if not user_id:
                return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

            
            transaction = Transaction.objects.create(
                user=user, 
                trx_id=trx_id, 
                reference=reference,
                amount=amount, 
                accountNo=accountNo,
                typys=typys, 
                source_people=source_people,
                media=media,
                purpose=purpose,
                comment=comment,
                approved=approved,
                account=account_instance
            )

            print(f"Transaction created successfully: {transaction}")

            return redirect('https://rabi993.github.io/umsa_frontend/MyDonateHistory.html')

        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({"error": "Internal Server Error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # print('rabi')
        # logger.info("Payment success callback triggered")
        # logger.info(f"Received data: {request.data}")

        # # Extract required fields
        # trx_id = trx_id  # Ensure correct key name
        # user_id = request.data.get('value_a')  # Ensure user ID is passed in payment request

        # if not trx_id or not user_id:
        #     logger.error("Missing transaction ID or user ID")
        #     return Response({"error": "Missing transaction ID or user ID"}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     user = User.objects.get(id=user_id)
        #     logger.info(f"User found: {user}")

        #     # Create a transaction record
        #     transaction = Transaction.objects.create(
        #         user=user,
        #         trx_id=trx_id,
        #         reference=request.data.get('reference', 'N/A'),
        #         amount=request.data.get('amount', 0),
        #         accountNo=request.data.get('accountNo', 'N/A'),
        #         typys=request.data.get('typys', 'credit'),
        #         source_people=request.data.get('source_people', 'N/A'),
        #         media=request.data.get('media', 'Bank'),
        #         purpose=request.data.get('purpose', 'N/A'),
        #         comment=request.data.get('comment', 'N/A'),
        #         approved=True  # Mark transaction as approved
        #     )

        #     logger.info(f"Transaction created successfully: {transaction}")

        #     return redirect(settings.SUCCESS_URL)

        # except User.DoesNotExist:
        #     logger.error("User not found")
        #     return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # except Exception as e:
        #     logger.error(f"Exception occurred: {str(e)}")
        #     return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # @csrf_exempt
    # @action(detail=False, methods=['post'])
    # def success(self, request):
    #     print("success")
    #     trx_id = request.data.get('trx_id')
    #     user_id = request.data.get('user_id')

    #     try:
    #         user = User.objects.get(id=user_id)
    #         print(user)
    #         print(request.data.get('reference'))

    #         transaction = Transaction.objects.create(
    #             user=user,
    #             trx_id=trx_id,
    #             reference=request.data.get('reference'),
    #             amount=request.data.get('amount'),
    #             accountNo=request.data.get('accountNo'),
    #             typys=request.data.get('typys', 'credit'),
    #             source_people=request.data.get('source_people'),
    #             media=request.data.get('media', 'Bank'),
    #             purpose=request.data.get('purpose'),
    #             comment=request.data.get('comment'),
    #             approved=False
    #         )

    #         return redirect(settings.SUCCESS_URL)
    #     except User.DoesNotExist:
    #         return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def fail(self, request):
        return redirect('https://rabi993.github.io/umsa_frontend/transaction3.html')

    @action(detail=False, methods=['post'])
    def cancel(self, request):
        return redirect('https://rabi993.github.io/umsa_frontend/transaction3.html')