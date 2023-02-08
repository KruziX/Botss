# Слито в https://t.me/HACKER_PHONE_VIP

import random, db, logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import BoundFilter
import keyboards as kb
from config import TOKEN
from string import ascii_letters, digits


# Слито в https://t.me/HACKER_PHONE_VIP

logging.basicConfig(level=logging.INFO)

# Слито в https://t.me/HACKER_PHONE_VIP

class IsPrivate(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.PRIVATE
class Info(StatesGroup):
    upload_file = State()
    upload_file_password = State()
    delete_file = State()
    check_password = State()

# Слито в https://t.me/HACKER_PHONE_VIP

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.message_handler(IsPrivate(), commands=['start'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    users = []
    with open('users.txt', 'r', encoding='utf-8') as file:
        users = [line.strip() for line in file.readlines()]

# Слито в https://t.me/HACKER_PHONE_VIP

    if str(message.chat.id) not in users:
        with open('users.txt', 'a', encoding='utf-8') as file:
            file.write(str(message.chat.id)+ "\n")
    args = message.get_args()
    bot_data = await bot.get_me()
    bot_name = bot_data['username']
    if db.get_users_exist(message.chat.id) == False:
        db.add_user_to_db(message.chat.id)
        if not args:
            await bot.send_message(chat_id=message.chat.id, text='👋 Я - бот для обмена файлов, давайте приступим!', reply_markup = kb.menu_kb())
        else:
            type_file, fileID, views, password = db.get_file(args)
            if type_file is None and fileID is None:
                await bot.send_message(chat_id=message.chat.id, text='🚫 Файл не найден', reply_markup = kb.menu_kb())
            else:
                if password == (None,):
                    db.update_views(args)
                    if type_file[0] == 'photo':
                        await bot.send_photo(chat_id=message.chat.id, photo=fileID[0], caption=f'⚡ файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n 🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                    elif type_file[0] == 'video':
                        await bot.send_video(chat_id=message.chat.id, video=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n 🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                    elif type_file[0] == 'voice':
                        await bot.send_voice(chat_id=message.chat.id, voice=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n 🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                    elif type_file[0] == 'document':
                        await bot.send_document(chat_id=message.chat.id, document=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                else:
                    await bot.send_message(chat_id=message.chat.id, text='🛡️ Файл защищён, введите пароль', reply_markup = kb.back_kb())
                    await state.update_data(check_password=args)
                    await Info.check_password.set()
    else:
        if not args:
            await bot.send_message(chat_id=message.chat.id, text='👋 Я - бот для обмена файлами, давайте приступим!', reply_markup = kb.menu_kb())
        else:
            type_file, fileID, views, password = db.get_file(args)
            if type_file is None and fileID is None:
                await bot.send_message(chat_id=message.chat.id, text='🚫 Файл не найден', reply_markup = kb.menu_kb())
            else:
                if password == (None,):
                    db.update_views(args)
                    if type_file[0] == 'photo':
                        await bot.send_photo(chat_id=message.chat.id, photo=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                    elif type_file[0] == 'video':
                        await bot.send_video(chat_id=message.chat.id, video=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                    elif type_file[0] == 'voice':
                        await bot.send_voice(chat_id=message.chat.id, voice=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                    elif type_file[0] == 'document':
                        await bot.send_document(chat_id=message.chat.id, document=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                else:
                    await bot.send_message(chat_id=message.chat.id, text='🛡️ Файл защищён, введите пароль', reply_markup = kb.back_kb())
                    await state.update_data(check_password=args)
                    await Info.check_password.set()

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.message_handler(state=Info.check_password, content_types=types.ContentTypes.ANY)
async def upload_file(message: types.Message, state: FSMContext):
    bot_data = await bot.get_me()
    bot_name = bot_data['username']
    if message.text:
        if message.text.lower() == 'отмена':
            await bot.send_message(chat_id=message.chat.id, text='🚀 Вы вернулись в главное меню', reply_markup=kb.menu_kb())
            await state.finish()
        else:
            user_data = await state.get_data()
            code = user_data['check_password']
            type_file, fileID, views, password = db.get_file(code)
            print(views[0])
            if message.text == password[0]:
                db.update_views(code)
                if type_file[0] == 'photo':
                    await bot.send_photo(chat_id=message.chat.id, photo=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={args}', reply_markup = kb.menu_kb())
                elif type_file[0] == 'video':
                    await bot.send_video(chat_id=message.chat.id, video=fileID[0], caption=f'Вот ваш файл:\n\n Просмотры: {int(views[0])+1}\n\nВы перешли по ссылке: https://t.me/{str(bot_name)}?start={code}', reply_markup = kb.menu_kb())
                elif type_file[0] == 'voice':
                    await bot.send_voice(chat_id=message.chat.id, voice=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={code}', reply_markup = kb.menu_kb())
                elif type_file[0] == 'document':
                    await bot.send_document(chat_id=message.chat.id, document=fileID[0], caption=f'⚡ Ваш файл:\n\n 👁️‍🗨️ Просмотры: {int(views[0])+1}\n\n🔗 Вы перешли по ссылке: https://t.me/{str(bot_name)}?start={code}', reply_markup = kb.menu_kb())
                await state.finish()
            else:
                await bot.send_message(chat_id=message.chat.id, text='🚫 Неверный пароль!', reply_markup = kb.back_kb())
    else:
        await bot.send_message(chat_id=message.chat.id, text='🛡️ Файл защищён, введите пароль', reply_markup = kb.back_kb())

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.message_handler(text="📥 Загрузить файл")
async def create_post(message: types.Message):
    if db.get_users_exist(message.chat.id) == True:
        await bot.send_message(message.chat.id, text='🟡 Отправь мне файл.', reply_markup = kb.back_kb())
        await Info.upload_file.set()

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.message_handler(text="🌸 Мои файлы")
async def create_post(message: types.Message):
    if db.get_users_exist(message.chat.id) == True:
        bot_data = await bot.get_me()
        bot_name = bot_data['username']
        all_types, all_ids, all_views, passwords = db.get_files_user(message.from_user.id)
        if all_types == []:
            await bot.send_message(message.chat.id, text='😪 У Вас нету загруженных файлов, чтобы загрузить файлы нажмите "📥 Загрузить файл"', reply_markup = kb.menu_kb())
        else:
            text='🛡️ Ваши файлы: \n\n'
            for i, id_file in enumerate(all_ids):
                text+=f'{i+1}. https://t.me/{str(bot_name)}?start={id_file[0]} | {all_types[i][0]} | {all_views[i][0]} | 🔣 Пароль: {passwords[i][0]}\n\n'
            await bot.send_message(chat_id=message.chat.id, text=text, reply_markup = kb.delete_file())

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.message_handler(state=Info.upload_file_password, content_types=types.ContentTypes.TEXT)
async def upload_file(message: types.Message, state: FSMContext):
    bot_data = await bot.get_me()
    bot_name = bot_data['username']
    user_data = await state.get_data()
    file_data = user_data['upload_file_password']
    if message.text == '-':
        if file_data.split('|')[1] == 'photo':
            code = file_data.split('|')[2]
            db.add_new_file(file_data.split('|')[0], 'photo', file_data.split('|')[2], file_data.split('|')[3])
            await bot.send_message(chat_id=message.chat.id, text=f'🚀 Файл был успешно загружен.\n\n 🔗 Чтобы поделиться им отправь данную ссылку: https://t.me/{bot_name}?start={code}', reply_markup=kb.menu_kb())
            await state.finish()
        elif file_data.split('|')[1] == 'video':
            code = file_data.split('|')[2]
            db.add_new_file(file_data.split('|')[0], 'video', file_data.split('|')[2], file_data.split('|')[3])
            await bot.send_message(chat_id=message.chat.id, text=f'🚀 Файл был успешно загружен.\n\n🔗 Чтобы поделиться им отправь данную ссылку: https://t.me/{bot_name}?start={code}', reply_markup=kb.menu_kb())
            await state.finish()
        elif file_data.split('|')[1] == 'voice':
            code = file_data.split('|')[2]
            db.add_new_file(file_data.split('|')[0], 'voice', file_data.split('|')[2], file_data.split('|')[3])
            await bot.send_message(chat_id=message.chat.id, text=f'🚀 Файл был успешно загружен.\n\n🔗 Чтобы поделиться им отправь данную ссылку: https://t.me/{bot_name}?start={code}', reply_markup=kb.menu_kb())
            await state.finish()
        elif file_data.split('|')[1] == 'document':
            code = file_data.split('|')[2]
            db.add_new_file(file_data.split('|')[0], 'document', file_data.split('|')[2], file_data.split('|')[3])
            await bot.send_message(chat_id=message.chat.id, text=f'🚀 Файл был успешно загружен.\n\n🔗 Чтобы поделиться им отправь данную ссылку: https://t.me/{bot_name}?start={code}', reply_markup=kb.menu_kb())
            await state.finish()
    elif message.text.lower() == '🚫 Отмена':
        await bot.send_message(chat_id=message.chat.id, text='🚀 Вы вернулись в главное меню', reply_markup=kb.menu_kb())
        await state.finish()
    else:
        if file_data.split('|')[1] == 'photo':
            code = file_data.split('|')[2]
            db.add_new_file_with_password(file_data.split('|')[0], 'photo', file_data.split('|')[2], file_data.split('|')[3], message.text)
            await bot.send_message(chat_id=message.chat.id, text=f'🚀 Файл был успешно загружен.\n\nПароль: {message.text}\n\n 🔗 Чтобы поделиться им отправь данную ссылку: https://t.me/{bot_name}?start={code}', reply_markup=kb.menu_kb())
            await state.finish()
        elif file_data.split('|')[1] == 'video':
            code = file_data.split('|')[2]
            db.add_new_file_with_password(file_data.split('|')[0], 'video', file_data.split('|')[2], file_data.split('|')[3], message.text)
            await bot.send_message(chat_id=message.chat.id, text=f'🚀 Файл был успешно загружен.\n\n🔣 Пароль: {message.text}\n\n🔗 Чтобы поделиться им отправь данную ссылку: https://t.me/{bot_name}?start={code}', reply_markup=kb.menu_kb())
            await state.finish()
        elif file_data.split('|')[1] == 'voice':
            code = file_data.split('|')[2]
            db.add_new_file_with_password(file_data.split('|')[0], 'voice', file_data.split('|')[2], file_data.split('|')[3], message.text)
            await bot.send_message(chat_id=message.chat.id, text=f'🚀 Файл был успешно загружен.\n\n🔣 Пароль: {message.text}\n\n🔗 Чтобы поделиться им отправь данную ссылку: https://t.me/{bot_name}?start={code}', reply_markup=kb.menu_kb())
            await state.finish()
        elif file_data.split('|')[1] == 'document':
            code = file_data.split('|')[2]
            db.add_new_file_with_password(file_data.split('|')[0], 'document', file_data.split('|')[2], file_data.split('|')[3], message.text)
            await bot.send_message(chat_id=message.chat.id, text=f'🚀 Файл был успешно загружен.\n\n🔣 Пароль: {message.text}\n\n🔗 Чтобы поделиться им отправь данную ссылку: https://t.me/{bot_name}?start={code}', reply_markup=kb.menu_kb())
            await state.finish()

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.message_handler(state=Info.upload_file, content_types=types.ContentTypes.ANY)
async def upload_file(message: types.Message, state: FSMContext):
    bot_data = await bot.get_me()
    bot_name = bot_data['username']
    if message.photo:
        fileID = message.photo[-1].file_id
        code = ''.join(random.sample(ascii_letters + digits, random.randint(33, 40)))
        await state.update_data(upload_file_password=f'{message.from_user.id}|photo|{code}|{fileID}')
        await bot.send_message(chat_id=message.chat.id, text='🛡️ Создайте пароль, для отмены отправьте "-"', reply_markup=kb.back_kb())
        await Info.upload_file_password.set()
    elif message.text:
        if message.text.lower() == '🚫 Отмена':
            await bot.send_message(chat_id=message.chat.id, text='🚀 Вы вернулись в меню.', reply_markup=kb.menu_kb())
            await state.finish()
        else:
            await bot.send_message(chat_id=message.chat.id, text='🟡 Отправь мне файл.', reply_markup=kb.back_kb())
    elif message.voice:
        fileID = message.voice.file_id
        code = ''.join(random.sample(ascii_letters + digits, random.randint(33, 40)))
        await state.update_data(upload_file_password=f'{message.from_user.id}|voice|{code}|{fileID}')
        await bot.send_message(chat_id=message.chat.id, text='🛡️ Создайте пароль, для отмены отправьте "-"', reply_markup=kb.back_kb())
        await Info.upload_file_password.set()
    elif message.video:
        fileID = message.video.file_id
        code = ''.join(random.sample(ascii_letters + digits, random.randint(33, 40)))
        await state.update_data(upload_file_password=f'{message.from_user.id}|video|{code}|{fileID}')
        await bot.send_message(chat_id=message.chat.id, text='🛡️ Создайте пароль, для отмены отправьте "-"', reply_markup=kb.back_kb())
        await Info.upload_file_password.set()
    elif message.document:
        fileID = message.document.file_id
        code = ''.join(random.sample(ascii_letters + digits, random.randint(33, 40)))
        await state.update_data(upload_file_password=f'{message.from_user.id}|document|{code}|{fileID}')
        await bot.send_message(chat_id=message.chat.id, text='🛡️ Создайте пароль, для отмены отправьте "-"', reply_markup=kb.back_kb())
        await Info.upload_file_password.set()

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.message_handler(state=Info.delete_file, content_types=types.ContentTypes.TEXT)
async def del_file(message: types.Message, state: FSMContext):
    try:
        number = int(message.text)
        user_data = await state.get_data()
        mess_id = user_data['delete_file']
        all_types, all_ids, all_views, passwords = db.get_files_user(message.from_user.id)
        if number > len(all_ids):
            await bot.send_message(chat_id=message.chat.id, text='🚫 Файла не существует. Введите номер файла:', reply_markup=kb.delete_back())
        else:
            db.delete_file(all_ids[(number-1)][0])
            await bot.delete_message(message.chat.id, mess_id)
            await bot.send_message(chat_id=message.chat.id, text='⚡ Вы успешно удалили файл!', reply_markup=kb.menu_kb())
            await state.finish()
    except ValueError:
        await bot.send_message(chat_id=message.chat.id, text='🔢 Введите номер файла', reply_markup=kb.delete_back())

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.callback_query_handler(state='*')
async def handler_call(call: types.CallbackQuery, state: FSMContext):
    bot_data = await bot.get_me()
    bot_name = bot_data['username']
    chat_id = call.from_user.id
    if call.data == 'delete_file':
        all_types, all_ids, all_views, passwords = db.get_files_user(chat_id)
        if all_ids == []:
            await bot.delete_message(chat_id, call.message.message_id)
            await bot.send_message(chat_id=chat_id, text='🚫 У Вас нет загруженных файлов, чтобы загрузить файлы нажмите "📥 Загрузить файл"', reply_markup = kb.menu_kb())
        else:
            text='📁 Файлы для удаления: \n\n'
            for i, id_file in enumerate(all_ids):
                text+=f'{i+1}. https://t.me/{str(bot_name)}?start={id_file[0]} | {all_types[i][0]} | {all_views[i][0]} | 🔣 Пароль: {passwords[i][0]}\n\n'
            text+='🔢 Введите номер файла, который Вы хотите удалить.'
            await bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=text, reply_markup=kb.delete_back())
            await state.update_data(delete_file=call.message.message_id)
            await Info.delete_file.set()
    if call.data == 'delete_back':
        await state.finish()
        all_types, all_ids, all_views, passwords = db.get_files_user(chat_id)
        if all_ids == []:
            await bot.delete_message(chat_id, call.message.message_id)
            await bot.send_message(chat_id=chat_id, text='🚫 У Вас нет загруженных файлов, чтобы загрузить файлы нажмите "📥 Загрузить файл"', reply_markup = kb.menu_kb())
        else:
            text='📁 Ваши файлы: \n\n'
            for i, id_file in enumerate(all_ids):
                text+=f'{i+1}. https://t.me/{str(bot_name)}?start={id_file[0]} | {all_types[i][0]} | {all_views[i][0]} | 🔣 Пароль: {passwords[i][0]}\n\n'
            await bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=text, reply_markup=kb.delete_file())

# Слито в https://t.me/HACKER_PHONE_VIP

if __name__ == "__main__":
    db.check_db()
    executor.start_polling(dp, skip_updates=True)

# Слито в https://t.me/HACKER_PHONE_VIP