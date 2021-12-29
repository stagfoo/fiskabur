import threading
import time
import sys
import random
import webview


class Api:

    def getImage(self):
        file_types = ('Image Files (*.bmp;*.jpg;*.gif)', 'All files (*.*)')
        result = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        response = {
            'message': result
        }
        return response



if __name__ == '__main__':
    api = Api()
    window = webview.create_window('API example', 'www/index.html', js_api=api)
    webview.start()