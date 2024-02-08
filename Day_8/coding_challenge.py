
class exception(Exception):
    def __init__(self, msg = 'Can\'t find file...'):
        self.msg = msg
# raise exception("Can\'t read file...")

def file(file_path):
    try:
        with open(file_path, "r") as filedata:
            data = filedata.read()
        return data
    except FileNotFoundError:
        raise exception("File not found!!!")
    except IOError as e:
        raise exception("Error occurred while reading file..!")            

file_path = "\PythonTask\Day_6\Textfil.txt"
try:
    result = file(file_path)
    print(result)

except exception as e:
    print(f"CaughtError: {e}")
