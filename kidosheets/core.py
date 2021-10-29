import click


import xlsxwriter

KIDO_PAPER_SIZE = 9  # A4
TOTAL_HEIGHT = 480
KIDO_ROW_SIZE = 44  # optimal for 10 row A4
BORDER_STYLE_DOUBLE = 6
BORDER_STYLE_SINGLE = 7
FONT_SIZE_HINT = 7


@click.group()
def cli():
    pass


@cli.command()
@click.option("--sign", default="?")
@click.option("--min_rows", default=0, type=int)
@click.option("--max_rows", default=10, type=int)
@click.option("--step_rows", default=1, type=int)
@click.option("--min_cols", default=0, type=int)
@click.option("--max_cols", default=10, type=int)
@click.option("--step_cols", default=1, type=int)
@click.option("--filename", default="kidosheets.xlsx")
def math_square_ruled(
    sign,
    min_rows,
    max_rows,
    step_rows,
    min_cols,
    max_cols,
    step_cols,
    filename,
):
    workbook = xlsxwriter.Workbook(filename)
    height = TOTAL_HEIGHT / (1 + (max_rows - min_rows / step_rows))

    worksheet = workbook.add_worksheet()
    worksheet.set_paper(KIDO_PAPER_SIZE)

    worksheet.set_default_row(height)
    worksheet.set_landscape()

    cell_format = workbook.add_format()
    cell_format.set_border(BORDER_STYLE_DOUBLE)
    cell_format.set_font_size(height - 2)
    cell_format.set_align("center")
    cell_format.set_align("vcenter")

    worksheet.write(0, 0, sign, cell_format)
    for row in range(min_rows, max_rows, step_rows):
        worksheet.write(row + 1, 0, row, cell_format)
    for col in range(min_cols, max_cols, step_cols):
        worksheet.write(0, col + 1, col, cell_format)

    cell_format = workbook.add_format()
    cell_format.set_border(BORDER_STYLE_SINGLE)
    cell_format.set_font_size(FONT_SIZE_HINT)
    cell_format.set_align("center")
    cell_format.set_align("top")

    for row in range(min_rows, max_rows, step_rows):
        for col in range(min_cols, max_cols, step_cols):
            worksheet.write(row + 1, col + 1, f"{col} {sign} {row}", cell_format)

    workbook.close()


if __name__ == "__main__":
    cli()
