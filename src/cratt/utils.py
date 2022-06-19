import os


def call(*commands: str | list[str]):
    commands = ' && '.join(commands)  # type: ignore
    os.system(commands)  # type: ignore
