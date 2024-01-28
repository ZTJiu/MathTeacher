from playsound import playsound
from aip import AipSpeech
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Speaker(object):
    def __init__(self):
        APP_ID = os.environ["APP_ID"]
        API_KEY = os.environ["API_KEY"]
        SECRET_KEY = os.environ["SECRET_KEY"]
        DATA_DIR = os.environ["DATA_DIR"]
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        self.voice_cache = {}
        self.data_dir = DATA_DIR
        Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

    def get_voice_file_path(self, text) -> str:
        return os.path.join(self.data_dir, text + '.mp3')

    def gen_voice_mp3(self, text, filename) -> bool:
        result = self.client.synthesis(text, 'zh', 1, {
            'vol': 5,
        })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open(filename, 'wb') as f:
                f.write(result)
            self.voice_cache[text] = filename
            return True
        else:
            print(result)
        return False

    def get_voice_file(self, text) -> str:
        if text not in self.voice_cache:
            filename = self.get_voice_file_path(text)
            if not self.gen_voice_mp3(text, filename):
                raise Exception('生成语音失败')
        return self.voice_cache[text]

    def speak(self, text):
        filename = self.get_voice_file(text)
        playsound(filename)


if __name__ == '__main__':
    speaker = Speaker()
    speaker.speak('你好，我是张天九')
