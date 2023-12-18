from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math
class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators= ["/", "*", "+", "-", "^"]
        self.last_was_operator =None
        self.last_button= None

        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color="black", foreground_color="white",
                                  multiline=False, halign="right", font_size=55)

        main_layout .add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "^", "-"],
            ["√", "3√", "%", "C"],

        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ""
            self.power_exponent = None
        elif button_text == "√":
            self.calculate_square_root()
        elif button_text == '3√':
            self.calculate_cube_root()
        elif button_text == '%':
            self.calculate_percentage()
        elif button_text == '^':
            self.last_button = button_text
            self.last_was_operator = True
            self.power_exponent = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def calculate_square_root(self):
        current = self.solution.text
        try:
            if current:
                result = str(math.sqrt(float(current)))
                self.solution.text = result
        except ValueError:
            self.solution.text = "Error"

    def calculate_cube_root(self):
        current = self.solution.text
        try:
            if current:
                result = str(math.pow(float(current), 1 / 3))
                self.solution.text = result
        except ValueError:
            self.solution.text = "Error"

    def calculate_power(self):
        current = self.solution.text
        try:
            if current and self.power_exponent is not None:
                result = str(eval(current) ** self.power_exponent)
                self.solution.text = result
        except Exception:
            self.solution.text = "Error"


    def calculate_percentage(self):
        current = self.solution.text
        try:
            if current:
                result = str(float(current) / 100)
                self.solution.text = result
        except ValueError:
            self.solution.text = "Error"
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()