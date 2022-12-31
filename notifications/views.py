from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status

from .schema import NotificationSchema
from .models import Notification
from .serializers import NotificationSerializer
from .forms import NotificationForm

# Create your views here.
class NotificationsView(APIView):
    """
    This view handles all the crud operations for notification messages
    """

    schema=NotificationSchema()

    # permissions
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """ Returns all notification messages """

    def get(self,request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    """ Creates a new notification """

    def post(self,request):
        form=NotificationForm(request.data)

        if form.is_valid():
            notification=form.save(commit=False)
            notification.save()
            
            serializer=NotificationSerializer(notification).data

            return Response(serializer,status=status.HTTP_201_CREATED)
            
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


    """ Updates existing notification, sets it as read/viewed"""

    def patch(self, request):
        notification=get_object_or_404(Notification, id=request.data.get("id"))

        if notification:
            notification.read=True
            notification.save()
            serializer=NotificationSerializer(notification).data

            return Response(serializer,status=status.HTTP_202_ACCEPTED)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)


    """ deletes a product from db """

    def delete(self, request):
        notification=get_object_or_404(Notification, id=request.data.get("id"))

        if notification:
            notification.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)