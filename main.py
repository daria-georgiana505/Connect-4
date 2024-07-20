from repository.tests_repo import test_all_fn_repo
from services.tests_services import test_all_fn_services
from ui.console import Console
from ui.gui import GUI

if __name__ == '__main__':
    # game = Console()
    game = GUI()

    test_all_fn_repo()
    test_all_fn_services()

    game.start_game()