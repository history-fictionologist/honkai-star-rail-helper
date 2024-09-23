# honkai-star-rail-helper

`honkai-star-rail-helper` — это утилита, предназначенная для управления и обработки данных персонажей, навыков и рекомендаций по реликвиям для видеоигры [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail). Она читает входные файлы, обрабатывает различные атрибуты, такие как информация о персонажах и наборы навыков, и выводит результаты в организованном формате. Входные данные берутся из официальных обновлений в репозитории [StarRailData](https://github.com/Dimbreath/StarRailData/t...

## Последняя таблица персонажей
<!-- CHARACTER_TABLE_START -->
| DAMAGE_TYPE | RARITY | DESTRUCTION               | THE_HUNT  | ERUDITION | HARMONY   | NIHILITY                  | PRESERVATION       | ABUNDANCE  |
|-------------|--------|---------------------------|-----------|-----------|-----------|---------------------------|--------------------|------------|
| PHYSICAL    | 5      | clara\|player\|yunli      | boothill  | argenti   | robin     |                           |                    |            |
| PHYSICAL    | 4      |                           | sushang   |           | hanya     | luka                      |                    | natasha    |
| FIRE        | 5      | sam                       | topaz     | himeko    |           | jiaoqiu                   | player2            | lingsha    |
| FIRE        | 4      | hook                      |           |           | asta      | guinaifen                 |                    | gallagher  |
| ICE         | 5      | jingliu                   | yanqing   |           | ruanmei   |                           | gepard             |            |
| ICE         | 4      | misha                     |           | herta     |           | pela                      | mar7th             |            |
| LIGHTENING  | 5      |                           |           | jingyuan  |           | acheron\|kafka            |                    | bailu      |
| LIGHTENING  | 4      | arlan                     | moze      | serval    | tingyun   |                           |                    |            |
| WIND        | 5      | blade                     | feixiao   |           | bronya    | blackswann                |                    | huohuo     |
| WIND        | 4      |                           | danheng   |           |           | sampo                     |                    |            |
| QUANTUM     | 5      |                           | seele     | jade      | sparkle   | silverwolf                | fuxuan             |            |
| QUANTUM     | 4      | xueyi                     |           | qingque   |           |                           |                    | lynx       |
| IMAGINARY   | 5      | danhengil                 | drratio   |           | player3   | welt                      | aventurine         | luocha     |
| IMAGINARY   | 4      |                           | mar7th2   |           | yukong    |                           |                    |            |
<!-- CHARACTER_TABLE_END -->

## Основные функции
- Автоматически загружает данные персонажей, CV, наборы навыков и рекомендации по реликвиям.
- Обрабатывает и организует данные в версиях для входных/выходных директорий.
- Конфигурация номеров версий через командную строку для каждого нового обновления.

## Требования

Убедитесь, что у вас есть следующее:
- **Python 3.8+** (проверьте с помощью `python3 --version`).
- Требуемые пакеты Python перечислены в `requirements.txt`.

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(Опционально) Создайте и активируйте виртуальную среду:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # В Windows: venv\Scriptsctivate
   ```

3. **Установите зависимости (дополнительные зависимости пока не требуются):**
   ```bash
   # На данный момент установка зависимостей не требуется, но если потребуется в будущем:
   # pip install -r requirements.txt
   ```

## Использование

### Запуск инструмента
   Перейдите в директорию `src/` и запустите основной скрипт с нужным номером версии:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - Замените `<version_number>` на текущую версию (например, `2.5`).
   - Если вы хотите пропустить загрузку файлов, добавьте флаг `--skip-download`.

   Входные файлы будут загружены в папку `input/{version}`, а вывод будет сохранен в папке `output/{version}`.

### Примеры использования

- Чтобы запустить скрипт с версией `2.5` и загрузить файлы:
  ```bash
  python3 main.py --version 2.5
  ```

- Чтобы запустить скрипт с версией `2.5` и пропустить загрузку файлов:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- Чтобы запустить скрипт с версией 2.5 и загрузить файлы для определенных языков (например, EN и JP):
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## Вклад

Мы приветствуем вклад! Вы можете:
- Отправить pull request для новых функций или исправления ошибок.
- Сообщить о проблемах через трекер проблем.
- Убедитесь, что все вклады включают тесты и соответствующую документацию.

## Лицензия

Этот проект лицензирован на условиях лицензии MIT. Дополнительную информацию смотрите в файле [LICENSE](LICENSE).
