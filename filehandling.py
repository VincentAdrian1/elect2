def read_write_file(filename, read_mode="r", write_mode="w", content=None):

  with open(filename, read_mode) as file:
    
    if read_mode == "r":
      contents = file.read()
      return contents

    elif read_mode == "a":
      if content is not None:
        file.write(content + "\n")
    else:
      if write_mode == "w" and content is not None:
        file.write(content)

file_contents = read_write_file("my_file.txt")
print(file_contents)

read_write_file("my_file.txt", write_mode="w", content="This is new content")

read_write_file("my_file.txt", read_mode="a", content="This is appended content")