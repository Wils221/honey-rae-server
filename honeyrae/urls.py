from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import register_user, login_user
from rest_framework import routers
from repairsapi.views import CustomerView
from repairsapi.views import EmployeeView
from repairsapi.views import ServiceTicketView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')

router_1 = routers.DefaultRouter(trailing_slash=False)
router_1.register(r'employees', EmployeeView, 'employee')

router_2 = routers.DefaultRouter(trailing_slash=False)
router_2.register(r'service_tickets', ServiceTicketView, 'serviceTicket')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(router_1.urls)),
    path('', include(router_2.urls)),
]