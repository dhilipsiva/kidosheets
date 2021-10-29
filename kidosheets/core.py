import click


import xlsxwriter


@click.group()
def cli():
    pass


@cli.command()
@click.option("--root_val", default="")
@click.option("--min_rows", default=0, type=int)
@click.option("--max_rows", default=10, type=int)
@click.option("--step_rows", default=1, type=int)
@click.option("--min_cols", default=0, type=int)
@click.option("--max_cols", default=10, type=int)
@click.option("--step_cols", default=1, type=int)
@click.option("--filename", default="kidosheets.xlsx")
def math_square_ruled(
    root_val, min_rows, max_rows, step_rows, min_cols, max_cols, step_cols, filename
):
    workbook = xlsxwriter.Workbook(filename)

    worksheet = workbook.add_worksheet()
    worksheet.set_default_row(44)
    worksheet.set_landscape()
    worksheet.set_paper(9)

    cell_format = workbook.add_format()
    cell_format.set_border(6)
    cell_format.set_font_size(30)
    cell_format.set_align("center")
    cell_format.set_align("vcenter")

    worksheet.write(0, 0, root_val, cell_format)
    for row in range(min_rows, max_rows, step_rows):
        worksheet.write(row + 1, 0, row, cell_format)
    for col in range(min_cols, max_cols, step_cols):
        worksheet.write(0, col + 1, col, cell_format)
    for row in range(min_rows + 1, max_rows + 1, step_rows):
        for col in range(min_cols + 1, max_cols + 1, step_cols):
            worksheet.write(row, col, "", cell_format)

    workbook.close()


if __name__ == "__main__":
    cli()
