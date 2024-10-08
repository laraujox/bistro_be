"""
URL configuration for bistro_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from order.views import CreateOrderView, upgrade_order_status_view, downgrade_order_status_view

urlpatterns = [
    path("", CreateOrderView.as_view(), name="create_order"),
    path('<int:order_id>/upgrade', upgrade_order_status_view, name='upgrade_order_status'),
    path(
        '<int:order_id>/downgrade', downgrade_order_status_view, name='downgrade_order_status'
    ),
]
