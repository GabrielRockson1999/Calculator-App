import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.10.1")


class CalculatorLayout(BoxLayout):

    def calculate(self, express):
        if not express: return

        try:
            self.display.text = str(eval(express))

        except Exception:
            self.display.text = "error"


class CalculatorApp(App):
    def build(self):
        self.title = "Simple Calculator"
        self.icon = "Calculator-icon.png"
        return CalculatorLayout()

    def on_pause(self):
        return True


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
