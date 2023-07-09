from django.contrib import admin

from vaibhav_app.models import Contact,Cposting,Blog_Post,Post,BlogComment
# Register your models here.

admin.site.register(Contact)
admin.site.register(Cposting)
admin.site.register(Blog_Post)
admin.site.register((Post,BlogComment))


'''admin.site.register(Room)
admin.site.register(Message)'''

