import flet
from time import sleep
from cipher import cipher_encode, cipher_decode
# import pyperclip

# Vytvoření okna
def main(page: flet.Page):
    page.window_height = 600
    page.window_width = 450
    page.window_left = 900
    page.window_top = 100
    page.title = "Top Secret Communication"
    page.bgcolor = "black"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def home_screen(e):
        main_container.content.clean()
        main_container.content = flet.Container(content=flet.Column([en_button, de_button],
                                                                    alignment=flet.MainAxisAlignment.CENTER,
                                                                    spacing=30),
                                                width=350, height=480, border_radius=15,
                                                gradient=flet.LinearGradient(colors=["#0f766e", "#064e3b"],
                                                                             begin=flet.alignment.top_left,
                                                                             end=flet.alignment.bottom_right),
                                                alignment=flet.alignment.center)
        field_to_encode.value = ""
        encoded_field.value = " "
        field_to_decode.value = ""
        decoded_field.value = " "
        shift_number.value = ""
        page.update()

    def encode_choice(e):
        shift_number.on_submit = encode
        main_container.content.clean()
        main_container.content = flet.Column([flet.Container(flet.Row([text_to_encode], alignment=flet.MainAxisAlignment.CENTER)),
                                              flet.Row([flet.Column(
                                                  [(flet.Container(back_button, padding=flet.padding.only(left=10)))]),

                                                  flet.Container(content=flet.Row([
                                                      flet.Column([flet.Container(
                                                          flet.Text("Kód:", size=18, weight=flet.FontWeight.BOLD),
                                                          padding=flet.padding.only(left=4, right=-8))]),
                                                      flet.Column([flet.Container(shift_number, bgcolor="#28282b",
                                                                                  border_radius=10)])]),
                                                      padding=flet.padding.only(left=5)),

                                                  flet.Column([flet.Container(encode_button,
                                                                              padding=flet.padding.only(
                                                                                  left=9))],
                                                              alignment=flet.MainAxisAlignment.CENTER)]),
                                              flet.Row([encoded_text], alignment=flet.MainAxisAlignment.CENTER)],
                                             alignment=flet.MainAxisAlignment.CENTER, spacing=7)
        shift_number.label = "0-9999"
        page.update()

    def decode_choice(e):
        shift_number.on_submit = decode
        main_container.content.clean()
        main_container.content = flet.Column([flet.Row([text_to_decode], alignment=flet.MainAxisAlignment.CENTER),
                                              flet.Row([flet.Column(
                                                  [(flet.Container(back_button, padding=flet.padding.only(left=10)))]),
                                                  flet.Container(content=flet.Row([
                                                      flet.Column([flet.Container(
                                                          flet.Text("Kód:", size=18, weight=flet.FontWeight.BOLD),
                                                          padding=flet.padding.only(left=4, right=-8))]),
                                                      flet.Column([flet.Container(shift_number, bgcolor="#28282b",
                                                                                  border_radius=10)])]),
                                                      padding=flet.padding.only(left=5)),
                                                  flet.Column([flet.Container(decode_button,
                                                                              padding=flet.padding.only(
                                                                                  left=9))],
                                                              alignment=flet.MainAxisAlignment.CENTER)]),
                                              flet.Row([decoded_text], alignment=flet.MainAxisAlignment.CENTER)],
                                             alignment=flet.MainAxisAlignment.CENTER, spacing=7)
        shift_number.label = "0-9999"
        page.update()

    def erase_shift_numbers(e):
        shift_number.label = ""
        page.update()

    def encode(e):
        legit = True
        if shift_number.value == "":
            error_1 = flet.Container(
                flet.Text("Zadejte hodnotu kódu!", color="red", size=15, weight=flet.FontWeight.BOLD),
                height=35, width=300, bgcolor="#28282b", border=flet.border.all(2, "black"),
                border_radius=10, alignment=flet.alignment.center)
            main_container.content = flet.Column([flet.Row([text_to_encode], alignment=flet.MainAxisAlignment.CENTER),
                                                  flet.Row([error_1], alignment=flet.MainAxisAlignment.CENTER),
                                                  flet.Row([encoded_text], alignment=flet.MainAxisAlignment.CENTER)],
                                                 alignment=flet.MainAxisAlignment.CENTER, spacing=7)
            page.update()
            sleep(3)
            encode_choice(e)
        elif len(shift_number.value) > 4:
            error_2 = flet.Container(
                flet.Text("Kód smí obsahovat maximálně 4 znaky!", color="red", size=15, weight=flet.FontWeight.BOLD),
                height=35, width=300, bgcolor="#28282b", border=flet.border.all(2, "black"),
                border_radius=10, alignment=flet.alignment.center)
            main_container.content = flet.Column([flet.Row([text_to_encode], alignment=flet.MainAxisAlignment.CENTER),
                                                  flet.Row([error_2], alignment=flet.MainAxisAlignment.CENTER),
                                                  flet.Row([encoded_text], alignment=flet.MainAxisAlignment.CENTER)],
                                                 alignment=flet.MainAxisAlignment.CENTER, spacing=7)
            page.update()
            sleep(3)
            shift_number.value = ""
            encode_choice(e)
        else:
            for letter in shift_number.value:
                if letter not in str(list(range(10))):
                    legit = False
                    error_3 = flet.Container(
                        flet.Text("Kód smí obsahovat jen číslice!", color="red", size=15, weight=flet.FontWeight.BOLD),
                        height=35, width=300, bgcolor="#28282b", border=flet.border.all(2, "black"),
                        border_radius=10, alignment=flet.alignment.center)
                    main_container.content = flet.Column(
                        [flet.Row([text_to_encode], alignment=flet.MainAxisAlignment.CENTER),
                         flet.Row([error_3], alignment=flet.MainAxisAlignment.CENTER),
                         flet.Row([encoded_text], alignment=flet.MainAxisAlignment.CENTER)],
                        alignment=flet.MainAxisAlignment.CENTER, spacing=7)
                    page.update()
                    sleep(3)
                    shift_number.value = ""
                    encode_choice(e)
                    break
            if legit:
                key_to_code = int(shift_number.value)
                encoded_field.value = cipher_encode(field_to_encode.value, key_to_code)
                page.update()

    def decode(e):
        legit = True
        if shift_number.value == "":
            error_1 = flet.Container(
                flet.Text("Zadejte hodnotu kódu!", color="red", size=15, weight=flet.FontWeight.BOLD),
                height=35, width=300, bgcolor="#28282b", border=flet.border.all(2, "black"),
                border_radius=10, alignment=flet.alignment.center)
            main_container.content = flet.Column([flet.Row([text_to_decode], alignment=flet.MainAxisAlignment.CENTER),
                                                  flet.Row([error_1], alignment=flet.MainAxisAlignment.CENTER),
                                                  flet.Row([decoded_text], alignment=flet.MainAxisAlignment.CENTER)],
                                                 alignment=flet.MainAxisAlignment.CENTER, spacing=7)
            page.update()
            sleep(3)
            decode_choice(e)
        elif len(shift_number.value) > 4:
            error_2 = flet.Container(
                flet.Text("Kód smí obsahovat maximálně 4 znaky!", color="red", size=15, weight=flet.FontWeight.BOLD),
                height=35, width=300, bgcolor="#28282b", border=flet.border.all(2, "black"),
                border_radius=10, alignment=flet.alignment.center)
            main_container.content = flet.Column([flet.Row([text_to_decode], alignment=flet.MainAxisAlignment.CENTER),
                                                  flet.Row([error_2], alignment=flet.MainAxisAlignment.CENTER),
                                                  flet.Row([decoded_text], alignment=flet.MainAxisAlignment.CENTER)],
                                                 alignment=flet.MainAxisAlignment.CENTER, spacing=7)
            page.update()
            sleep(3)
            shift_number.value = ""
            decode_choice(e)
        else:
            for letter in shift_number.value:
                if letter not in str(list(range(10))):
                    legit = False
                    error_3 = flet.Container(
                        flet.Text("Kód smí obsahovat jen číslice!", color="red", size=15, weight=flet.FontWeight.BOLD),
                        height=35, width=300, bgcolor="#28282b", border=flet.border.all(2, "black"),
                        border_radius=10, alignment=flet.alignment.center)
                    main_container.content = flet.Column(
                        [flet.Row([text_to_decode], alignment=flet.MainAxisAlignment.CENTER),
                         flet.Row([error_3], alignment=flet.MainAxisAlignment.CENTER),
                         flet.Row([decoded_text], alignment=flet.MainAxisAlignment.CENTER)],
                        alignment=flet.MainAxisAlignment.CENTER, spacing=7)
                    page.update()
                    sleep(3)
                    shift_number.value = ""
                    decode_choice(e)
                    break
            if legit:
                key_to_code = int(shift_number.value)
                decoded_field.value = cipher_decode(field_to_decode.value, key_to_code)
                page.update()

    def erase_encode_text(e):
        field_to_encode.value = ""
        field_to_encode.focus()

    def erase_decode_text(e):
        field_to_decode.value = ""
        field_to_decode.focus()

    # def copy_encoded_text(e):
    #     pyperclip.copy(encoded_field.value)
        # data = encoded_field.value
        # subprocess.run("pbcopy", text=True, input=data)


    # Dát na výběr, jestli zprávu zakódovat nebo odkódovat
    en_button = flet.ElevatedButton(content=flet.Text(" Chci zprávu\nZAKÓDOVAT", size=25, font_family="Lucida Sans"),
                                    width=300, height=200, color="white", bgcolor="#28282b", on_click=encode_choice,
                                    style=flet.buttons.ButtonStyle(overlay_color="#303034",
                                                                   side=flet.border.BorderSide(width=2,
                                                                                               color="#28282b"),
                                                                   shape=flet.RoundedRectangleBorder(radius=10)))

    de_button = flet.ElevatedButton(content=flet.Text(" Chci zprávu\nODKÓDOVAT", size=25, font_family="Lucida Sans"),
                                    width=300, height=200, color="white", bgcolor="#28282b", on_click=decode_choice,
                                    style=flet.buttons.ButtonStyle(overlay_color="#303034",
                                                                   side=flet.border.BorderSide(width=2,
                                                                                               color="#28282b"),
                                                                   shape=flet.RoundedRectangleBorder(radius=10)))

    main_container = flet.Container(content=flet.Column([en_button, de_button], alignment=flet.MainAxisAlignment.CENTER,
                                                        spacing=30),
                                    width=350, height=530, border_radius=15,
                                    gradient=flet.LinearGradient(colors=["#0f766e", "#064e3b"],
                                                                 begin=flet.alignment.top_left,
                                                                 end=flet.alignment.bottom_right),
                                    alignment=flet.alignment.center)
    page.add(main_container)

    # Pokud zakódovat, tak se okno přemění:
    # Vytvořit pole, do kterého se bude vkládat text k zakódování
    # Tlačítko na vymazání zadaného textu k zakódování "#22292f"
    erase_encode_button = flet.Container(
        flet.IconButton(icon=flet.icons.DELETE_FOREVER_OUTLINED, icon_color="white", icon_size=25),
        height=200, on_click=lambda e: erase_encode_text(e),
        border_radius=flet.border_radius.only(topLeft=20, bottomLeft=20, topRight=10, bottomRight=10),
        bgcolor="#22292f")
    # Vytvořit pole, do kterého se bude vkládat text k zakódování
    field_to_encode = flet.TextField(label="Zpráva k zakódování", width=252, height=200,
                                     color="#a6a6ac", autofocus=True, cursor_color="#a6a6ac",
                                     text_style=flet.TextStyle(font_family="Frutiger", size=18),
                                     multiline=True, min_lines=6, border_radius=10,
                                     border_color="transparent", text_align=flet.TextAlign.JUSTIFY,
                                     label_style=flet.TextStyle(size=20, color="#d2d2d5",
                                                                weight=flet.FontWeight.BOLD))
    text_to_encode = flet.Container(border=flet.border.all(2, "black"), bgcolor="#28282b", border_radius=10, width=300, padding=flet.padding.only(right=3),
                                    content=flet.Column(spacing=0,
                                                        controls=[
                                                            flet.Row(alignment=flet.MainAxisAlignment.END, spacing=0,
                                                                     controls=[
                                                                         field_to_encode,
                                                                         erase_encode_button])
                                                            ]
                                                        ),
                                    )

    # Vybrat kód pro zakódování (0 - 9999)
    shift_number = flet.TextField(width=70, height=30, color="#a6a6ac", cursor_color="#a6a6ac", label="0-9999",
                                  border_radius=10, border_color="black", text_align=flet.TextAlign.CENTER,
                                  tooltip="Kód pro následné odkódování\nMaximálně 4 znaky\nPouze číslice",
                                  on_focus=erase_shift_numbers, label_style=flet.TextStyle(color="#d2d2d5", size=14))
    # Tlačítko, které zprávu zakóduje
    encode_button = flet.ElevatedButton(text="Zakódovat", icon=flet.icons.MOVE_DOWN, color="#a6a6ac",
                                        bgcolor="#28282b", on_click=encode,
                                        style=flet.ButtonStyle(overlay_color="#303034",
                                                               shape=flet.RoundedRectangleBorder(radius=15),
                                                               side=flet.border.BorderSide(width=1,
                                                                                           color="black")))
    # Tlačítko na zkopírování textu
    # copy_encode_button = flet.Container(flet.IconButton(icon=flet.icons.COPY, icon_size=25, icon_color="white"),
    #                                     height=200, on_click=lambda e: copy_encoded_text(e),
    #                                     border_radius=flet.border_radius.only(topLeft=20, bottomLeft=20, topRight=10,
    #                                                                           bottomRight=10),
    #                                     bgcolor="#22292f")
    # Vypsání zakódovaného textu
    encoded_field = flet.TextField(label="Zakódovaná zpráva", value=" ", width=255, height=200,
                                   color="#a6a6ac", cursor_color="#a6a6ac", read_only=True, border_color="transparent",
                                   text_style=flet.TextStyle(font_family="Frutiger", size=18),
                                   multiline=True, min_lines=6, border_radius=10,
                                   label_style=flet.TextStyle(size=20, color="#d2d2d5",
                                                              weight=flet.FontWeight.BOLD))
    encoded_text = flet.Container(bgcolor="#28282b", border_radius=10, width=300, border=flet.border.all(2, "black"),
                                  content=flet.Column(
                                      controls=[
                                          flet.Row(spacing=0,
                                                   controls=[
                                                       encoded_field,
                                                       # copy_encode_button
                                                   ]
                                                   )
                                      ]
                                  ))

    # Tlačítko "zpět na výběr code/decode" (ideálně šipka)
    back_button = flet.IconButton(icon=flet.icons.ARROW_BACK, icon_color="#a6a6ac", tooltip="Zpět na výběr akce",
                                  bgcolor="#28282b", on_click=home_screen,
                                  style=flet.ButtonStyle(overlay_color="#303034",
                                                         side=flet.border.BorderSide(width=1,
                                                                                     color="black")))

    # Pokud odkódovat, tak se okno přemění:
    # Tlačítko pro smazání inputu:
    erase_decode_button = flet.Container(
        flet.IconButton(icon=flet.icons.DELETE_FOREVER_OUTLINED, icon_color="white", icon_size=25),
        height=190, on_click=lambda e: erase_decode_text(e),
        border_radius=flet.border_radius.only(topLeft=20, bottomLeft=20, topRight=10, bottomRight=10),
        bgcolor="#22292f")
    # gradient=flet.LinearGradient(["#28282b", "transparent"],
    #   begin=flet.alignment.center_left, end=flet.alignment.center_right))
    # border_radius=25, border=flet.border.all(width=0.2, color="#3d3d48"))
    # border=flet.border.only(left=flet.border.BorderSide(width=0.2, color="silver")))

    # Vytvořit pole, do kterého se bude vkládat text k odkódování
    field_to_decode = flet.TextField(label="Zpráva k odkódování", width=255, height=200,
                                     color="#a6a6ac", autofocus=True, cursor_color="#a6a6ac",
                                     text_style=flet.TextStyle(font_family="Frutiger", size=18),
                                     multiline=True, min_lines=6, border_radius=10,
                                     border_color="transparent",
                                     label_style=flet.TextStyle(size=20, color="#d2d2d5",
                                                                weight=flet.FontWeight.BOLD))
    text_to_decode = flet.Container(border=flet.border.all(2, "black"), bgcolor="#28282b", border_radius=10, width=300,
                                    content=flet.Column(spacing=1,
                                                        controls=[
                                                            flet.Row(alignment=flet.MainAxisAlignment.END, spacing=1,
                                                                     controls=[
                                                                         field_to_decode,
                                                                         erase_decode_button])
                                                            ]
                                                        ),
                                    )
    # Tlačítko, které zprávu odkóduje (posun o -43)
    # Vypsání odkódovaného textu
    decoded_field = flet.TextField(label="Odkódovaná zpráva", value=" ", width=300, height=200,
                                   color="#a6a6ac", cursor_color="#a6a6ac", read_only=True,
                                   text_style=flet.TextStyle(font_family="Frutiger", size=18),
                                   multiline=True, min_lines=6, border_radius=10, border_color="black",
                                   label_style=flet.TextStyle(size=20, color="#d2d2d5",
                                                              weight=flet.FontWeight.BOLD))
    decoded_text = flet.Container(decoded_field, bgcolor="#28282b", border_radius=10)

    # Tlačítko "zpět na výběr code/decode" (ideálně šipka)
    decode_button = flet.ElevatedButton(text="Odkódovat", icon=flet.icons.MOVE_DOWN, color="#a6a6ac",
                                        bgcolor="#28282b", on_click=decode,
                                        style=flet.ButtonStyle(overlay_color="#303034",
                                                               shape=flet.RoundedRectangleBorder(radius=15),
                                                               side=flet.border.BorderSide(width=1,
                                                                                           color="black")))


# Spuštění programu

if __name__ == "__main__":
    flet.app(target=main)
