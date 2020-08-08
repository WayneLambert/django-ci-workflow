from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from aa_project.settings.base import DJANGO_ADMIN_LOGIN_PATH

urlpatterns = [
    path('', include('pages.urls')),
]

# Admin Site URLs
urlpatterns += [
    path(
        f'{DJANGO_ADMIN_LOGIN_PATH}/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset'
    ),
    path(
        f'{DJANGO_ADMIN_LOGIN_PATH}/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
    path(f'{DJANGO_ADMIN_LOGIN_PATH}/', admin.site.urls),
]


# Django Debug Toolbar Settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
