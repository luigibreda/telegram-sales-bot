from cgitb import text
import pdb
from telegram import ReplyKeyboardRemove
from ..language import get_text
from telegram.ext import (
    Filters,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler)
from telegram_ecommerce.database.query import list_all_users_query
from telegram_ecommerce.handlers.show_categories import GET_LIST_OF_PRODUCTS
from telegram_ecommerce.tamplates.products import send_a_inline_with_a_list_of_products

(END, ASK_FOR_CATEGORY_NAME, GET_LIST_OF_PRODUCTS, LIST_ALL_USERS_CALLBACK, BUY_PROCESS) = range(-1, 4)

def list_all_users_callback(update, context):
    update.message.reply_text("Listando todos os usuários:")
    all_users = list_all_users_query()
    if all_users:
        for user in all_users:
            update.message.reply_text(str(user))
        return GET_LIST_OF_PRODUCTS
    else:
        update.message.reply_text("Nenhum usuário encontrado.")
        return END

lista_usuarios = CommandHandler("lista_usuarios", list_all_users_callback)
