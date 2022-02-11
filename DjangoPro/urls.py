"""DjangoPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.http import HttpRequest
from django.urls import path
from ninja import NinjaAPI  # 장고닌자 import!
from typing import Dict

api = NinjaAPI()  # 장고닌자 api를 바로 인스턴스화


@api.get("/add")  # 함수를 데코레이터로 감싸서 사용 / # view function을 데코레이터로 감싸고 /add 로 url을 넘겨준다
def add(request: HttpRequest, a: int, b: int) -> Dict[str, int]:
    return {"result": a + b}  # 기존 장고의 분리된 방식보다 가독성 up!!


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]