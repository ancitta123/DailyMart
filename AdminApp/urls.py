from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
   path('admin',views.adminindex,name='adminindex'),
   path('addc',views.addcategory,name='addcategory'),
   path('categorydata',views.categorydata,name='categorydata'),
   path('viewc',views.viewcategory,name='viewcategory'),
   path('addp',views.addproduct,name='addproduct'),
   path('productdata',views.productdata,name='productdata'),
   path('viewpro',views.viewproduct,name='viewproduct'),
   path('editc/<int:id>',views.editc,name='editc'),
   path('update/<int:id>',views.update,name='update'),
   path('delete/<int:id>',views.delete,name='delete'),
   path('editpro/<int:id>',views.editpro,name='editpro'),
   path('updates/<int:id>',views.updates,name='updates'),
   path('deletes/<int:id>',views.deletes,name='deletes'),
   path('ctable',views.contacttable,name='contacttable'),
   path('rtable',views.registertable,name='registertable'),
    path('order',views.vieworder,name='vieworder')
] 
