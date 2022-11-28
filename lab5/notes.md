• Что происходит при прерывании скрипта `text-trap.sh`? Объясните, почему.
```sh
При нажатии на комбинацию клавиш CTRL+C во время выполнения сработает реакция по умолчанию на сигнал SIGINT (Signal Interrupt), 
установленная командой trap, и программа аварийно завершится.
```
• Напишите, по какой причине выводы команды `ls -l /proc/self` и `ls -l /proc/$$` отличаются?
```sh
 Содержимое ссылки (файла /proc/self) меняется в зависимости от того, кто к ней обращается. 
 Вывод команды `ls -l /proc/self` соответствует PID процесса ls.
 $$ — это специальная переменная BASH, определяющая PID текущего процесса-сценария.
 Вывод команды `ls -l /proc/$$` относитя к PID оболочки bash.
```
• Напишите, какие дескрипторы в выводе команды `ls -l /proc/self/fd` отвечают за stdin, stdout, stderr.
```sh
 0 — stdin
 1 — stdout
 2 — stderr
```
• Что происходит с дескрипторами при перенаправлении потоков stdout и stderr в файлы при выполнении команды `ls -l /proc/self/fd > /tmp/ls.out 2> /tmp/ls.err`?
```sh
 Происходит переназначение файловых дескрипторов, связанных с потоками stdout и stderr.
 Bash перенаправляет стандартные потоки stdout и stderr в файлы /tmp/ls.out и /tmp/ls.err соответственно.
```
• Запишите эту же команду, добавив к ней перенаправление потока stdin. Что изменилось?
```sh
 ls -l /proc/self/fd < /tmp/ls.in > /tmp/ls.out 2> /tmp/ls.err
 
 Если входного файла нет, то будет сообщение об ошибке, записанное в файл /tmp/ls.err. 
 Иначе в файл /tmp/ls.out записывается вывод команды `ls -l /proc/self/fd`.
```
• Какой эффект наблюдается при выполнении команды `exec ps -l`?
```sh
 Закрывается текущее окно терминала, т.к. текущий процесс оболочки bash заменяется процессом команды `ps -l`
```
• Что означает `pos` при выводе содержимого файла `/proc/$$/fdinfo/3`?
```sh
 Текущую позицию указателя чтения-записи в открытом файле процесса оболочки Bash.
```
• Существует ли возможность читать содержимое файла `test.out` даже после его удаления? Почему так происходит?
```sh
 Удаление файла —  это удаление указателя на его inode и удаление содержимого файла, если не остается ни одной жесткой ссылки на него.
 Если обращение к файлу test.out осуществляется через дескриптор(он указывает на inode файла, который существует после удаления данного файла), вывод команды `cat <&4` должен быть пустым.
 При обращении к файлу test.out по имени выводится сообщение об ошибке(нет такого файла).
```