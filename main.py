main.py
import discord
from discord.ext import commands
from os import remove
from time import sleep
from cl_model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def photo(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
                await attachment.save(f'./images/{file_name}')
                msg = await ctx.send('Пытаюсь разобрать что на фото...')
                class_name, confidence = get_class(model_path='model/keras_model.h5', labels_path='model/labels.txt', image_path=f'/images/{file_name}')
                await msg.delete()
                await ctx.send(f'С вероятностью {confidence}% на фото {class_name.lower()}')
                remove(f'./images/{file_name}')
            else:
                await ctx.send('Неправильный формат файлов! (мне нужны картинки)')
                return
    else:
        await ctx.send('Кажется, ты забыл прикрепить фотографии ;c')
bot.run("")

cl_model.py
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def get_class(model_path, labels_path, image_path):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_Model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r", encoding='utf-8').readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("<IMAGE_PATH>").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    return class_name[2:len(class_name)], round(confidence_score)
