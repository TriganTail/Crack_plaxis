import ctypes
import os
import traceback

import ctypes
import os
import sys



class CrackPlaxis():
    def start():
        try:
            #ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
            #                        __file__, None, 1)

            with open(host_path) as file:
                array = [row.strip() for row in file]

            check = CrackPlaxis.test(array)

            if check == True:
                array = CrackPlaxis.recreate(array)
                _Array = CrackPlaxis.inserts(array)
            else:
                _Array = CrackPlaxis.inserts(array)

            a = input("""
            Для того, что-бы Crack сработал, вам необходимо перезагрузить компьютер. Сделать это сейчаc? (Д/н) (Y/n):
            """)
            if a == "Y" or a == "y" or a == "Д" or a == "д":
                os.system('shutdown /r /t 1')
            else:
                exit(1)

            with open(host_path, 'w') as file:
                # Записываем каждую строку из списка в файл
                for line in _Array:
                    file.write(line + "\n")
        except Exception as e:
            print("Error",e)
            print("Вы не активировали режим администратора? Запустите программу сначала и нажмите на подтверждение!")
            exit(1)


    def test(array):
        for i in range(len(array)):
            if array[i] == "127.0.0.1 13.68.104.252" or array[i] == "127.0.0.1 40.115.6.34" or array[i] == "127.0.0.1 52.29.92.197" or array[i] == "127.0.0.1 11.00.13.09" or array[i] == "127.0.0.1 11.00.02.20":

                return True

    def recreate(array):
        a = input("""
        У вас уже был ранее запущена данная программа, вы хотите снова поправить код? (Д/н) или (Y/n) : 
        """)
        if a == "Y" or a == "y" or a == "Д" or a == "д":
            array = CrackPlaxis.recreate_join(array)
            return array
        else:
            exit(1)
    def recreate_join(array):
            clear_array = []
            for i_arr in range(len(array)):
                for i_dat in range(len(data)):
                    if array[i_arr] == data[i_dat]:
                        array[i_arr] = []

            for i_arr in range(len(array)):
                if array[i_arr] != []:
                    clear_array.append(array[i_arr])
            if clear_array != []:
                array = clear_array

            return array

    def inserts(array):
        for i in range(len(data)):
            array.append(data[i])
        return array

host_path = "C:\Windows\System32\drivers\etc\hosts"
data = ["127.0.0.1 13.68.104.252", "127.0.0.1 40.115.6.34", "127.0.0.1 52.29.92.197", "127.0.0.1 11.00.13.09",
                "127.0.0.1 11.00.02.20"]
CrackPlaxis.start()