import subprocess

# Команда PowerShell для получения списка локальных пользователей
powershell_command = "Get-WmiObject -Class Win32_UserAccount | Select-Object Name"

# Вызов команды PowerShell и получение вывода
output = subprocess.check_output(["powershell", "-Command", powershell_command], shell=True, text=True)

# Вывод списка локальных пользователей
users = output.strip().split('\n')
for user in users:
    print(user.strip())
