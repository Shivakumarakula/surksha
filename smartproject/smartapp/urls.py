
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('',views.openingpage,name='home'),
    path('homepage2',views.homepage2,name="homepage2"),
    path('login/',views.login,name="login"),
      path('signup/',views.signup,name="signup"),
        path('dashboard/',views.dashboard,name="dashboard"),
         path('forgotpass',views.forgotpass,name="forgotpass"),
         path('about/',views.about,name="about"),
         path('services',views.services,name="services"),


path('user_register',views.user_register,name="user_register"),

   path('activate/<uidb64>/<token>/', views.activate, name='activate'),
   
   path('login_operations/',views.login_operation, name='login_operation'),
    # path('logout/',views.user_logout, name="user_logout"),
    
path('password_reset/', views.password_reset_request, name='password_reset'),
  
     path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('reset/invalid/', views.password_reset_invalid, name='password_reset_invalid'),


path('dashboard/', views.dashboard, name='dashboard'),
path('device_detail2/<int:device_id>/', views.device_detail2, name='device_detail2'),

path('handle_voice_assistant/', views.handle_voice_assistant, name='handle_voice_assistant'),
    # path('activate_device/', views.activate_device, name='activate_device'),
    
    
    #   path('add-device/', views.add_device, name='add_device'),
      
        # path('add-contact/', views.add_contact, name='add_contact'),  # URL for adding contacts,
        
          path('add_device/', views.add_device, name='add_device'),
          # path('device_details/<str:device_name>/', views.device_details, name='device_details'),
          path('device_details/<str:device_name>/', views.device_details, name='device_details'),
    path('payment/verify/', views.payment_verify, name='payment_verify'),
          # path('device_details',views.device_details,name="device_details"),
          
            path('add_contact/', views.add_contact, name='add_contact'),  # Add the contact route
            
             path('manage_contacts/', views.manage_contacts, name='manage_contacts'),  # Add this line

        path('api/get_contact_details/<int:device_id>/', views.get_contact_details, name='get_contact_details'),
        path('logout',views.logout,name="logout"),
        
  #      path('call-response/', views.call_response, name='call_response'),
  #  path('handle-keypress/', views.handle_keypress, name='handle_keypress'),
]