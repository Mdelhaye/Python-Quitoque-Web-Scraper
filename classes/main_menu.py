from classes import RecipeScraper

class MainMenu:
    menu_structure = {
        "Scraper": {
            "Recipe Cards": {},
            "Recipe": {}
        },
        "Cleaner": {}
    }

    @staticmethod
    def display_menu(menu: dict = menu_structure, path = "MAIN MENU") -> None:
        while True:
            print("\n" + '-' * 100)
            print(f"📌 {path}".center(80, " "))
            print("-" * 100)

            options = list(menu.keys())
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            print("0. Quit" if path == "MAIN MENU" else "O. Back")

            choice = input("\n👉 Choose an option : ")

            if choice == "0":
                if path == "MAIN MENU":
                    print("👋 End of the program.")
                    break

                else:
                    return
            
            try:
                choice = int(choice) - 1
                if 0 <= choice < len(options):
                    selected_option = options[choice]
                    sub_menu = menu[options[choice]]

                    if isinstance(sub_menu, dict) and sub_menu:
                        MainMenu.display_menu(sub_menu, f"{path} > {options[choice]}")
                    else:
                        print(f"\n✅ You have selected: {options[choice]}.")
                        
                        match selected_option:
                            case "Recipe Cards":
                                print("📥 Start recipe card scraping...\n")
                                RecipeScraper.main()
                        # input("🔄 Press Enter to return to the menu…")
                else:
                    print("⚠️ Invalid choice, please try again.")
            except ValueError:
                print("⚠️ Please enter a valid number.")