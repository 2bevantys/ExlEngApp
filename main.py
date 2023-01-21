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
from kivymd.uix.list import OneLineListItem


KV = '''
Screen:

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
                            size_hint: .5, .7
                            pos_hint: {"center_x": .5, "center_y": .5}
                            elevation: 4
                            shadow_radius: 6
                            shadow_offset: 0, 2
                            
                            MDFloatLayout:
                                adaptive_height: True
                                
                                MDRaisedButton:
                                    id: button_for_score
                                    text: 'score:'
                                    md_bg_color: "blue"
                                    pos_hint: {"center_x": .1, "center_y": .82}
                                
                                MDRaisedButton:
                                    id: ban_this_word
                                    text: 'ban this word'
                                    md_bg_color: "blue"
                                    pos_hint: {"center_x": .855, "center_y": .82}
                                    on_release: app.ban_word()
                                    
                            MDBoxLayout:   
                                MDLabel:
                                    id: text_label
                                    text: 'empty'
                                    halign: 'center'
                                    valign: 'center'
                                    bold: True
                                    font_style: "H4"
                                
                            MDFloatLayout:                  
                        
                                MDTextField:
                                    id: text_field
                                    hint_text: "translate here"
                                    mode: "fill"
                                    pos_hint: {"center_x": .5, "center_y": .7}
                                    helper_text: "you made a mistake"
                                    helper_text_mode: "on_error"
                            
                                
                                MDRaisedButton:
                                    id: button_for_run
                                    text: "verify"
                                    md_bg_color: "grey"
                                    pos_hint: {"center_x": .855, "center_y": .2}
                                    on_release: app.next_word()
                                    size_hint:
                    
                    Tab:
                        title: "Tab 2"
                    
                        MDScrollView:

                            MDList:
                                id: container
                        
        
        

    
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
        self.screen = Builder.load_string(KV)
        self.screen.ids.text_label.text = f'{self.word_eng}'
        self.screen.ids.button_for_score.text = f"score: {self.score_word}"
        # self.screen.ids.text_field.bind(
        #     on_text_validate=self.set_error_message,
        #     on_focus=self.get_date,
        # )

        return self.screen

    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )

    def next_word(self):
        if self.screen.ids.text_field.text:
            if self.screen.ids.text_field.text == self.word_rus:
                self.score_plus()
                self.search_word()
                self.screen.ids.button_for_run.md_bg_color = "green"
                self.screen.ids.text_label.text = self.word_eng
                self.screen.ids.text_field.text = ''

            else:
                self.screen.ids.button_for_run.md_bg_color = "red"
                self.screen.ids.text_field.error = True



    def get_date(self):
        print(self.screen.ids.text_field.text)

    # def on_start(self):
    #     for name_tab in self.icons:
    #         tab = Tab(title=name_tab, icon=name_tab)
    #         self.root.ids.tabs.add_widget(tab)

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):


        textttt = tab_text
        print(f"Welcome to {textttt}")

    def search_word(self):
        conn = sq.connect("exleng.db")
        cur = conn.cursor()
        random_id = randrange(1, 888)
        cur.execute("""SELECT * FROM words WHERE word_id=? AND ban_word=0""", (random_id,))
        for_print = cur.fetchone()
        cur.close()
        self.id_word = for_print[0]
        self.word_eng = for_print[1]
        self.word_rus = for_print[2]
        self.score_word = for_print[3]
        self.info_ban_word = for_print[4]
        print(for_print)

    def ban_word(self):
        conn = sq.connect("exleng.db")
        cur = conn.cursor()
        cur.execute("""UPDATE words SET ban_word=1 WHERE word_id=?""", (self.id_word,))
        conn.commit()
        cur.close()


    def score_plus(self):
        conn = sq.connect("exleng.db")
        cur = conn.cursor()
        cur.execute("""UPDATE words SET score = score + 1 WHERE word_id=?""", (self.id_word,))
        conn.commit()
        cur.close()


if __name__ == '__main__':
    Exleng().run()
