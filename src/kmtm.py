import click

#v1.0
# @click.command()
# @click.option("--kilos", "-k", type=float, help="Number of kilometers to convert to miles.")
# @click.option("--miles", "-m", type=float, help="Number of miles to convert to kilometers.")
# def cli(kilos, miles):
#     if kilos:
#         converted_value = round(kilos*0.62137,2)
#         click.echo(f"{kilos} kilometers is {converted_value} miles.")
#     elif miles:
#         converted_value = round(miles*1.62137, 2)
#         click.echo(f"{miles} miles is {converted_value} kilometers.")
#     else:
#         click.echo("No kilometers given to convert.")

# v2.0
# @click.command()
# @click.argument("number", nargs=1, type=float, required=True)
# @click.option("--kilos", "-k", default=False, help="Number of kilometers to convert to miles.")
# @click.option("--miles", "-m", default=False, help="Number of miles to convert to kilometers.")
# def cli(number, kilos, miles):
#     if kilos:
#         converted_value = round(number*0.62137,2)
#         click.echo(f"{number} is {converted_value} miles.")
#     elif miles:
#         converted_value = round(number*1.62137, 2)
#         click.echo(f"{number} is {converted_value} kilometers.")
#     else:
#         click.echo("No kilometers given to convert.")


@click.command()
@click.argument("number", nargs=1, type=float, required=True)
@click.option("--kilos", "-k", is_flag=True, help="Number of kilometers to convert to miles.")
@click.option("--miles", "-m", is_flag=True, help="Number of miles to convert to kilometers.")
def cli(number, kilos, miles):
    if kilos is not None:
        converted_value = round(number * 0.62137, 2)
        click.echo(f"{number} kilometers is {converted_value} miles.")
    elif miles is not None:
        converted_value = round(number * 1.60934, 2)
        click.echo(f"{number} miles is {converted_value} kilometers.")
    else:
        click.echo("No conversion selected.")

if __name__ == "__main__":
    cli()