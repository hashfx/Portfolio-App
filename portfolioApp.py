# toolbar = """
# Screen:
#     BoxLayout:
#         orientation: 'vertical'  # orientation of toolbar
#         MDToolbar:
#             title: 'Portfolio App'  # title of toolbar
#             md_bg_color: app.theme_cls.accent_color
#             left_action_items: [["menu", lambda x: app.navigation_draw()]]  # icon at left with response
#             elevation: 10  # generates shadow under toolbar
#
#         MDLabel:  # displays a label on screen
#             text: 'Hello, Label!'
#             halign: 'center'  # aligns label at center of screen
#
#         MDBottomAppBar:  # displays toolbar at bottom of the screen
#             MDToolbar:
#                 # title: 'StatusBar'  # title of toolbar
#                 left_action_items: [["home", lambda x: app.navigation_draw()]]
#                 mode: 'end'  # action_button modes :: 'end' ; 'free-end'
#                 type: 'bottom'  # elevates action_button
#                 icon: 'apple'  # icon of action_button
#                 on_action_button: app.navigation_draw()  # response of action_button
# """

# Main Screen + Toolbar [Top + Bottom] + Navigation Drawer


navigation_drawer = """
Screen: 
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'  # orientation of toolbar
                    MDToolbar:
                        title: 'Portfolio App'  # title of toolbar
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open"), "Menu"]]  # toggle nav_draw
                        right_action_items: [["dots-vertical", lambda x: app.callback(x), "Tooltip"]]  # Tooltip :: ,["clock", lambda x: app.callback(x)]
                        elevation: 10  # generates shadow under toolbar
                        
                    # MDLabel:  #  [!important]
                    #     text: 'Text Here'  # display dummy text for menu [!important]
                    #     halign: 'center'  # center [!important]
                    
                    # MDBottomAppBar:  # displays toolbar at bottom of the screen
                    #     MDToolbar:
                    #         # title: 'StatusBar'  # title of toolbar
                    #         left_action_items: [["instagram", lambda x: app.left_button()]]
                    #         right_action_items: [["github", lambda x: app.right_button()]]
                    #         mode: 'center'  # action_button modes :: 'end'; 'free-end'; 'center'; free-center
                    #         type: 'bottom'  # elevates action_button
                    #         icon: 'home'  # icon of action_button
                    #         icon_color: 1, 1, 0, 1  # action_button icon color
                    #         on_action_button: app.navigation_draw()  # response of action_button
                    
                    MDBottomNavigation:
                        panel_color: 1,1,1,1
            
                        MDBottomNavigationItem:
                            name: 'screen 1'  # todo: add response to tabs
                            text: 'Home'
                            icon: 'home'

                            MDLabel:
                                text: 'Home Text'
                                halign: 'center'
                            
            
                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'Projects'
                            icon: 'folder-account-outline'
            
                            MDLabel:
                                text: 'Projects Text'
                                halign: 'center'
                            
                                    
            
                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'Social Media'
                            icon: 'television'
            
                            MDLabel:
                                text: 'Social Media Text'
                                halign: 'center'        
                    # Widget:

        MDNavigationDrawer:
            id: nav_drawer  # when button is clicked, id:nav is called
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'favicon.png'  # image added to Navigation Drawer
                MDLabel:
                    text: '   Harsh Soni'
                    font_style: 'Subtitle1'
                    size_hint_y: None  # do not use automatic height
                    height: self.texture_size[1]
                MDLabel:
                    text: '    IG@hash.prog'
                    font_style: 'Caption'
                    size_hint_y: None  # do not use automatic height
                    height: self.texture_size[1]
                MDLabel:
                    text: '    gh@hashfx'
                    font_style: 'Caption'
                    size_hint_y: None  # do not use automatic height
                    height: self.texture_size[1]

                ScrollView:  # aligns everything to top
                    MDList:  # list inside Navigation Drawer
                        TwoLineIconListItem:
                            text: 'hash.prog'
                            secondary_text: 'Instagram'
                            on_release: app.show_toast(text='Instagram')  # toast added
                            on_release: print("Instagram")  # open ig_link
                            IconLeftWidget:
                                icon: 'instagram'
                        TwoLineIconListItem:
                            text: 'hashfx'
                            secondary_text: 'Github'
                            on_release: app.show_toast(text='Github')  # toast added
                            on_release: print("Github")  # open gh_link
                            IconLeftWidget:
                                icon: 'github'
"""

TooltipDot = """
<TooltipMDIconButton>
Screen:
    TooltipMDIconButton:
        icon: "android"
        tooltip_text: self.icon
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        

"""

switch_screen = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    SocialScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'profile'  # on_click: return ProfileScreen
    MDRectangleFlatButton:
        text: 'Social Profile'
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        on_press: root.manager.current = 'social'  # on_click: return SocialScreen

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome!'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.2}
        on_press: root.manager.current = 'menu'  # on_click: return MenuScreen

<SocialScreen>:
    name: 'social'
    MDLabel:
        text: 'Yeah boi, full SocialBaazi!'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        on_press: root.manager.current = 'menu'  # on_click: return MenuScreen
"""