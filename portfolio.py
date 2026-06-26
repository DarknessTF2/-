from content import PORTFOLIO_DATA


class Portfolio:
    """Stores and prints portfolio sections."""

    def __init__(self, data):
        self.data = data

    def get_section_keys(self):
        return list(self.data.keys())

    def print_section(self, key):
        section = self.data[key]
        print_frame(section["title"])
        for item in section["items"]:
            print(f"  - {item}")
        print()

    def print_all_sections(self):
        for key in self.get_section_keys():
            self.print_section(key)


class PortfolioApp:
    """Console menu for the portfolio project."""

    def __init__(self):
        self.portfolio = Portfolio(PORTFOLIO_DATA)
        self.menu_items = self._build_menu_items()

    def _build_menu_items(self):
        items = []
        for key in self.portfolio.get_section_keys():
            title = self.portfolio.data[key]["title"]
            items.append((key, title))
        return items

    def run(self):
        while True:
            self._print_menu()
            choice = input("Выбери раздел: ").strip()

            if choice == "0":
                print("Спасибо за просмотр портфолио!")
                break

            if choice == "9":
                self.portfolio.print_all_sections()
                pause()
                continue

            if not choice.isdigit():
                print("Ошибка: введи номер пункта меню.")
                pause()
                continue

            menu_index = int(choice) - 1
            if 0 <= menu_index < len(self.menu_items):
                section_key = self.menu_items[menu_index][0]
                self.portfolio.print_section(section_key)
            else:
                print("Такого пункта нет. Попробуй еще раз.")

            pause()

    def _print_menu(self):
        print_frame("Портфолио «Обо мне»")
        for number, (_, title) in enumerate(self.menu_items, start=1):
            print(f"{number}. {title}")
        print("9. Показать все разделы")
        print("0. Выход")
        print("-" * 44)


def print_frame(title):
    line = "=" * 44
    print(line)
    print(title.center(44))
    print(line)


def pause():
    input("Нажми Enter, чтобы продолжить...")


if __name__ == "__main__":
    PortfolioApp().run()
