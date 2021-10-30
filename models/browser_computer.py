class BrowserComputer:
    """
    Браузеры и компютеры
    для реализации связи многие-ко-многим
    """

    def __init__(self, computer_id, browser_id):
        self.browser_id = browser_id
        self.computer_id = computer_id