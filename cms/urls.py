from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("form",views.form_view, name="form"),
    path("entry",views.entry, name="entry"),
    path("dashboard",views.dashboard, name="dashboard"),
    path("project/<int:item>",views.project, name="project"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("csvexport", views.csv_export, name="csv_export"),
    path("excelexport", views.excel_export, name="excel_export"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

