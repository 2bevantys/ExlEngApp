from random import randrange
import sqlite3 as sq
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.properties import StringProperty, ListProperty
from kivymd.icon_definitions import md_icons



runwords_KV = '''
Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'
    

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1
                
                        
                        
                        Tab:
                            title: "Tab 1"
                            

                            MDCard:
                                orientation: 'vertical'
                                padding: 0, 0, 0 , "36dp"
                                size_hint: .5, .5
                                pos_hint: {"center_x": .5, "center_y": .5}
                                elevation: 4
                                shadow_radius: 6
                                shadow_offset: 0, 2
                                
                                
                        
                                MDLabel:
                                    id: word_label
                                    text: 'app.search_word '
                                    halign: "center"
                                    valign: "center"
                                    bold: True
                                    font_style: "H5"
                                                                      
                        
                                MDTextField:
                                    hint_text: "translate here"
                                    mode: "fill"
                                    pos_hint: {"center_x": .5, "center_y": .5}
                                    
                                
                        
                        
                        
                        Tab:
                            title: "Tab 2"
                        
                            MDCard:
                                
                                padding: 0, 0, 0 , "36dp"
                                size_hint: .5, .5
                                pos_hint: {"center_x": .5, "center_y": .5}
                                elevation: 4
                                shadow_radius: 6
                                shadow_offset: 0, 2
                            
                                MDLabel:
                                    
                                    text: "Fake"
                                    halign: "center"
                                    valign: "center"
                                    bold: True
                                    font_style: "H5"
                        
        
        

    
'''
class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))

class Tab(MDFloatLayout, MDTabsBase):

    icon = ObjectProperty()




class Exleng(MDApp):



    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.search_word()


        return Builder.load_string(runwords_KV)

    # def on_start(self):
    #     for name_tab in self.icons:
    #         tab = Tab(title=name_tab, icon=name_tab)
    #         self.root.ids.tabs.add_widget(tab)

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        count_icon = instance_tab.icon
        print(f"Welcome to {count_icon}' tab'")

    def search_word(self):
        conn = sq.connect("exleng.db")
        cur = conn.cursor()
        random_id = randrange(1, 1000)
        cur.execute("""SELECT word, translate FROM words WHERE word_id=? AND ban_word=0""", (random_id,))
        for_print = cur.fetchone()
        cur.close()
        self.word_eng = for_print[0]
        self.word_rus = for_print[1]
        print(for_print)
        # self.root.ids.word_label.text = f'{for_print[0]}'




Exleng().run()
