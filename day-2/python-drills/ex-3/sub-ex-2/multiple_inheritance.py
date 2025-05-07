class Book:
    def __init__(self, title):
        self.title = title

class AudioMixin:
    def play_audio(self):
        print(f"Playing audio version of {self.title}")

class AudioBook(Book, AudioMixin):
    pass

ab = AudioBook("1984")
ab.play_audio()
