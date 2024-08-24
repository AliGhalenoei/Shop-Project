from .models import Product
from .serializers import ProductsSerializer

SESSION_CART_ID = 'cart'

class Cart:

    def __init__(self , request) -> None:
        
        """
            create session
        """
        self.session = request.session
        cart = self.session.get(SESSION_CART_ID)

        if not cart:
            cart = self.session[SESSION_CART_ID] = {}
        self.cart = cart

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in = products_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = ProductsSerializer(product).data

        for new_item in self.cart.values():
            new_item['total'] = int(new_item['price']) * new_item['quantity']
            yield new_item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """
            The final price of the shopping cart. 🛒💰
        """
        return sum(int(item["price"] ) * item["quantity"] for item in self.cart.values())

    def add_cart(self , product , quantity):

        """
            Adding a product to the shopping cart.

            Note: 
                If the product is already in the cart, it will increase the quantity.
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0 ,'price':str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove_cart(self , product):

        """
            Remove the product from the shopping cart.

            Note: 
                If the quantity of the products is more than 1, only the quantity will be decreased.
        """

        product_id = str(product.id)

        if product_id in self.cart:

            if self.cart[product_id]['quantity'] > 1:
                self.cart[product_id]['quantity'] -= 1
                self.save()

            else:
                del self.cart[product_id]
                self.save()

    def clear_cart(self):

        """
            Remove the entire shopping cart. 
        """
        del self.session[SESSION_CART_ID]
        self.save()

    def save(self):
        self.session.modified = True