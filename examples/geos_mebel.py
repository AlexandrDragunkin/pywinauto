# -*- coding: utf-8 -*-
from pywinauto.application import Application
import pywinauto
from pywinauto.timings import Timings
import time

# Таймаут ожидания запуска приложения
Timings.Fast()
Timings.window_find_timeout = 20

# Запускаем к3 - мебель из папки ARL7
app = Application(backend="win32").start(r'C:\ARL7\Bin\Mebel.exe')

# Цепляемся к реестру заказов
reestr_z =app.window(title_re='.*Реестр заказов')

# Вызываем справку
reestr_z["Справка"].click()

# Цепляемся к справке
hw = app.window(title_re = '.*К3-Мебель')

# Ждем 3 секунды
time.sleep(3)

# Выводим список контролов до 3 - го уровня на экран
hw.print_control_identifiers(depth=3, filename=None)

# Закрываем окно Справка при помощи эмуляции  Alt+F4
pywinauto.keyboard.SendKeys('%{F4}') # закрыть активное окно Alt+F4

# Жмем на кнопку Открыть в Реестре заказов (разные варианты)
# reestr_z.child_window(title="Открыть", class_name="WindowsForms10.BUTTON.app.0.1fed012_r71_ad1").click()
reestr_z['Окрыть'].click()

# Цепляемся к главному окну приложения
k_ = app.window(title_re = '.*K3-Mebel.*')

# Выводим список контролов до 3 - го уровня в файл
k_.print_control_identifiers(depth=3, filename= r'c:\temp\k3_control.txt')

# Ждем 3 секунды
time.sleep(3)

# Закрываем K3
# k_.menu_select("Файл->Выход")
k_.Close()



