from moderation import moderate
from Utils.handler import get_input, set_output
from Utils.format import format_input, format_output


def moderation_call(messages):
    moderation_flag = ""
    if messages:
        for msg in messages:
            for key in msg:
                moderation_flag = moderate(msg[key])

            msg.update({'moderation_status': moderation_flag})
    return messages


def main():
    messages, type = get_input()
    formatted_messages = format_input(messages, type)
    output = moderation_call(formatted_messages)
    formatted_output = format_output(messages, formatted_messages, output, type)
    set_output(formatted_output)


if __name__ == '__main__':
    main()
