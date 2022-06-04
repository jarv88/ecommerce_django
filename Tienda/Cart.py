class Cart:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        cart=self.session.get("cart")
        
        if not cart:
            self.cart=self.session["cart"]={}
        else:
            self.cart=cart

    def add(self,product):
        #print (self.cart)
        
        if(str(product.id) not in self.cart.keys()):
            self.cart[product.id]={
                "product_id":product.id,
                "code":product.code,
                "title":product.title,
                "price":str(product.price),
                "quantity":1,
                "image":product.image.url
            }
        else:
            for key,value in self.cart.items():
                if key==str(product.id):
                    value["quantity"]=value["quantity"]+1
                    break
        self.saveCart()
    
    def saveCart(self):
        self.session["cart"]=self.cart
        self.session.modified=True

    def deleteFromCart(self,product):
        product.id=str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.saveCart()

    def deductProduct(self,product):
        for key,value in self.cart.items():
                if key==str(product.id):
                    value["quantity"]=value["quantity"]-1
                    if value["quantity"]<1:
                        self.deleteFromCart(product)
                    break
        self.saveCart()
    
    def cleanCart(self):
        self.session["cart"]={}
        self.session.modified=True