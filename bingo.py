import random
from string import Template

NUMBER_OF_BOARDS = 32

with open("templates/pages.html", "r") as f:
    pages_template = f.read()

with open("templates/bingo_board.html", "r") as f:
    bingo_board_html_template = f.read()

pages = Template(pages_template)
bingo_board_template = Template(bingo_board_html_template)

with open("things.txt", "r") as f:
    things = f.read().splitlines()

random_things = []
bingo_board = {"board": ""}
for output in range(NUMBER_OF_BOARDS):
    random.shuffle(things)
    random_things.append(things[:9])

for page, bingo_things in enumerate(random_things):
    bingo_cells = {"page": page}
    if page % 2:
        bingo_cells["pagebreak"] = "pagebreak"
    else:
        bingo_cells["pagebreak"] = "dontbreak"
    for i, thing in enumerate(bingo_things):
        print(thing)
        bingo_cells[f"bingo{i}"] = thing

    bingo_board["board"] += bingo_board_template.safe_substitute(bingo_cells)

with open(f"htmls/bingo_game.html", "w") as output_file:
    output_file.write(pages.safe_substitute(bingo_board))
