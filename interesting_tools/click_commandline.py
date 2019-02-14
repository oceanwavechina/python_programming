import click
import time

"""
    document:
        https://click.palletsprojects.com/en/7.x/
"""

@click.group()
def cli():
    pass

@click.command()
@click.option('--ip', default='127.0.0.1', help='the ip of database')
@click.argument('schema')
def initdb(ip, schema):
    click.echo("Initialized the databases:%s from:%s" % (ip, schema))

@click.command()
@click.confirmation_option(prompt=click.style("Are you sure?",fg='red', bold=True, blink=True))
def dropdb():
    click.echo("Dropped Database")
    
    # 这个功能是根据for循环测次数来实现的，
    # 但是在with里边不能有print之类的操作，否则会影响进度条的输出
    with click.progressbar([1,2,3,4,5],label="Dropping all table:",length=5) as tables:
        for table in tables:
            time.sleep(1)

@click.command()
@click.argument('f', type=click.Path(exists=True, file_okay=False))
def touch(f):
    # 检查文件存在不存在, 以及判断文件类型
    click.echo("create a new file:%s"%f)

@click.command()
@click.option('--count', type=click.IntRange(0, 20))
@click.option('--type', type=click.Choice(['type1', 'type2']))
def setparam(count, type):
    # 限制范围
    click.echo("set count: %d, type:%s" % (count, type))

@click.command()
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def encrypt(password):
    click.echo('Encrypting password to %s' % password.encode('utf8'))

cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(encrypt)
cli.add_command(setparam)
cli.add_command(touch)

if __name__ == "__main__":
    cli()