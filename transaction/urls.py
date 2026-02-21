from django.urls import path
from .views import TransactionListCreateAPIView, TransactionDetailAPIView

urlpatterns = [
    path('', TransactionListCreateAPIView.as_view(), name='transaction-list-create'),
    path('<int:pk>/', TransactionDetailAPIView.as_view(), name='transaction-detail'),
    # path('<int:id>/approve/', update_transaction, name='transaction-approve'),
]