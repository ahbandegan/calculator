from flet import *

def main(page: Page):
    def press(e):
        try:
            math.color = None
            if e.control.data == "C":
                math.value = math.value[0:-1]

            elif e.control.data == "=":
                math.value = str(eval(math.value))
                math.color = "#00ff00"

            else:
                math.value += e.control.data
            math2.value = eval(math.value)

            math.update()
            page.update()

        except:
            page.update()

    def clear(e):
        math.value = ""
        page.update()

    def key_press(e: KeyboardEvent):
        try:
            math.color = None
            match e.key:
                case "Backspace": math.value = math.value[0:-1]
                case "Numpad Divide": math.value += "/"
                case "Numpad Multiply": math.value += "*"
                case "Numpad Subtract": math.value += "-"
                case "Numpad Add": math.value += "+"
                case "Enter":
                    math.value = str(eval(math.value))
                    math.color = "#00ff00"
                case "Numpad 1": math.value += "1"
                case "Numpad 2": math.value += "2"
                case "Numpad 3": math.value += "3"
                case "Numpad 4": math.value += "4"
                case "Numpad 5": math.value += "5"
                case "Numpad 6": math.value += "6"
                case "Numpad 7": math.value += "7"
                case "Numpad 8": math.value += "8"
                case "Numpad 9": math.value += "9"
                case "Numpad 0": math.value += "0"
            math2.value = eval(math.value)
            math.update()
            page.update()
        except:
            math.update()
            page.update()

    def them(e):
        if e.control.data:
            page.theme_mode = ThemeMode.DARK
            e.control.data = False
        elif not e.control.data:
            page.theme_mode = ThemeMode.LIGHT
            e.control.data = True

        page.update()

    def change(e):
        try:
            math2.value = eval(math.value)
            page.update()
        except:
            pass

    page.on_keyboard_event = key_press
    page.title = "calculator"
    page.window.width = 350
    page.window.height = 630
    page.window.min_width = 350
    page.window.min_height = 630
    page.window.max_width = 350
    page.window.max_height = 630
    page.vertical_alignment = "center"
    page.appbar = AppBar(
        title=Text("Calculator"),
        actions=[
            CupertinoButton(text="them change",on_click=them, data=True)
        ]
    )


    math = TextField(value="", width=310, text_size=25, border_color="#777777", border="underline", keyboard_type=KeyboardType.DATETIME,
                     input_filter=InputFilter(r"[0-9]", True, ""),
                     on_change=change)
    math2 = Text(value="", size=20, color="#777777")
    page.add(
        Row(
            [
                math
            ], alignment="center"
        ),
        Row(
            [
                math2
            ], alignment="END"
        ),
        Divider(15, ),
        Row(
            [
                ElevatedButton(text="C", data="C", height=70, width=70, color="#ff0000", bgcolor="#777777",
                               on_click=press, on_long_press=clear),
                ElevatedButton(text="(", data="(", height=70, width=70, color="#00ff00", bgcolor="#777777",
                               on_click=press),
                ElevatedButton(text=")", data=")", height=70, width=70, color="#00ff00", bgcolor="#777777",
                               on_click=press),
                ElevatedButton(text="/", data="/", height=70, width=70, color="#00ff00", bgcolor="#777777",
                               on_click=press),

            ], alignment="center"
        ), Row(
            [

                ElevatedButton(text="9", data="9", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="8", data="8", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="7", data="7", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="*", data="*", height=70, width=70, color="#00ff00", bgcolor="#777777",
                               on_click=press),
            ], alignment="center"
        ), Row(
            [

                ElevatedButton(text="6", data="6", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="5", data="5", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="4", data="4", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="+", data="+", height=70, width=70, color="#00ff00", bgcolor="#777777",
                               on_click=press),
            ], alignment="center"
        ), Row(
            [

                ElevatedButton(text="3", data="3", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="2", data="2", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="1", data="1", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="-", data="-", height=70, width=70, color="#00ff00", bgcolor="#777777",
                               on_click=press),
            ], alignment="center"
        ), Row(
            [

                ElevatedButton(text="0", data="0", height=70, width=150, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text=".", data=".", height=70, width=70, color="#000000", bgcolor="#ffffff",
                               on_click=press),
                ElevatedButton(text="=", data="=", height=70, width=70, color="#00ff00", bgcolor="#777777",
                               on_click=press),
            ], alignment="center"
        ),
    )


if __name__ == '__main__':
    app(main)
