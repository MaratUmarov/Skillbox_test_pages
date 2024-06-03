import socket
import re


def solve_expression(expression):
    # Ищем числа и оператор
    global result
    match = re.match(r'(\d+)\s*([-+*///**%])\s*(\d+)\s*=\s', expression)
    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))

        # Вычисляем результат
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '//':
            result = num1 // num2
        elif operator == '**':
            result = num1 ** num2
        elif operator == '%':
            result = num1 % num2
        return str(result)
    else:
        return None


def main():
    host = 'ppc-ctf.o3.ru'
    port = 7090

    # Подключаемся к серверу
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Принимаем и обрабатываем выражения
        for _ in range(100):
            data = s.recv(1024).decode()
            print("Получено выражение:", data)
            result = solve_expression(data)
            if result:
                print("Решение:", result)
                s.sendall(result.encode())
                # Принимаем ответное сообщение от сервера и выводим его
                response = s.recv(1024).decode()
                print("Ответ от сервера:", response)
            else:
                print("Ошибка при обработке выражения")

        # Получаем флаг
        flag = s.recv(1024).decode()
        print("Флаг:", flag)


if __name__ == "__main__":
    main()
