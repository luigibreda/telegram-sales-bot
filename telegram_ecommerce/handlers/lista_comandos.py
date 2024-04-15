from telegram.ext import CommandHandler

def luigi_callback(update, context):
    try:
        # Obtém os comandos registrados no bot
        bot_commands = context.bot.get_my_commands()
        
        # Lista os comandos
        command_list = "\n".join([f"{command.command} - {command.description}" for command in bot_commands])
        
        # Envia a lista como mensagem de resposta
        update.message.reply_text(f"Comandos disponíveis no bot:\n{command_list}")
    except Exception as e:
        update.message.reply_text(f"Ocorreu um erro ao listar os comandos: {e}")

lista_comandos = CommandHandler("lista_comandos", luigi_callback) 