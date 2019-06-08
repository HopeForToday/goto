from os.path import expanduser
from subprocess import PIPE, Popen, run

from click import echo, group, pass_context

import commentjson as json

DATA_DIR = expanduser("~/.local/share/goto")
CONFIG_DIR = expanduser("~/.config/goto")
FILE_LIST_PATH = f"{DATA_DIR}/files"
IGNORE_FILE_PATH = f"{DATA_DIR}/ignore"
CONFIG_FILE_PATH = f"{CONFIG_DIR}/config.json"


@group(invoke_without_command=True)
@pass_context
def cli(ctx):
    if ctx.invoked_subcommand:
        return

    with open(FILE_LIST_PATH, "rb") as f:
        file_list = f.read()

    p = Popen("fzf", stdout=PIPE, stdin=PIPE)
    stdout, _ = p.communicate(file_list)
    echo(stdout.decode("utf8"))


@cli.command()
def sync():
    with open(CONFIG_FILE_PATH) as f:
        config_str = f.read()

    config = json.loads(config_str)
    sources = config.get("sources")
    if not sources:
        print("Please configure `sources`")
        return

    p = run(
        ["fd", "-aH", "--ignore-file", IGNORE_FILE_PATH, ".", *sources],
        capture_output=True,
        check=True,
    )
    with open(FILE_LIST_PATH, "w") as f:
        f.write(p.stdout.decode("utf8"))

    echo("Sync succeed")


if __name__ == "__main__":
    cli()
