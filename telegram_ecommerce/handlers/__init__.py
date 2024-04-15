from telegram import BotCommand

from ..language import get_text
from .language import language
from .start import start
from .lista_comandos import lista_comandos
from .lista_usuarios import lista_usuarios
from .help import help_command
from .register import register
from .add_category import add_category
from .add_product import add_product 
from .show_categories import show_categories
from .search import search
from ..tamplates.rating import rating_precess_handlers
from ..tamplates.buy_callbacks import (
    pre_checkout_handler,
    successful_payment_handler)


all_handlers = ([
    start,
    help_command,
    register,
    add_category, 
    add_product, 
    language,
    search,
    show_categories, 
    lista_comandos,
    lista_usuarios,
    pre_checkout_handler, 
    successful_payment_handler] +
    rating_precess_handlers)


all_public_commands_descriptions = [
    BotCommand(
        "start", 
        get_text("start_description")
        ),
    BotCommand(
        "ajuda", 
        get_text("help_description")
        ),
    BotCommand(
        "buscar", 
        get_text("search_description")
        ),
    BotCommand(
        "registrar", 
        get_text("register_description")
        ),
    BotCommand(
        "idioma", 
        get_text("language_description")
        ),
    BotCommand(
        "categorias", 
        get_text("show_categories_description")
        ),
    BotCommand(
        "lista_comandos", 
        get_text("lista_comandos_descricao")
        ),
        BotCommand(
        "lista_usuarios",
        get_text("lista_usuarios_descricao")
        )
    ]


