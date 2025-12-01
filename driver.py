from playwright.sync_api import Page

#class Singleton(type):
#    _instances = {}

#    def __call__(cls, *args, **kwargs):
#        if cls not in cls._instances:
#            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#        return cls._instances[cls]

def singleton(cls):
    _instances = {}

    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    wrapper.reset_instances = lambda: _instances.clear()
    return wrapper

@singleton
class Driver():
    def __init__(self, page: Page, *args, **kwargs):
        self._page = page
        if self._page:
            self._page.set_default_timeout(10000)
            
    def __getattr__(self, name):
        """Делегируем все вызовы к page объекту"""
        if not self._page:
            raise RuntimeError("Page не инициализирован. Сначала установите page через set_page()")
        return getattr(self._page, name)
