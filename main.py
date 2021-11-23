import webbrowser

from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.core.window import Window  # regulates size of window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, \
    IconLeftWidget, ThreeLineAvatarIconListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.tooltip import MDTooltip
from kivymd.toast import toast
from kivy import platform

from portfolioApp import navigation_drawer, TooltipDot, switch_screen

Window.size = (300, 500)  # window size at runtime :: for development purposes only


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class SocialScreen(Screen):
    pass


class Hello(Screen):
    pass


class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass


sm = ScreenManager()  # ScreenManager added
sm.add_widget(MenuScreen(name='menu'))  # MenuScreen is accessed through name: menu
sm.add_widget(ProfileScreen(name='profile'))  # ProfileScreen is accessed through name: profile
sm.add_widget(SocialScreen(name='social'))  # SocialScreen is accessed through name: social
sm.add_widget(Hello(name='hello'))


class PortfolioApp(MDApp):

    def left_button(self):
        """method to be evoked when menu button of toolbar is clicked"""
        print("Left Button Clicked!")  # displays text when menu button is clicked
        # webbrowser.open('www.google.com')  # open a link in browser on button click

    def right_button(self):
        print("Right Button Clicked!")

    def show_toast(self, text=''):
        """Display Toast while opening apps or links"""
        if platform == 'android':  # 'win' for 'windows'
            toast(text=text, gravity=80, duration=5)
        else:
            toast(text=text, duration=5)

    def build(self):
        self.theme_cls.primary_palette = "LightBlue"  # changes app theme to Teal
        # ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
        #  'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

        self.theme_cls.primary_hue = "200"  # sets hue

        # STARThere

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        # ENDhere

        # screen_toolbar = Builder.load_string(toolbar)
        screen_nav_draw = Builder.load_string(navigation_drawer)
        tooltip = Builder.load_string(TooltipDot)
        screen_switch_screen = Builder.load_string(switch_screen)
        # return screen_toolbar
        return screen_nav_draw
        # return screen_switch_screen

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()

        self.tap_target_view = MDTapTargetView(
            widget=navigation_drawer.ids.button,
            title_text="This is an add button",
            description_text="This is a description of the button",
            widget_position="left_bottom",
        )

        def tap_target_start(self):
            if self.tap_target_view.state == "close":
                self.tap_target_view.start()
            else:
                self.tap_target_view.stop()


if __name__ == '__main__':
    PortfolioApp().run()  # running app
