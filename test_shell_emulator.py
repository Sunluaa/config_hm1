import unittest
from io import StringIO
import sys
from shell_emulator import ShellEmulator


class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        """Подготовка перед каждым тестом"""
        self.emulator = ShellEmulator(username="testuser", vfs="tar.tar", script=None)

    def test_ls_root(self):
        """Тест команды ls в корневой директории"""
        result = self._capture_output(self.emulator.ls, [])
        self.assertIn("file1.txt", result)
        self.assertIn("dir1", result)
        self.assertIn("file2.txt", result)

    def test_ls_in_directory(self):
        """Тест команды ls в поддиректории dir1"""
        self.emulator.cd(["dir1"])
        result = self._capture_output(self.emulator.ls, [])
        self.assertIn("file3.txt", result)
        self.assertIn("file4.txt", result)
        self.assertIn("dir3", result)
        self.assertIn("dirinfinity", result)

    def test_cd_back_to_root(self):
        """Тест команды cd для возвращения в корень"""
        self.emulator.cd(["dir1"])
        self.emulator.cd([".."])
        self.assertEqual(self.emulator.cwd, "/")

    def test_tac_file1(self):
        """Тест команды tac для file1.txt"""
        result = self._capture_output(self.emulator.tac, ["file1.txt"])
        self.assertEqual(result.strip(), "1\n2\n3")  # Проверка содержимого в обратном порядке

    def test_tac_file2(self):
        """Тест команды tac для file2.txt"""
        result = self._capture_output(self.emulator.tac, ["file2.txt"])
        self.assertEqual(result.strip(), "3\n2\n1")  # Проверка содержимого в обратном порядке

    def test_tac_empty_file(self):
        """Тест команды tac для пустого файла"""
        self.emulator.cd(["dir1"])
        result = self._capture_output(self.emulator.tac, ["file3.txt"])
        self.assertEqual(result.strip(), "")  # Пустой файл

    def test_cd_nonexistent_directory(self):
        """Тест ошибки при переходе в несуществующую директорию"""
        result = self._capture_output(self.emulator.cd, ["nonexistent"])
        self.assertIn("No such file or directory", result)

    def test_exit(self):
        """Тест команды exit"""
        with self.assertRaises(SystemExit):  # Ожидаем завершения программы
            self.emulator.exit_shell()

    def _capture_output(self, func, args):
        """Вспомогательный метод для захвата вывода команды"""
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            func(args)
            return out.getvalue()
        finally:
            sys.stdout = saved_stdout


if __name__ == "__main__":
    unittest.main()
