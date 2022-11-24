"""Console script for first_package."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("first_package")
    click.echo("=" * len("first_package"))
    click.echo("第一个包")


if __name__ == "__main__":
    main()  # pragma: no cover
