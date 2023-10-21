import flet as ft
f = open("C:/work/introToFlet/word.txt", "r")
word_list = [i for i in f.read().split()]
def main(page):
    page.title = "Word Validity"
    check_result = ft.Text(value = "", color= "")
    def check_valid(e):
        if word.value not in word_list:
            check_result.value = "invalid word!"
            check_result.color = "red"
            page.update()
        if word.value in word_list:
            check_result.value = "valid word!"
            check_result.color = "green"
            page.update()
    page.add(ft.Text(value = "IS YOUR WORD VALID?"))
    page.add(ft.Text(value = "Fighting over a word your friend suggested in a game but don't know for sure? Enter it here and you'll figure it out for sure!"))
    word = ft.TextField(hint_text="Enter your word")
    page.add(ft.Row([word, ft.ElevatedButton("Check", on_click = check_valid)]))
    page.add(check_result)
ft.app(target=main)