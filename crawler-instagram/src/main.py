from config.environments import USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM

from core.driver_manager.driver_manager import DriverManager
from core.builder.instagram_builder import InstagramBuilder

from constants.driver_constants import INSTAGRAM_URL,PATH_DRIVER

def main():
    driver_manager = DriverManager(driver_path=PATH_DRIVER)
    driver_manager.open_website(INSTAGRAM_URL)

    scrapper = (
        InstagramBuilder()
        .set_driver(driver_manager.driver)
        .set_credentials(USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM)
        .build()
    )

    scrapper.login()
    scrapper.handle_notifications()
    scrapper.turn_off_notifications()

    # Continue com o restante do seu código aqui

    # Feche o navegador quando terminar
    driver_manager.close()

if __name__ == "__main__":
    main()