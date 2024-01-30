from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
# Window.size = (300,500)



KV = '''
MDBoxLayout:
    orientation: "vertical"
    
    MDTopAppBar:
        title: "BDMCQ"
        elevation: 0
        md_bg_color: 85,85,85,85
        left_action_items: [["dots-vertical"]]
        right_action_items: [["account-circle-outline"]]
        text_color: (0,0,0,1)
        font_style: 'Body 2'
        
    BoxLayout:
        canvas:
            Color:
                rgb: [.99, .99, .99]
            Rectangle:
                pos: self.pos
                size: self.size
        MDWidget:
            size_hint: .5, None
            height: self.width
            radius: self.height / 2
            
        MDLabel:
            text: "He built the famous Tara Mosque of Dhaka"
            pos_hint: {'center_x': 0.5, 'center_y': 0.9}
            
    BoxLayout:
        canvas:
            Color:
                rgb: [.96, .96, .96]
            Rectangle:
                pos: self.pos
                size: self.size
    
'''


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)


MyApp().run()
