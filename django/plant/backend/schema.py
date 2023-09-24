import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Customers,Orders,Plants,WishList,Products,WishListProduct,Cart,UserRecentlyViewed
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CustomerType(DjangoObjectType):
    class Meta:
        model=Customers
        fields="__all__"

class PlantType(DjangoObjectType):
    class Meta:
        model=Plants
        fields="__all__"

class ProductsType(DjangoObjectType):
    class Meta:
        model=Products
        fields="__all__"

class CustomerLikedPlantsType(DjangoObjectType):
    class Meta:
        model=WishList
        fields="__all__"

class CustomerLikedProductsType(DjangoObjectType):
    class Meta:
        model=WishListProduct
        fields="__all__"

class OrderType(DjangoObjectType):
    class Meta:
        model=Orders
        fields="__all__"

class CartType(DjangoObjectType):
    class Meta:
        model = Cart
        fields = "__all__"

class UserRecentlyViewedType(DjangoObjectType):
    class Meta:
        model = UserRecentlyViewed
        fields = "__all__"


class Query(graphene.ObjectType):

    #customer
    all_customers=graphene.List(CustomerType)
    displayCustomerById=graphene.Field(CustomerType,id=graphene.ID(required=True))
    
    def resolve_all_customers(self,info):
        return Customers.objects.all()
    
    def resolve_displayCustomerById(self,info,id):
        try:
            return Customers.objects.get(id=id)
        except Customers.DoesNotExist:
            raise GraphQLError(f"Customer with Id{id} does not exist. ")
        
    
    #Plant
    all_plants=graphene.List(PlantType)
    plantsById=graphene.Field(PlantType,id=graphene.ID(required=True))
    plantsByCategory=graphene.List(PlantType,category=graphene.String(required=True))
    plantsBySubCategory=graphene.List(PlantType,subcategory=graphene.String(required=True))
    plantsByName=graphene.List(PlantType, plant_name=graphene.String(required=True))
    plantsBySize=graphene.List(PlantType,size=graphene.String(required=True))
    plantsByMainCategory=graphene.List(PlantType,mainCategory=graphene.String(required=True))

    def resolve_all_plants(self,info):
        return Plants.objects.all()
    
    def resolve_plantsById(self,info,id):
        try:
            return Plants.objects.get(id=id)
        except Plants.DoesNotExist:
            raise GraphQLError(f"Plant with ID {id} does not exist.")

    def resolve_plantsByMainCategory(self,info,mainCategory):
        try:
            return Plants.objects.filter(mainCategory=mainCategory)
        except Plants.DoesNotExist:
            return None
            
    def resolve_plantsByCategory(self,info,category):
        try:
            return Plants.objects.filter(category=category)
        except Plants.DoesNotExist:
            return None
        
    def resolve_plantsBySubCategory(self,info,subcategory):
        try:
            return Plants.objects.filter(subcategory=subcategory)
        except Plants.DoesNotExist:
            return None

    def resolve_plantsByName(self,info,plant_name):
        try:
            return Plants.objects.filter(plant_name=plant_name)
        except Plants.DoesNotExist:
            return None
        
    def resolve_plantsBySize(self,info,size):
        try:
            return Plants.objects.filter(size=size)
        except Plants.DoesNotExist:
            return None

#fertilizers,tools,pots

    all_products=graphene.List(ProductsType)
    productsById=graphene.Field(ProductsType,id=graphene.ID(required=True))
    productsByCategory=graphene.List(ProductsType,mainCategory=graphene.String(required=True))

    def resolve_all_products(self,info):
        return Products.objects.all()
    
    def resolve_productsById(self,info,id):
        try:
            return Products.objects.get(id=id)
        except Products.DoesNotExist:
            raise GraphQLError(f"Plant with ID {id} does not exist.")

    def resolve_productsByCategory(self,info,mainCategory):
        try:
            return Products.objects.filter(mainCategory=mainCategory)
        except Products.DoesNotExist:
            return None
            

    #favorite plants
    
    displayCustomerLikedPlants= graphene.List(CustomerLikedPlantsType)
    displayCustomerLikedPlantsById=graphene.List(CustomerLikedPlantsType,customerId=graphene.ID(required=True))


    def resolve_displayCustomerLikedPlants(self,info):
        return WishList.objects.all()


    def resolve_displayCustomerLikedPlantsById(self,info,customerId):
        try:
            return WishList.objects.filter(customerId=customerId).order_by('-likedPlants')
        except WishList.DoesNotExist:
            raise GraphQLError(f"Customer with ID {customerId} does not have any liked products.")
        
    #favorite products
    displayCustomerLikedProduct= graphene.List(CustomerLikedProductsType)
    displayCustomerLikedProductsById=graphene.List(CustomerLikedProductsType,customerId=graphene.ID(required=True))


    def resolve_displayCustomerLikedProducts(self,info):
        return WishListProduct.objects.all()


    def resolve_displayCustomerLikedProductsById(self,info,customerId):
        try:
            return WishListProduct.objects.filter(customerId=customerId).order_by('-likedProducts')
        except WishListProduct.DoesNotExist:
            raise GraphQLError(f"Customer with ID {customerId} does not have any liked products.")

    #orders
    all_orders=graphene.List(OrderType)
    orderById=graphene.Field(OrderType,orderId=graphene.ID(required=True))
    
    
    
    def resolve__all_orders(self,info):
        return Orders.objects.all()
    
    def resolve_ordersById(self,info,orderId):
        try:
            return Orders.objects.get(orderId=orderId)
        except Orders.DoesNotExist:
            raise GraphQLError(f"Order with Id {id} does not exist.")
        
    #cart    
    userCart = graphene.List(CartType)
    userCartById=graphene.List(CartType,id=graphene.ID(required=True))

    def resolve_userCart(self, info):

        return Cart.objects.all()    

    def resolve_userCartById(self, info, id):
        try:

            return Cart.objects.filter(id=id)

        except Cart.DoesNotExist:
            raise GraphQLError(f"User with ID {id} does not have anything in their cart.")    
        
    #Recently Viewed
    displayUserRecentlyViewed = graphene.List(UserRecentlyViewedType, customerId=graphene.ID(required=True))

    def resolve_displayUserRecentlyViewed(self, info, customerId):
        try:
            return UserRecentlyViewed.objects.filter(customerId=customerId).order_by('-recentlyViewedTime')
        except UserRecentlyViewed.DoesNotExist:
            raise GraphQLError(f"Customer with ID {customerId} hasn't seen any products")


#Mutations

class CreateCustomer(graphene.Mutation):

    customer=graphene.Field(CustomerType)

    class Arguments:
           
           fullName=graphene.String(required=True)
           address=graphene.String(required=True)
           city=graphene.String(required=True)
           state=graphene.String(required=True)
           zipCode=graphene.String(required=True)
           country=graphene.String(required=True)
           phone=graphene.String(required=True)
          
            
    def mutate(self,info,fullName,address,city,state,zipCode,country,phone):
        customer=Customers(fullName=fullName,address=address,city=city,state=state,zipCode=zipCode,country=country,phone=phone)
        customer.save()
        return CreateCustomer(customer=customer)

class CreatePlant(graphene.Mutation):
    plant=graphene.Field(PlantType)

    class Arguments:
        plant_name = graphene.String()
        desc = graphene.String()
        size = graphene.String()
        family = graphene.String()
        price = graphene.Int()
        category = graphene.String()
        sunlight = graphene.String()
        water = graphene.String()
        fertilizer = graphene.String()
        
        subcategory = graphene.String()
        images=graphene.String()
        


    def mutate(self,info,**kwargs):
        plant=Plants(**kwargs)
        plant.save()
        return CreatePlant(plant=plant)
    
class CreateProducts(graphene.Mutation):
    products=graphene.Field(ProductsType)

    class Arguments:
        mainCategory = graphene.String()
        product_name = graphene.String()
        description =graphene.String()
        price = graphene.Int()
        size = graphene.String()
        images = graphene.String()

    def mutate(self,info,**kwargs):
        products=Products(**kwargs)
        products.save()
        return CreatePlant(products=products)    
    
class CreateOrder(graphene.Mutation):
    order=graphene.Field(OrderType)

    class Arguments:
        product_id = graphene.Int()
        customer_id = graphene.Int()
       # plant_id=graphene.Int()
        quantity = graphene.Int()
        price = graphene.Int()
        # address = graphene.String()
        # phone = graphene.String()
        # date = graphene.String()
        # status = graphene.Boolean()
        #address,phone,date,status
    def mutate(self,info,product_id,customer_id,quantity,price):
        product=Plants.objects.get(pk=product_id)
        customer=Customers.objects.get(pk=customer_id)
        # ,address=address,phone=phone,date=date,status=status
        order=Orders(product=product,customer=customer,quantity=quantity,price=price)
        order.save()
        return CreateOrder(order=order)


class AddPlantsToWishList(graphene.Mutation):
    class Arguments:
        customerId=graphene.ID(required=True)
        plantId=graphene.ID(required=True)

    saved_plant= graphene.Field(CustomerLikedPlantsType)

    def mutate(self,info,customerId,plantId):
        try:
            customer=Customers.objects.get(id=customerId)
            plant=Plants.objects.get(id=plantId)
            saved_plant=WishList(customerId=customer,plantId=plant)
            saved_plant.save()
            return AddPlantsToWishList(saved_plant=saved_plant)
        except Customers.DoesNotExist:
            raise GraphQLError(f"Customer with ID {customerId} does not have any liked products.")
        except Plants.DoesNotExist:
            raise GraphQLError(f"Product with ID {plantId} does not have any liked products.")

class RemovePlantsFromWishlist(graphene.Mutation):
    class Arguments:
        customerId = graphene.ID(required=True)
        plantId = graphene.ID(required=True)
   
    deletedCount = graphene.Int()

    def mutate(self, info, customerId, plantId):
        try:
            # Attempt to retrieve the WishList object
            customer_saved_plant = WishList.objects.get(customerId=customerId, plantId=plantId)
            customer_saved_plant.delete()
            return RemovePlantsFromWishlist(deletedCount=1)
        except WishList.DoesNotExist:
            # Handle the case where the WishList object does not exist
            return RemovePlantsFromWishlist(deletedCount=0)
    

#mutation for liked products
class AddProductsToWishList(graphene.Mutation):
    class Arguments:
        customerId=graphene.ID(required=True)
        productId=graphene.ID(required=True)

    saved_product= graphene.Field(CustomerLikedProductsType)

    def mutate(self,info,customerId,productId):
        try:
            customer=Customers.objects.get(id=customerId)
            product=Products.objects.get(id=productId)
            saved_product=WishListProduct(customerId=customer,productId=product)
            saved_product.save()
            return AddProductsToWishList(saved_product=saved_product)
        except Customers.DoesNotExist:
            raise GraphQLError(f"Customer with ID {customerId} does not have any liked products.")
        except Products.DoesNotExist:
            raise GraphQLError(f"Product with ID {productId} does not have any liked products.")

class RemoveProductsFromWishList(graphene.Mutation):
    class Arguments:
        customerId=graphene.ID(required=True)
        productId=graphene.ID(required=True)
   
    deletedCount=graphene.Int()

    def mutate(self,info,customerId,productId):
        try:
            customer_saved_product=WishListProduct.objects.get(customerId=customerId,productId=productId)
            customer_saved_product.delete()
            return RemoveProductsFromWishList(deletedCount=1)
        except WishListProduct.DoesNotExist:
            return RemoveProductsFromWishList(deletedCount=0)



           

class AddToCart(graphene.Mutation):
    class Arguments:
        customerId = graphene.ID(required=True)
        itemId = graphene.ID(required=True)
        itemType = graphene.String(required=True)
        quantity = graphene.Int(required=True)  # Add quantity argument

    saved_product = graphene.Field(CartType)

    def mutate(self, info, customerId, itemId, itemType, quantity):
        try:
            customer = Customers.objects.get(id=customerId)

            if itemType == "product":
                product = Products.objects.get(id=itemId)
                saved_product, created = Cart.objects.get_or_create(customer=customer, product=product)
            elif itemType == "plant":
                plant = Plants.objects.get(id=itemId)
                saved_product, created = Cart.objects.get_or_create(customer=customer, plant=plant)
            else:
                raise GraphQLError("Invalid itemType. It must be 'product' or 'plant'.")

            if not created:
                # If the item is already in the cart, update the quantity
                saved_product.quantity += quantity
            else:
                saved_product.quantity = quantity

            saved_product.save()
            return AddToCart(saved_product=saved_product)
        except Customers.DoesNotExist:
            raise GraphQLError(f"Customer with ID {customerId} does not exist.")
        except Products.DoesNotExist:
            raise GraphQLError(f"Product with ID {itemId} does not exist.")
        except Plants.DoesNotExist:
            raise GraphQLError(f"Plant with ID {itemId} does not exist.")


class RemoveFromCart(graphene.Mutation):

    class Arguments:
        customerId = graphene.ID(required=True)
        itemId = graphene.ID(required=True)
        itemType = graphene.String(required=True)

    deletedCount=graphene.Int()
    def mutate(self, info, customerId, itemId, itemType):
        try:
            customer = Customers.objects.get(id=customerId)
            if itemType =="product":
                product=Products.objects.get(id=itemId)
                customer_cart_product=Cart.objects.get(customer=customer,product=product)
                customer_cart_product.delete()
                return RemoveFromCart(deletedCount=1)
            
            elif itemType =="plant":
                plant=Plants.objects.get(id=itemId)
                customer_cart_product=Cart.objects.get(customer=customer,plant=plant)
                customer_cart_product.delete()
                return RemoveFromCart(deletedCount=1)

        except Cart.DoesNotExist:
            return RemoveFromCart(deletedCount=0)     
        except Customers.DoesNotExist:
            raise GraphQLError(f"Customer with ID {customerId} does not exist.")
        except Products.DoesNotExist:
            raise GraphQLError(f"Product with ID {itemId} does not exist.")
        except Plants.DoesNotExist:
            raise GraphQLError(f"Plant with ID {itemId} does not exist.")

from django.utils import timezone
class AddToRecentlyViewed(graphene.Mutation):
    class Arguments:
        customerId = graphene.ID(required=True)
        itemId = graphene.ID(required=True)
        itemType = graphene.String(required=True)
        
    recentlyViewed = graphene.Field(UserRecentlyViewedType)

    def mutate(self, info, customerId, itemId, itemType):
        try:
            customer = Customers.objects.get(id=customerId)
            product = None 
            plant=None
            if itemType == "product":
                product = Products.objects.get(id=itemId)
                # print(str(product.query))
                existing_entry = UserRecentlyViewed.objects.filter(customerId=customer, productId=product).first()
            
            elif itemType == "plant":
                plant = Plants.objects.get(id=itemId)
                existing_entry = UserRecentlyViewed.objects.filter(customerId=customer, plantId=plant).first()
            
            else:
                raise GraphQLError("Invalid itemType. It must be 'product' or 'plant'.")

            if existing_entry:
                existing_entry.recentlyViewedTime = timezone.now()
                existing_entry.save()
                return AddToRecentlyViewed(recentlyViewed=existing_entry)

            viewed_count = UserRecentlyViewed.objects.filter(customerId=customer).count()

            if viewed_count >= 5:
                oldest_entry = UserRecentlyViewed.objects.filter(customerId=customer).order_by('-recentlyViewedTime').first()
                oldest_entry.plantId = plant if itemType == "plant" else oldest_entry.plantId
                oldest_entry.productId = product if itemType == "product" else oldest_entry.productId
                oldest_entry.recentlyViewedTime = timezone.now()
                oldest_entry.save()
                return AddToRecentlyViewed(recentlyViewed=oldest_entry)
            else:
                recentlyViewed = UserRecentlyViewed(customerId=customer, plantId=plant, productId=product, recentlyViewedTime=timezone.now())
                recentlyViewed.save()
                return AddToRecentlyViewed(recentlyViewed=recentlyViewed)

        except Customers.DoesNotExist:
            raise GraphQLError(f"Customer with Id {customerId} does not exist")
        except Plants.DoesNotExist:
            raise GraphQLError(f"Plant with Id {itemId} does not exist")
        except Products.DoesNotExist:
            raise GraphQLError(f"Product with id {itemId} does not exist")

class Mutation(graphene.ObjectType):
    create_customer= CreateCustomer.Field()
    create_plant=CreatePlant.Field()
    create_products=CreateProducts.Field()
    create_order=CreateOrder.Field()

    add_plants_to_wishlist=AddPlantsToWishList.Field()
    remove_plants_from_wishlist=RemovePlantsFromWishlist.Field()

    add_products_to_wishlist=AddProductsToWishList.Field()
    remove_products_from_wishlist=RemoveProductsFromWishList.Field()

    add_to_cart = AddToCart.Field()
    remove_from_cart= RemoveFromCart.Field()
    # update_cart_item_quantity = UpdateCartItemQuantity.Field()

    add_to_recently_viewed = AddToRecentlyViewed.Field()



schema=graphene.Schema(query=Query,mutation=Mutation)

