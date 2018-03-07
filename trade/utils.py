def list_with_and(lizt):
    if len(lizt) == 0:
        return str(lizt[0])

    out = ""

    for item in lizt[:-1]:
        out += str(item) + ", "

    out += "and " + str(lizt[-1])

    return out
