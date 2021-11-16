import click
import xlsxwriter

from tamil import mei, uyir, uyirmei

PAPER_SIZE = 9  # A4
TOTAL_HEIGHT = 480
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
    worksheet.set_paper(PAPER_SIZE)

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


@cli.command()
@click.option("--filename", default="kidosheets-tamil.xlsx")
@click.option("--hint/--no-hint", default=True)
def tamil_matrix(filename, hint):
    sign = "+"
    height = TOTAL_HEIGHT / (1 + len(uyir))
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    worksheet.set_paper(PAPER_SIZE)
    worksheet.set_default_row(height)
    worksheet.set_landscape()

    cell_format = workbook.add_format()
    cell_format.set_border(BORDER_STYLE_DOUBLE)
    cell_format.set_font_size(height - 2)
    cell_format.set_align("center")
    cell_format.set_align("vcenter")

    worksheet.write(0, 0, sign, cell_format)
    for row, letter in enumerate(mei):
        worksheet.write(0, row + 1, letter, cell_format)
    for col, letter in enumerate(uyir):
        worksheet.write(col + 1, 0, letter, cell_format)

    cell_format = workbook.add_format()
    cell_format.set_border(BORDER_STYLE_SINGLE)
    if hint:
        cell_format.set_font_size((height - 10) / 2)
    else:
        cell_format.set_font_size(height - 15)
    cell_format.set_align("center")
    cell_format.set_align("top")

    for row, mei_letter in enumerate(mei):
        for col, uyir_letter in enumerate(uyir):
            content = uyirmei[row][col]
            if hint:
                content = f"{mei_letter} {sign} {uyir_letter}\n{content}"
            worksheet.write(col + 1, row + 1, content, cell_format)

    workbook.close()


if __name__ == "__main__":
    cli()
