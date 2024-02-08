import click

#v1.0
@click.command()
@click.option("--kms", default=1, help="Number of kilometers to convert to miles.")
def km_to_miles(kms):
    miles = round(kms*0.62137,2)
    click.echo(f"{kms} is {miles} miles.")

# # v2.0
# @click.command()
# @click.argument("kms", nargs=1)
# def km_to_miles(kms):
#     miles = round(kms*0.62137,2)
#     click.echo(f"{kms} is {miles} miles.")

if __name__ == "__main__":
    km_to_miles()