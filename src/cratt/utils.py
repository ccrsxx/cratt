import os


def call(*commands: list[str]):
    commands = ' && '.join(commands)  # type: ignore
    os.system(commands)  # type: ignore
