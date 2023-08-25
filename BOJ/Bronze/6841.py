def txtmsg(msg):
    short_form = {
        "CU": "see you",
        ":-)": "I’m happy",
        ":-()": "I’m unhappy",
        ";-)": "wink",
        ":-P": "stick out my tongue",
        "(~.~)": "sleepy",
        "TA": "totally awesome",
        "CCC": "Canadian Computing Competition",
        "CUZ": "because",
        "TY": "thank-you",
        "YW": "you’re welcome",
        "TTYL": "talk to you later"
    }

    if msg in short_form:
        msg = short_form[msg]

    return msg


while True:
    try:
        msg = input()
        print(txtmsg(msg))
    except EOFError:
        break
