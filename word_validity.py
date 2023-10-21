import sys
import os
import flet as ft

f = open(os.path.join(sys.path[0], "all_words.txt"), "r")
word_list = [i for i in f.read().split()]
def main(page: ft.Page):
    page.title = "Word Validity"

    check_result = ft.Text(value = "", color= "",style=ft.TextThemeStyle.HEADLINE_LARGE, font_family="Verdana")
    def check_valid(e):
        if word.value.lower() not in word_list:
            check_result.value = "Invalid word!"
            check_result.color = "red"
            page.update()
        if word.value.lower() in word_list:
            check_result.value = "Valid word!"
            check_result.color = "green"
            page.update()

    word = ft.TextField(hint_text="Enter your word", expand=True, on_submit=check_valid)
    tasks_view = ft.Column()

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    

    _main_container=ft.Container(
        expand=True,
        gradient=ft.RadialGradient(
            center=ft.Alignment (0.8, 0.8),
            radius=1.4,
            colors=[
                "#14b8a6",
                "#0d9488",
                "#0f766e",
                "#115e59",
                "#134e4a",
                "#1e3e3b",
                "#1a3734",
                "#182726",
            ],
        ),
        padding=30,
        content=ft.Column(
            alignment='center',
            expand=True,
            controls=[
                ft.Text(value = "IS YOUR WORD VALID?",size=40,weight=ft.FontWeight.W_100, font_family="Verdana"),
                ft.Text(value = "Fighting over a word your friend suggested in a game but don't know for sure? Enter it here and you'll figure it out for sure!", style=ft.TextThemeStyle.BODY_LARGE, font_family="Verdana"),
                ft.Row(
                    controls=[
                        word,
                        ft.ElevatedButton("Check", icon=ft.icons.CHECK_ROUNDED, icon_color='#9f59d9' ,on_click = check_valid),
                    ],
                ),
                tasks_view,
                check_result,
            ],
        ),
    )
    _main_container.content.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    _main_container.content.vertical_alignment = ft.CrossAxisAlignment.CENTER


    page.add(_main_container)
    page.update()
    
ft.app(target=main) 