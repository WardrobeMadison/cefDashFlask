from cefpython3 import cefpython as cef
import platform
import sys

switches = {
    "disable-gpu": "",
}

settings = {
    "context_menu": {"nagivation": True}
}


def run_cef_gui(url_target, title):
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize(switches=switches, settings=settings)
    cef.CreateBrowserSync(url=url_target,
                          window_title=title)
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    print("[cef_boot.py] CEF Python {ver}".format(ver=cef.__version__))
    print("[cef_boot.py] Python {ver} {arch}".format(
          ver=platform.python_version(), arch=platform.architecture()[0]))
    assert cef.__version__ >= "55.3", "CEF Python v55.3+ required to run this"


if __name__ == '__main__':
    run_cef_gui("localhost:5000", 'Window Title')