from .views import GeeksView
from django.urls import path
  
urlpatterns = [  
    path('', GeeksView.as_view())
    # path('api-auth/', include('rest_framework.urls'))
]  