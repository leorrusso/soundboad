import flet as ft

def main(page: ft.Page):
    
    page.bgcolor = "#f5f5f5"
    page.padding = 16

    items = [
        {
            "name": "Pedro",
            "image": "/01.jpeg",
            "sound":"/pedroGemido1.m4a"
        },
        {
            "name": "Rud",
            "image": "/02.jpeg",
            "sound":"/rudGemido.m4a"
        },
        {
            "name": "Dani",
            "image": "/03.jpeg",
            "sound":"/daniDisruptivo.m4a"
        },
        {
            "name": "Edu",
            "image": "/04.jpeg",
            "sound":"/Duck-quack.mp3"
        }
    ]

    title = ft.Container(content=ft.Text("Soundboard", size=32, color="#222222"))
    currentAudio = ft.Audio(src='/Duck-quack.mp3',autoplay=True)

    
    def play_sound(e, sound_path):
        currentControl = e.control
        currentControl.border = ft.border.all(width=4, color="red")
        currentControl.update()
        currentAudio.src = sound_path
        page.add(currentAudio)

    # Correção da estrutura da compreensão de lista
    galleryElement = ft.Row(
        wrap=True,controls=[
            ft.Container(
                width=132, height=132,bgcolor="#888888", border_radius=12,   on_click=lambda e, sp=p["sound"]: play_sound(e, sp),
                content=ft.Image(src=p["image"], width=72, height=72,expand=True)
            ) for p in items
        ]
    )

    mainColumn = ft.Column(controls=[title, galleryElement])
    page.add(mainColumn)
    page.update()  # Corrigido

ft.app(target=main, assets_dir='Assets')