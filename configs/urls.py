from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from ONW.hostsManager import views as hostsManagerViews
from ONW.groupsManager import views as groupsManagerViews

urlpatterns = [
    path('hosts/' ,hostsManagerViews.list),
    path('host/add' ,hostsManagerViews.add),
    path('host/view/<int:ID>' ,hostsManagerViews.view),
    path('host/edit/<int:ID>' ,hostsManagerViews.edit),
    path('host/delete/<int:ID>' ,hostsManagerViews.delete),

    path('groups/',groupsManagerViews.list),
    path('group/add',groupsManagerViews.add),
    path('group/view/<int:ID>' ,groupsManagerViews.view),
    path('group/edit/<int:ID>',groupsManagerViews.edit),
    path('group/delete/<int:ID>',groupsManagerViews.delete),






    # path('tasks/'),
    # path('task/get/<int:ID:>'),
    # path('task/add/<int:ID:>'),
    # path('task/edit/<int:ID:>'),
    # path('task/delete/<int:ID:>'),
]
