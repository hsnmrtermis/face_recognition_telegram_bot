from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler, CallbackQueryHandler, CallbackContext
import numpy as np
from io import BytesIO
import helper
from FaceRecognition import FaceRecognition


async def start(updater, context):
    await updater.message.reply_text('Face recognition app.')


async def help(updater, context):
    await updater.message.reply_text(
        """
         Tanımamı istediğin kişinin fotoğrafını at. \n
        /help uygulama hakkında bilgi verir. \n
        /count klasorlerdeki resim sayılarını verir.
        /delete klasorlerdeki resimleri siler
        """)


async def image(updater: Update , context: ContextTypes.DEFAULT_TYPE):
    photo = await  context.bot.get_file(updater.message.photo[-1].file_id)
    savedPhoto = await helper.savePhoto(photo)
    face_recognition = FaceRecognition()
    face_recognition.clear_properties()
    face_recognition.run_recognition(savedPhoto)
    for cropped_image, name in zip(face_recognition.cropped_faces, face_recognition.face_names):
        helper.sendPhoto(cropped_image)
        await updater.message.reply_text(name)
    del face_recognition
    await updater.message.reply_text('İşlem bitti.')
    
    
async def fileCount(updater: Update, context: ContextTypes.DEFAULT_TYPE):
    cropped_faces = helper.getCountOfDirectoryFiles('cropped_faces')
    permanents = helper.getCountOfDirectoryFiles('permanents')
    await updater.message.reply_text(f"cropped_faces klasorunde: {cropped_faces} adet fotograf var. permanents klasorunde: {permanents} adet fotograf var.")
    
async def deleteImageFolders(updater: Update, context: ContextTypes.DEFAULT_TYPE):
    helper.removeImageFolders()
    await updater.message.reply_text(f"cropped_faces ve permanents klasoru icindeki fotograflar silindi.")


app = ApplicationBuilder().token(
    "TOKEN GELECEK").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("count", fileCount))
app.add_handler(CommandHandler("delete", deleteImageFolders))
app.add_handler(MessageHandler(filters.PHOTO, image))

app.run_polling()