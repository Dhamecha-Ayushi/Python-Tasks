import multiprocessing
import requests

def downloadfile(url, name):
    print(f"download starting {name}")
    response=requests.get(url)
    #"wb" mode opens the file in binary format for writing. Unlike text files, binary files are not human-readable.
    open(f"Images/file{name}.jpg","wb").write(response.content)

    print(f"download finish {name}")
if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    process=[]

    for i in range(1,6):
    # downloadfile(url,i)
        j = multiprocessing.Process(target = downloadfile, args = [url,i])
        j.start()
        process.append(j)

    for j in process:
        j.join()