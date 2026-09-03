import subprocess
import sys

def run_command(cmd):
    """Запускает команду в оболочке, возвращает (stdout, stderr, код_возврата)."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=False)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), -1

def main():
    print("=== Git push automation ===")

    # 1. Проверяем, что мы в Git-репозитории
    _, stderr, ret = run_command("git status")
    if ret != 0:
        print("Ошибка: текущая папка не является Git-репозиторием или Git не установлен.")
        sys.exit(1)

    # 2. Запрашиваем сообщение коммита
    msg = input("Введите сообщение для коммита: ").strip()
    if not msg:
        print("Ошибка: сообщение не может быть пустым.")
        sys.exit(1)

    # 3. Добавляем все изменения
    print("Добавление изменений...")
    _, stderr, ret = run_command("git add .")
    if ret != 0:
        print(f"Ошибка при git add: {stderr}")
        sys.exit(1)

    # 4. Создаём коммит
    print("Создание коммита...")
    _, stderr, ret = run_command(f'git commit -m "{msg}"')
    if ret != 0:
        # Если изменений нет, просто выходим
        if "nothing to commit" in stderr:
            print("Нет изменений для коммита. Пуш пропущен.")
            sys.exit(0)
        else:
            print(f"Ошибка при git commit: {stderr}")
            sys.exit(1)

    # 5. Пушим
    print("Отправка изменений на удалённый репозиторий...")
    stdout, stderr, ret = run_command("git push")
    if ret != 0:
        print(f"Ошибка при git push: {stderr}")
        # Подсказка, если не настроен upstream
        if "no upstream branch" in stderr:
            print("Возможно, ветка не привязана к удалённой. Попробуйте вручную: git push -u origin <branch>")
        sys.exit(1)
    else:
        print("Пуш успешно выполнен!")
        if stdout:
            print(stdout)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nОперация прервана пользователем.")
        sys.exit(1)