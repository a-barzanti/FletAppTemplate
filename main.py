import flet as ft

async def main(page: ft.Page):
    page.title = "Flet Application"
    main_view = ft.Column([], expand=True)
    page.add(main_view)

ft.app(target=main)
