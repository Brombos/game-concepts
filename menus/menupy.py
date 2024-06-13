class button:
    name = ""
    bind = ""
    selected = False

def use_button(button):
    exec(button.bind)

class menu:
    buttons = []
    button_idx = 0
    
    def init(self):
        self.buttons[0].selected = True    
    
    def moveselection_up(self):
        self.buttons[self.button_idx].selected = False
        self.button_idx = self.button_idx + 1
        if self.button_idx == len(self.buttons):
            self.button_idx = 0
        self.buttons[self.button_idx].selected = True

    def moveselection_down(self):
        self.buttons[self.button_idx].selected = False
        self.button_idx = self.button_idx - 1
        if self.button_idx == 0:
            self.button_idx = len(self.buttons) - 1
        self.buttons[self.button_idx].selected = True

    def click():
        exec(self.buttons[self.button_idx].bind)
        