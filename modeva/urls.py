from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views  # ✅ Import your app views

urlpatterns = [
    # 🔐 Authentication
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),

    # 🧭 Admin Panel
    path('admin/', admin.site.urls),

    # 🏠 Include all URLs from your main app
    path('', include('main.urls')),
]

# 🖼️ Serve media files (images, uploads, etc.) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
