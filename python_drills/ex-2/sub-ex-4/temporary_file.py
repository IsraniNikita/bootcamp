import tempfile

with tempfile.TemporaryFile(mode="w+t") as tf:
    tf.write("Temp data")
    tf.seek(0)
    print("From temp file:", tf.read())
