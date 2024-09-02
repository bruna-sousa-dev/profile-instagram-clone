import flet as ft
import math

class App:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = 'Intagram Profile'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor = ft.colors.WHITE
        # self.page.scroll = ft.ScrollMode.HIDDEN
        self.page.padding = ft.padding.all(0)
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.main()

    def main(self):
        
        def toggle_follow(e):
            if e.control.content.value == 'Seguir':
                e.control.content.value = 'Seguindo'
                e.control.bgcolor = ft.colors.GREY_300
                e.control.content.color = ft.colors.BLACK
                you_follow.text = 'você '
                you_follow_e.text = 'e '
            else:
                e.control.content.value = 'Seguir'
                e.control.bgcolor = ft.colors.BLUE
                e.control.content.color = ft.colors.WHITE
                you_follow.text = ''
                you_follow_e.text = ''
            e.control.update()
            you_follow.update()
            you_follow_e.update()
            
        header = ft.Container(
            content = ft.ResponsiveRow(
                controls = [
                    ft.Container(
                        col = {'xs': 12, 'sm': 4},
                        padding = ft.padding.all(10),
                        bgcolor = ft.colors.BLACK,
                        content = ft.Image(src = 'images/perfil.png'),
                        shape = ft.BoxShape.CIRCLE,
                        height = 200,
                    ),
                    ft.Container(
                        col = {'xs': 12, 'sm': 8},
                        padding = ft.padding.all(10),
                        content = ft.Column(
                            controls = [
                                ft.Row(
                                    controls = [
                                        ft.Text(value = 'eng.desenvolvedor', weight = ft.FontWeight.BOLD, color = ft.colors.BLACK),
                                        ft.Icon(name = ft.icons.VERIFIED, size = 16, color = ft.colors.BLUE),
                                        ft.Container(expand = True),
                                        ft.PopupMenuButton(rotate = math.radians(90), items = [ft.PopupMenuItem(text = 'Item 1'), ft.PopupMenuItem(text = 'Item 2')])
                                    ],
                                ),
                                ft.ResponsiveRow(
                                    controls = [
                                        ft.Container(
                                            col = 4,
                                            bgcolor = ft.colors.BLUE_500,
                                            content = ft.Text(
                                                value = 'Seguir',
                                                weight = ft.FontWeight.BOLD,
                                                color = ft.colors.WHITE,
                                                max_lines = 1,
                                                overflow = ft.TextOverflow.ELLIPSIS
                                            ),
                                            border_radius = ft.border_radius.all(10),
                                            padding = ft.padding.symmetric(vertical = 5, horizontal = 10),
                                            alignment = ft.alignment.center,
                                            on_click = toggle_follow
                                        ),
                                        ft.Container(
                                            col = 6,
                                            bgcolor = ft.colors.GREY_300,
                                            content = ft.Text(
                                                value = 'Enviar mensagem',
                                                weight = ft.FontWeight.BOLD,
                                                color = ft.colors.BLACK,
                                                max_lines = 1,
                                                overflow = ft.TextOverflow.ELLIPSIS
                                            ),
                                            border_radius = ft.border_radius.all(10),
                                            padding = ft.padding.symmetric(vertical = 5, horizontal = 10),
                                            alignment = ft.alignment.center
                                        ),

                                    ],
                                ),
                                ft.ResponsiveRow(
                                    controls = [
                                        ft.Row(
                                            col = {'xs': 12, 'sm': 4},
                                            spacing = 5,
                                            controls = [
                                                num_publications := ft.Text(value = '139', weight = ft.FontWeight.BOLD, size = 12, color = ft.colors.BLACK),
                                                ft.Text(value = 'publicações', weight = ft.FontWeight.NORMAL, size = 12, color = ft.colors.BLACK),
                                            ],
                                        ),
                                        ft.Row(
                                            col = {'xs': 12, 'sm': 4},
                                            spacing = 4,
                                            controls = [
                                                num_followers := ft.Text(value = '100 mil', weight = ft.FontWeight.BOLD, size = 12, color = ft.colors.BLACK),
                                                ft.Text(value = 'seguidores', weight = ft.FontWeight.NORMAL, size = 12, color = ft.colors.BLACK),
                                            ],
                                        ),
                                        ft.Row(
                                            col = {'xs': 12, 'sm': 4},
                                            spacing = 5,
                                            controls = [
                                                num_following := ft.Text(value = '133', weight = ft.FontWeight.BOLD, size = 12, color = ft.colors.BLACK),
                                                ft.Text(value = 'seguindo', weight = ft.FontWeight.NORMAL, size = 12, color = ft.colors.BLACK),
                                            ],
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    content = ft.Text(
                                        value = 'Engenheiro Desenvolvedor',
                                        weight = ft.FontWeight.BOLD
                                    )
                                ),
                                ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            ft.Text(value = '🎯 Desenvolvedor Full Stack\n🎓 Engenheiro de Software\n🚀 Especialista em Ciência de Dados e Inteligência Artificial\n😎 PYTHON + HTML + CSS + JS + PHP + JAVA\n👇👇👇', size = 12, color = ft.colors.BLACK),
                                            ft.Row(
                                                spacing = 0,
                                                controls = [
                                                    ft.Icon(ft.icons.LINK),
                                                    ft.TextButton(
                                                        text = 'linktr.ee/eng.bruna.sousa', 
                                                        style = ft.ButtonStyle(color = ft.colors.BLUE_500)
                                                    )
                                                ],
                                            )
                                        ],
                                    ),
                                ),
                                ft.Container(
                                    content = ft.Text(
                                        spans = [
                                            ft.TextSpan(text = 'Seguido por ', style = ft.TextStyle(size = 12, color = ft.colors.BLACK)),
                                            you_follow := ft.TextSpan(text = '', style = ft.TextStyle(size = 12, weight = ft.FontWeight.BOLD, color = ft.colors.BLACK)),
                                            you_follow_e := ft.TextSpan(text = '', style = ft.TextStyle(size = 12, color = ft.colors.BLACK)),
                                            ft.TextSpan(text = '100 outras pessoas', style = ft.TextStyle(size = 12, color = ft.colors.BLACK)),
                                        ],
                                    )
                                ),   
                            ],
                        )
                    ),                
                ],
            ),
        )

        stories = ft.Container(
            margin = ft.margin.only(bottom = 20, top = 10),
            content = ft.Row(
                scroll = ft.ScrollMode.HIDDEN,
                controls = [
                    ft.CircleAvatar(
                        foreground_image_url = f'https://picsum.photos/200?{num}',
                        radius = 40
                    ) for num in range(500, 519)
                ],
            ),
        )

        grid_posts = ft.GridView(
            # expand = True,
            child_aspect_ratio = 1,
            runs_count = 3,
            spacing = 5,
            run_spacing = 5,
            controls = [
                ft.Image(
                    src = f'https://picsum.photos/200?{num}',
                    fit = ft.ImageFit.COVER,
                    repeat = ft.ImageRepeat.NO_REPEAT
                ) for num in range(100)
            ],
        )

        grid_reels = ft.GridView(
            child_aspect_ratio = 9/16,
            runs_count = 3,
            spacing = 5,
            run_spacing = 5,
            controls = [
                ft.Image(
                    src = f'https://picsum.photos/200?{num}',
                    fit = ft.ImageFit.COVER,
                    repeat = ft.ImageRepeat.NO_REPEAT
                ) for num in range(101, 200)
            ],
        )

        grid_save = ft.GridView(
            child_aspect_ratio = 1,
            runs_count = 3,
            spacing = 5,
            run_spacing = 5,
            controls = [
                ft.Image(
                    src = f'https://picsum.photos/200?{num}',
                    fit = ft.ImageFit.COVER,
                    repeat = ft.ImageRepeat.NO_REPEAT
                ) for num in range(201, 300)
            ],
        )
        
        posts = ft.Tabs(
            selected_index = 0,
            animation_duration = 300,
            label_color = ft.colors.BLACK,
            unselected_label_color = ft.colors.GREY_500,
            divider_color = ft.colors.TRANSPARENT,
            indicator_color = ft.colors.TRANSPARENT,
            scrollable = False,
            tabs = [
                ft.Tab(text = 'Publicações', icon = ft.icons.GRID_ON, content = grid_posts),
                ft.Tab(text = 'Reels', icon = ft.icons.VIDEO_COLLECTION_OUTLINED, content = grid_reels),
                ft.Tab(text = 'Salvos', icon = ft.icons.BOOKMARK_BORDER, content = grid_save),
            ],
        )
                
        layout = ft.Container(
            padding = ft.padding.all(10),
            expand = True,
            content = ft.Column(
                scroll = ft.ScrollMode.HIDDEN, 
                spacing = 0,
                controls = [
                    header,
                    stories,
                    ft.Divider(color = ft.colors.GREY,height = 1),
                    posts
                ],
            )
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target = App, assets_dir = 'assets')
