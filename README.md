# config_hm1
Документация к эмулятору

Эмулятор командной строки (Shell Emulator) написан на Python и имитирует работу стандартной оболочки Unix-подобных операционных систем. Эмулятор поддерживает базовые команды и позволяет работать с виртуальной файловой системой, хранящейся в архиве формата tar. Команды, поддерживаемые эмулятором: ls, cd, tac, du, exit.

Программа запускается из реальной командной строки, принимает аргументы для указания пользователя, компьютера, пути к архиву с файловой системой и стартовому скрипту (необязательный параметр), который автоматически выполняется при запуске. По умолчанию в качестве имени пользователя и компьютера используются username и hostname соответственно, а путь к файловой системе - tar.tar.

Поддерживаемые команды:

ls [directory] - Выводит содержимое текущей директории. Если папка пуста — вывод будет пустым. Можно дописать путь к папке, в таком случае выведет содержимое введенной директории.

cd [directory] - Изменяет текущую директорию. Поддерживается относительная и абсолютная навигация.

tac [file name] - Выводит информацию полученную из файла, но в обратном порядке относительно cat

du [file or directory name] - стандартная Unix-программа для оценки занимаемого файлового пространства. Появилась в первой версии AT&T UNIX. По умолчанию показывает размер файлового пространства, занимаемого каждым файлом и каталогом в текущем каталоге. Чтобы указать другой путь для работы, необходимо поместить его первым параметром. 

exit - Завершает работу эмулятора.

Запуск эмулятора:

Запустить эмулятор можно с помощью команды:

python shell_emulator.py --username <имя пользователя> --vfs <путь к архиву> --script [<путь к стартовому скрипту>]

Пример работы команд:

Переход в директорию и вывод её содержимого:

![изображение](https://github.com/user-attachments/assets/d1941078-6d82-47f8-b1ec-434c249c40ce)

Выполнение команд из варианта:

![изображение](https://github.com/user-attachments/assets/aeb2d920-2966-4496-80a0-ec8849c8cedc)

Результаты прогона тестов:

Для всех команд эмулятора написаны тесты с использованием библиотеки unittest. Для запуска тестов выполняется команда:

python -m unittest test_shell_emulator.py

Скриншот успешного выполнения тестов:

![изображение](https://github.com/user-attachments/assets/9c71c781-a1ba-46ad-955e-2fb37eec1e73)


Дополнительно

Эмулятор поддерживает несколько основных команд, используемые в Unix-подобных системах. Все функции покрыты тестами, обеспечивающими стабильность работы программы.
