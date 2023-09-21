import os
import typer
import PIL
from PIL import Image


app = typer.Typer()
PIL.Image.MAX_IMAGE_PIXELS = 368640000


@app.command()
def png_to_pbm(dir_path: str):
    for path in os.listdir(dir_path):
        if path.endswith(".png"):
            Image.open(
                f"{dir_path}/{path}"
            ).convert("RGB").save(f'{dir_path}/{path.rsplit(".", 1)[0]}.ppm')


@app.command()
def pbm_to_png(dir_path: str):
    for path in os.listdir(dir_path):
        if path.endswith(".ppm"):
            Image.open(
                f"{dir_path}/{path}"
            ).save(f'{dir_path}/{path.rsplit(".", 1)[0]}.png')


if __name__ == "__main__":
    app()
