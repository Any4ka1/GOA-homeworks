from rich import print
from time import sleep

def rock_youre_body():
    lyrics = [
        ("[bold cyan]I wanna da-[/]", 1.2),
        ("[bold cyan]I wanna dance in the light[/]", 1.8),
        ("[bold cyan]I wanna ro-, [/]", 1.2),
        ("[bold cyan]I wanna rock your body[/]", 1.9),
        ("[bold cyan]I wanna go for a ride[/]", 1.9),
        ("[bold cyan]Hop in the music and[/]", 1.5),
        ("[bold cyan]Rock your body[/]", 1.6),
        ("[bold cyan]Rock that body[/]", 1.5),
        ("[bold cyan]come on, come on[/]", 1.1),
        ("[bold cyan](Rock your body)[/]", 1.0),
        ("[bold cyan]Rock that body[/]", 1.4),
        ("[bold cyan]come on, come on[/]", 1.1),
        ("[bold cyan]Rock that body[/]", 1.9),
    ]

    for line, delay in lyrics:
        print(line)
        sleep(delay)

rock_youre_body()