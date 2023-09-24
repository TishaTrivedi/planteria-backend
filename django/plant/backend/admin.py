from django.contrib import admin
# from .models import Plant

# admin.site.register(Plant)
# from .models import User, UserOrder

# admin.site.register(User)
# admin.site.register(UserOrder)

from .models import Customers,Plants,Orders,Products,WishList,WishListProduct,Cart,UserRecentlyViewed

# admin.site.register(Category)
admin.site.register(Customers)
admin.site.register(Plants)
admin.site.register(Products)
admin.site.register(WishList)
admin.site.register(WishListProduct)
admin.site.register(Orders)
admin.site.register(Cart)
admin.site.register(UserRecentlyViewed)



# Register your models here.
