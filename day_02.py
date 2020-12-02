"""--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down
 to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. 
"Something's wrong with our computers; we can't log in!" You ask if you can take
 a look.

Their password database seems to be a little corrupted: some of the passwords 
wouldn't have been allowed by the Official Toboggan Corporate Policy that was in
 effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of 
passwords (according to the corrupted database) and the corporate policy when 
that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy 
indicates the lowest and highest number of times a given letter must appear for 
the password to be valid. For example, 1-3 a means that the password must contain 
a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; 
it contains no instances of b, but needs at least 1. The first and third passwords 
are valid: they contain one a or nine c, both within the limits of their respective 
policies.

How many passwords are valid according to their policies?

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be 
what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password 
policy rules from his old job at the sled rental place down the street! The
Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the 
first character, 2 means the second character, and so on. (Be careful; Toboggan 
Corporate Policies have no concept of "index zero"!) Exactly one of these positions 
must contain the given letter. Other occurrences of the letter are irrelevant for 
the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""

def main(part_number):

    if part_number not in [1, 2]:
        print('Invalid part number.')
        return 
    
    check_functions = {
        1: is_password_valid_1,
        2: is_password_valid_2
    }

    rules_passwords = get_rules_and_passwords()

    num_valid_passwords = 0

    for rule_password_tuple in rules_passwords:
        if check_functions[part_number](*rule_password_tuple):
            num_valid_passwords += 1

    print(f"---Part {part_number}---")
    print(f"Number of valid passwords: {num_valid_passwords}")
    return

    
#------------------------------------------------------------------------------
# HELPER FUNCTIONS
#------------------------------------------------------------------------------

def get_rules_and_passwords():
    """Read and parse the input file and return a list of tuples
    containing a rule and a password.
    EX: ("1-5 x", "amxkdisskf")
    """
    input_file = 'input_files/input_day_02.txt'

    with open(input_file, 'r') as f:
        password_lines = [line.rstrip("\n") for line in f.readlines()]
    
    rules_passwords = []
    for password_line in password_lines:
        rules_passwords.append(password_line.split(": "))

    return rules_passwords # List of tuples: (rule, password)

def parse_rule(rule):
    """Parse the rule string to return 2 integers and a character.
    """
    first_number, second_number = rule.split("-")
    second_number, char = second_number.split(" ")

    first_number = int(first_number)
    second_number = int(second_number)

    return first_number, second_number, char

def is_password_valid_1(rule, password):
    """Check password according to supplied rule string.
    Rule defines a character and a minimum and maximum number of occurrences
    of the character in the password.
    Returns True if number of occurrences in the password is within the range.
    Returns False otherwise.
    """
    char_min, char_max, char = parse_rule(rule)

    num_occurrences = password.count(char)

    return char_min <= num_occurrences <= char_max

def is_password_valid_2(rule, password):
    """Check password according to supplied rule string.
    Rule defines a character and 2 positions in the passwords to check.
    Exactly ONE of these positions must contain the given letter.
    """
    position_one, position_two, char = parse_rule(rule)

    in_position_one = password[position_one-1] == char
    in_position_two = password[position_two-1] == char

    return in_position_one != in_position_two


if __name__ == "__main__":
    # Run!
    main(part_number=1)
    main(part_number=2)
