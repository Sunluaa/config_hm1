import os
import tarfile
import argparse


class ShellEmulator:
    def __init__(self, username, vfs, script):
        self.username = username
        self.hostname = "localhost"
        self.vfs_archive = tarfile.open(vfs, "r")
        self.cwd = "/"

        if script:
            self.run_script(script)

    def run_script(self, script_path):
        with open(script_path, 'r') as script:
            for line in script:
                self.execute_command(line.strip())

    def execute_command(self, command):
        if not command:
            return

        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "ls":
            self.ls(args)
        elif cmd == "cd":
            self.cd(args)
        elif cmd == "exit":
            self.exit_shell()
        elif cmd == "tac":
            self.tac(args)
        elif cmd == "du":
            self.du(args)
        else:
            print(f"{cmd}: command not found")

    def prompt(self):
        return f"{self.username}@{self.hostname}:{self.cwd.rstrip('/')}$ "

    def ls(self, args):
        if not args:
            path = self.cwd
        else:
            target = args[0]
            if target == "..":
                path = os.path.dirname(self.cwd.rstrip("/"))
                if not path:
                    path = "/"
            else:
                path = os.path.join(self.cwd, target)

        path = path.lstrip('/')
        entries = [m for m in self.vfs_archive.getmembers() if m.name.startswith(path)]
        if not entries:
            return

        unique_entries = set()
        for entry in entries:
            relative_path = entry.name[len(path):].strip("/").split("/")[0]
            if relative_path:
                unique_entries.add(relative_path)
        if not unique_entries:
            return

        for entry_name in sorted(unique_entries):
            print(entry_name)

    def run(self):
        try:
            while True:
                command = input(self.prompt())
                self.execute_command(command.strip())
        except KeyboardInterrupt:
            self.exit_shell()


def parse_args():
    parser = argparse.ArgumentParser(description="Эмулятор оболочки UNIX-подобной ОС.")
    parser.add_argument("--username", required=False, help="Имя пользователя для приглашения к вводу.",
                        default="username")
    parser.add_argument("--vfs", required=False, help="Путь к tar-архиву виртуальной файловой системы.",
                        default="vfs.tar")
    parser.add_argument("--script", required=False, help="Путь к стартовому скрипту.", default=None)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    shell = ShellEmulator(args.username, args.vfs, args.script)
    shell.run()
