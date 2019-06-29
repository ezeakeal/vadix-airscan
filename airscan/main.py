import kivy.app
import kivy.uix.boxlayout
import kivy.uix.textinput
import kivy.uix.label
import kivy.uix.button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp, sp
from screen_scan import ScanScreen
from screen_result import ResultScreen


class Airscan(kivy.app.App):
    # https://stackoverflow.com/questions/46351997/python-kivy-how-to-call-a-function-on-button-click
    report = {}
    scan_data = {}

    def build(self):
        pass


class ScreenManagement(ScreenManager):
    pass


class MainScreen(Screen):

    def scan_button_pressed(self):
        print("Starting scan prep")
        import netifaces as ni
        print("IMported")
        netconns = [i for i in ni.interfaces() if i.startswith("e") or i.startswith("w")]
        print("netConns: %s" % netconns)
        connected = False
        for netcon in netconns:
            print("ifaddresses: %s" % ni.ifaddresses(netcon))
            if ni.AF_INET in ni.ifaddresses(netcon).keys():
                connected = True
        print("Interfaces: %s" % netconns)
        if connected:
            self.parent.current = "scanning"
        else:
            self.box_popup = BoxLayout(orientation = 'vertical')

            self.box_popup.add_widget(Label(
                text="Connect to Wifi first!",
                font_size=sp(20)))

            self.popup_exit = Popup(
                title='Hey now!', 
                content=self.box_popup,
                size_hint = (0.8, 0.3),
                auto_dismiss = True
            )

            self.box_popup.add_widget(Button(
                text = "Okay",
                font_size=sp(20),
                on_press = lambda _: self.popup_exit.dismiss() ,
                size_hint=(0.8, 0.2),
                pos_hint={'center_x':.5}))

            self.popup_exit.open()


if __name__ == "__main__":
    airscan = Airscan()
    airscan.run()
