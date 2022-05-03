from configs.config_vars import custom_status_codes


def messagesHandler(message_code):
    for i in list(custom_status_codes):
        if message_code in custom_status_codes[i]:
            message = custom_status_codes[i][message_code]
    return message