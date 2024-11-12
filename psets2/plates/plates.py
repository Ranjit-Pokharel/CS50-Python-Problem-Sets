def main():
    # ask user for palte 
    plate = input("Plate: ")

    # check for palte valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not valid_len(s):
        return False
    if not valid_two_char(s):
        return False
    if not valid_num_start_non_zero(s):
        return False
    if not valid_not_num_in_middle(s):
        return False
    return True   

def valid_two_char(text):
    if text[:2].isalpha():
        return True
    return False

def valid_len(text):
    if 1 < len(text) < 7:
        return True
    return False

def valid_not_num_in_middle(text):
    for i, ch in enumerate(text):
        if ch.isdigit() and len(text)-1 > i:
            if not text[i+1].isdigit():
                return False
    return True

def valid_num_start_non_zero(text):
    for ch in text:
        if ch.isdigit():
            if int(ch) == 0:
                return False
            else:
                break        
    
    return True


if __name__ == "__main__":
    main()