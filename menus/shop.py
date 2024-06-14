import menupy


class shop:
    shop = menupy.menu()

    def set_buttons(self,buttons):
        shop.buttons = buttons
        shop.init()
        
    def default_setup():
        buy = menupy.button()
        sell = menupy.button()
        talk = menupy.button()
        
        buy.name = "Buy"
        sell.name = "Sell"
        talk.name = "Talk"
        set_buttons([buy,sell,talk])
    
        
tem_shop = shop()
tem_shop.default_setup()