import click


def title(fun):
    def wrapper(*args, **kwargs):
        fn_name = fun.__name__
        fn_name = fn_name.replace("_", " ").upper()

        click.echo("*" * 50)
        click.echo(fn_name.center(50))
        click.echo("*" * 50)

        return fun(*args, **kwargs)

    return wrapper
