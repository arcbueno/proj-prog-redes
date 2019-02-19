class File():

    def write(self, text):
        w = open("chat_record.txt", "w")
        w.write(text)
        w.close()

    def get_text(self):
        r = open("chat_record.txt", "r")
        text = r.read()
        r.close()
        return text
    