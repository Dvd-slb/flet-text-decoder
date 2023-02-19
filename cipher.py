alphabet_mixed = ['Ň', 'ř', 'í', 'ě', '5', 'ď', 'O', '0', 'D', '=', 's', 'G', '<', 'p', 'É', 'Í', 'Á', 'ů', 'j', 'w', '.', 'r', 'V', 'g', 'y', 'f', '>', '(', 'Ú', 'i', 'a', 'X', '"', '3', 'M', 'q', 'u', 'R', '?', 'd', ')', '+', 't', 'J', 'š', 'Y', '!', 'Ó', 'k', 'Č', 'H', 'U', 'v', 'ó', '-', 'B', 'ť', 'o', 'z', 'L', ' ', 'n', '#', '&', '9', 'ž', 'Z', 'Ě', "'", 'Ý', '8', '4', '2', 'K', 'N', 'c', 'Ž', 'ú', 'é', 'A', ':', 'l', 'ý', '7', 'e', 'Q', 'č', 'I', 'S', 'Š', '/', 'C', 'F', 'Ť', 'b', 'P', 'á', 'm', 'T', '6', '*', 'h', 'Ř', 'W', 'Ů', 'x', 'E', ';', ',', '1', 'Ď']


def cipher_encode(text, move):
    end_text = ""
    for one_letter in text:
        if one_letter in alphabet_mixed:
            index = alphabet_mixed.index(one_letter)
            if move % 111 == 0:
                move = 59
            new_index = index + move
            if new_index >= 111:
                new_index = new_index - new_index + (new_index % 111)
            end_text += alphabet_mixed[new_index]
        else:
            end_text += one_letter
    return end_text


def cipher_decode(text, move):
    end_text = ""
    for one_letter in text:
        if one_letter in alphabet_mixed:
            index = alphabet_mixed.index(one_letter)
            if move % 111 == 0:
                move = 59
            new_index = index - move
            if new_index <= -111:
                new_index = new_index - new_index + (new_index % 111)
            end_text += alphabet_mixed[new_index]
        else:
            end_text += one_letter
    return end_text
