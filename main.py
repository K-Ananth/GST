from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.core.window import Window

class CalculatorApp(MDApp):
    def __init__(self):
        super().__init__()
        self.current_value = ""
        self.dark_mode = False
        self.gst_mode = False

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        Window.clearcolor = self.theme_cls.bg_dark if self.dark_mode else self.theme_cls.bg_light

        # Calculator Layout
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Toolbar
        toolbar = BoxLayout(orientation="horizontal", size_hint=(1, None), height=48, padding=5, spacing=150)
        toolbar.add_widget(MDRectangleFlatButton(text="QuickGST", md_bg_color = (1, 1, 0, 1),text_color=(0, 0, 0, 1), pos_hint={"center_x": 0.5}))
        toolbar.add_widget(MDRectangleFlatButton(text="Dark Mode", md_bg_color = (0.8, 0.8, 0.8, 1),text_color=(0, 0, 0, 1), on_release=self.toggle_dark_mode))

        layout.add_widget(toolbar)

        # Display Label
        self.display_label = MDLabel(
            text="",
            halign='left',
            theme_text_color='Primary',
            font_size='50sp',
            padding=(10, 10),
            size_hint=(1, None),
            height=250
        )
        layout.add_widget(self.display_label)

        # Buttons Layout
        buttons_layout = GridLayout(cols=5, spacing=5, padding=10)
        buttons = [
            '+3%', '+5%', '+12%', '+18%', '+28%',
            '-3%', '-5%', '-12%', '-18%', '-28%',
            '7', '8', '9', '÷', '=',
            '4', '5', '6', 'x', 'C',
            '1', '2', '3', '-', 'AC',
            '0', '00', '.', '+', '%',
        ]

        colors = {
            '+3%':  (0.7, 1, 0.85, 1), '+5%': (0.7, 1, 0.85, 1), '+12%': (0.7, 1, 0.85, 1), '+18%': (0.7, 1, 0.85, 1),
            '+28%': (0.7, 1, 0.85, 1),
            '-3%': (0.7, 1, 0.85, 1), '-5%': (0.7, 1, 0.85, 1), '-12%': (0.7, 1, 0.85, 1), '-18%': (0.7, 1, 0.85, 1),
            '-28%': (0.7, 1, 0.85, 1),
            '%': (0.9, 0.9, 0.9, 1),
            '÷': (0.9, 0.9, 0.9, 1), '=': (0.9, 0.9, 0.9, 1),
            'x': (0.9, 0.9, 0.9, 1), 'C': (0.9, 0.9, 0.9, 1),
            '-': (0.9, 0.9, 0.9, 1),
            '+': (0.9, 0.9, 0.9, 1),
            'AC': (0.9, 0.9, 0.9, 1),
        }

        for button in buttons:
            buttons_layout.add_widget(MDRectangleFlatButton(
                text=button,
                text_color=(0, 0, 0, 1),
                on_release=self.calculate,
                md_bg_color=colors.get(button, (1, 1, 1, 1))  # Set the button color based on the dictionary values
            ))

        layout.add_widget(buttons_layout)
        return layout

    def toggle_dark_mode(self, instance):
        self.dark_mode = not self.dark_mode
        self.theme_cls.theme_style = "Dark" if self.dark_mode else "Light"
        Window.clearcolor = self.theme_cls.bg_dark if self.dark_mode else self.theme_cls.bg_light

    def calculate(self, instance):
        button_text = instance.text

        if button_text == '=':
            if self.gst_mode:
                try:
                    result = eval(self.current_value)
                    cgst = result * (self.gst_rate / 2)
                    sgst = result * (self.gst_rate / 2)
                    igst = result * self.gst_rate
                    tax = cgst + sgst
                    total = result + tax
                    self.display_label.text = f"{self.current_value}\nCGST [{self.gst_rate * 0.5:.1%}]   {cgst:.2f}\nSGST [{self.gst_rate * 0.5:.1%}]   {sgst:.2f}\nIGST [{self.gst_rate:.1%}]    {igst:.2f}\nTax [{self.gst_rate:.1%}]      {tax:.2f}\nTotal               {total:.2f}"
                    self.current_value = str(total)
                except:
                    self.display_label.text = "Error"
            else:
                try:
                    result = eval(self.current_value)
                    self.display_label.text = self.current_value + "\n" + str(result)
                    self.current_value = str(result)

                except:
                    self.display_label.text = "Error"

        elif button_text == 'C':
            if self.current_value:
                self.current_value = self.current_value[:-1]
                self.display_label.text = self.current_value

        elif button_text == 'AC':
            self.current_value = ""
            self.display_label.text = ""

        elif button_text == 'x':
            self.current_value += '*'
            self.display_label.text = self.current_value

        elif button_text == '÷':
            self.current_value += '/'
            self.display_label.text = self.current_value

        elif button_text == '%':
            try:
                result = float(self.current_value) / 100
                self.display_label.text = self.current_value + "\n" + str(result)
                self.current_value = str(result)
            except:
                self.display_label.text = "Error"

        elif button_text.endswith('%'):
            try:
                percentage = float(button_text[:-1]) / 100
                self.gst_rate = percentage
                self.gst_mode = True
                if self.current_value:
                    result = eval(self.current_value)
                    cgst = result * (self.gst_rate / 2)
                    sgst = result * (self.gst_rate / 2)
                    igst = result * self.gst_rate
                    tax = cgst + sgst
                    total = result + tax
                    self.display_label.text = f"{self.current_value}\nCGST [{self.gst_rate * 0.5:.1%}]   {cgst:.2f}\nSGST [{self.gst_rate * 0.5:.1%}]   {sgst:.2f}\nIGST [{self.gst_rate:.1%}]    {igst:.2f}\nTax [{self.gst_rate:.1%}]      {tax:.2f}\nTotal               {total:.2f}"
                    self.current_value = str(total)
                else:
                    self.display_label.text = ""
            except:
                self.display_label.text = "Error"

        else:
            self.current_value += button_text
            self.display_label.text = self.current_value
            self.gst_mode = False
if __name__ == '__main__':
    CalculatorApp().run()