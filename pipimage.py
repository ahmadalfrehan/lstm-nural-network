from PIL import Image

from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

def main():

    try:
        path = "C:/Users/DELL/Desktop/"
        img = Image.open("C:/Users/DELL/Desktop/ahmadalfrehan.jpg")
        img = img.rotate(150)
        print(img)
        img.show()
        width, height = img.size
        img.save(path+"resized_picture.jpg")
    except IOError:
        print(IOError)
        pass


if __name__ == "__main__":
    main()
