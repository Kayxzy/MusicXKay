from PrimeMusic import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5, ASS_CLI_6)


async def get_assistant_details(assistant: int):
    if int(assistant) == 1:
        a = ASS_CLI_1
    elif int(assistant) == 2:
        a = ASS_CLI_2
    elif int(assistant) == 3:
        a = ASS_CLI_3
    elif int(assistant) == 4:
        a = ASS_CLI_4
    elif int(assistant) == 5:
        a = ASS_CLI_5
    elif int(assistant) == 6:
        a = ASS_CLI_6
    return a
