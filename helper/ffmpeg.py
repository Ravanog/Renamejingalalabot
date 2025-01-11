import time
import os
import asyncio
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image, UnidentifiedImageError
import subprocess

def convert_with_ffmpeg(input_file, output_file):
    command = ["ffmpeg", "-i", input_file, "-vf", "format=yuv420p", output_file]
    subprocess.run(command)
def process_image(file_path):
    try:
        with Image.open(file_path) as img:
            # Ensure it's in the correct format
            img = img.convert("RGB")
            img.save(file_path, "JPEG", optimize=True, progressive=False)
            print("Image converted to Baseline JPEG format.")
    except UnidentifiedImageError:
        print("The file is not a valid image.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call this before processing images in your bot
process_image("input.jpg")

def convert_to_baseline(image_path, output_path):
    with Image.open(image_path) as img:
        img = img.convert("RGB")  # Ensure it's in RGB mode
        img.save(output_path, "JPEG", optimize=True, progressive=False)

# Example usage:
convert_to_baseline("input.jpg", "output.jpg")

async def fix_thumb(thumb):
    width = 0
    height = 0
    try:
        if thumb != None:
            parser = createParser(thumb)
            metadata = extractMetadata(parser)
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
                
            # Open the image file
            with Image.open(thumb) as img:
                # Convert the image to RGB format and save it back to the same file
                img.convert("RGB").save(thumb)
            
                # Resize the image
                resized_img = img.resize((width, height))
                
                # Save the resized image in JPEG format
                resized_img.save(thumb, "JPEG")
            parser.close()
    except Exception as e:
        print(e)
        thumb = None 
       
    return width, height, thumb
    
async def take_screen_shot(video_file, output_directory, ttl):
    out_put_file_name = f"{output_directory}/{time.time()}.jpg"
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        out_put_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None
