def give_choice(choices_list, choices_functions_list, message="What do you choose?"):
    i = 0
    for c in choices_list:
        print("%d. %s" % (i+1, c))
        i += 1
    choice = int(input(message)) - 1
    try:
        return choices_functions_list[choice]
    except:
        return "What you entered is not an option."