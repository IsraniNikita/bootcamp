import tempfile

with tempfile.NamedTemporaryFile(mode='w+', delete=True) as tmp:
    tmp.write("some temp data")
    tmp.seek(0)
    print("Temp file content:", tmp.read())
