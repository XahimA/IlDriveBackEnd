from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_detail),
    path("cardetail/", views.hello_world),
    path("random/<int:pk>/", views.generate_random),
    path("trip/<int:id_n>/", views.trip_data),
    path("trip_detailcheck/<int:id_t>/", views.get_trip_details),
    path('upload-csv/', views.upload_csv_api, name='upload_csv_api'),
    path('store-mobile-number/', views.store_mobile_number, name='store-mobile-number'),
    path('DriverDetail/', views.driver_detail, name='driver_detail'),     ## check      ## FTested
    path("DriverDetail/<int:pk>/", views.driver_detail, name='driver_detail_detail'),## check    ## FTested
    path('TruckDetail/', views.truck_detail, name='truck_detail'),## check     ## FTested
    path("TruckDetail/<int:pk>/", views.truck_detail, name='truck_detail_detail'),## check      ## FTested
    path('NewtripDetail/', views.newtrip_detail, name='newtrip_detail'),
    path("NewtripDetail/<int:pk>/", views.newtrip_detail, name='newtrip_detail_detail'),
    path('DataDetail/', views.data_detail, name='data_detail'),
    path("DataDetail/<int:pk>/", views.data_detail, name='data_detail_detail'),
    path("OwnerDetail/", views.owner_detail, name='data_owner_detail'),
    path("TruckOwner/<int:pk>", views.truck_owner, name='truck_owner_detail'),
    path("TripDriver/<int:pk>", views.trip_driver, name='trip_driver_detail'),
    path("DriverOwner/<int:pk>", views.driver_owner, name='driver_owner_detail'),
    path("NewtripOwner/<int:pk>", views.NewTrip_owner, name='NewTrip_owner_detail'),
    path("NewTripTruck/<int:pk>", views.NewTrip_Truck, name='NewTrip_Truck_detail')
]
