import threading
import time
import sys
import random
import webview


class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def sayHelloTo(self, name):
        response = {
            'message': 'Hello {0}!'.format(name)
        }
        return response
    def getImage(window):
        file_types = ('Image Files (*.bmp;*.jpg;*.gif)', 'All files (*.*)')
        result = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        response = {
            'message': result
        }
        return response

    def error(self):
        raise Exception('This is a Python exception')



if __name__ == '__main__':
    api = Api()
    window = webview.create_window('API example', 'dist/index.html', js_api=api)
    webview.start()