


class shop:
    text_buttons = []
    def default_setup():
        buy = button()
        sell = button()
        talk = button()
        
        buy.name = "Buy"
        sell.name = "Sell"
        talk.name = "Talk"
    def set_buttons(buttons):
        text_buttons = buttons
    
        
