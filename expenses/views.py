from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from .models import Expense
from .serializers import ExpenseSerializer, RegisterUserSerializer
from rest_framework.decorators import action
from django.db.models import Sum
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = []

    
class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        query_set = Expense.objects.filter(user=user)

        start = self.request.query_params.get('start_date')
        end = self.request.query_params.get('end_date')
        if start and end:
            query_set = query_set.filter(date__range=[start, end])
        return query_set
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def analytics(self, request):
        user = request.user
        start = request.query_params.get('start_date')
        end = request.query_params.get('end_date')
        expenses = Expense.objects.filter(user=user)

        if start and end:
            expenses = expenses.filter(date__range=[start, end])
        
        total = expenses.aggregate(total=Sum('amount'))['total'] or 0
        by_category = expenses.values('category').annotate(total=Sum('amount'))

        trend = expenses.annotate(period=TruncMonth('date')).values('period').annotate(total=Sum('amount'))

        return Response({
            'total_expenses' : total,
            'category_breakdown' : list(by_category),
            'monthly_trend' : list(trend),
        })