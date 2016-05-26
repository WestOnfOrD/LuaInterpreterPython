def lexDict(lexeme):
    return {
        'print' : "PRINT_TOK",
        'if' : 'IF_TOK',
        'then' : 'THEN_TOK',
        'else' : 'ELSE_TOK',
        'while' : 'WHILE_TOK',
        'do' : 'DO_TOK',
        'repeat' : 'REPEAT_TOK',
        'until' : 'UNTIL_TOK',
        'end' : 'END_TOK',
        'function' : 'FUNCTION_TOK',
        '+' : 'ADD_TOK',
        '*' : 'MUL_TOK',
        '-' : 'SUB_TOK',
        '/' : 'DIV_TOK',
        '=' : 'ASSIGN_TOK',
        '>' : 'GT_TOK',
        '<' : 'LT_TOK',
        '(' : 'OPENP_TOK',
        ')' : 'CLOSEP_TOK',
        '1' : 'CONST_TOK',
        '2' : 'CONST_TOK',
        '3' : 'CONST_TOK',
        '4' : 'CONST_TOK',
        '5' : 'CONST_TOK',
        '6' : 'CONST_TOK',
        '7' : 'CONST_TOK',
        '8' : 'CONST_TOK',
        '9' : 'CONST_TOK',
        '0' : 'CONST_TOK',
        '==' : 'EQ_TOK',
        '~=' : 'NE_TOK',
        '>=' : 'GE_TOK',
        '<=' : 'LE_TOK',
        '' : 'EOS_TOK',
        #Well this turned into a monstrosity
        #No time for optimization unfortunately
        'a' : 'ID_TOK',
        'b' : 'ID_TOK',
        'c' : 'ID_TOK',
        'd' : 'ID_TOK',
        'e' : 'ID_TOK',
        'f' : 'ID_TOK',
        'g' : 'ID_TOK',
        'h' : 'ID_TOK',
        'i' : 'ID_TOK',
        'j' : 'ID_TOK',
        'k' : 'ID_TOK',
        'l' : 'ID_TOK',
        'm' : 'ID_TOK',
        'n' : 'ID_TOK',
        'o' : 'ID_TOK',
        'p' : 'ID_TOK',
        'q' : 'ID_TOK',
        'r' : 'ID_TOK',
        's' : 'ID_TOK',
        't' : 'ID_TOK',
        'u' : 'ID_TOK',
        'v' : 'ID_TOK',
        'w' : 'ID_TOK',
        'x' : 'ID_TOK',
        'y' : 'ID_TOK',
        'z' : 'ID_TOK',
        'A' : 'ID_TOK',
        'B' : 'ID_TOK',
        'C' : 'ID_TOK',
        'D' : 'ID_TOK',
        'E' : 'ID_TOK',
        'F' : 'ID_TOK',
        'G' : 'ID_TOK',
        'H' : 'ID_TOK',
        'I' : 'ID_TOK',
        'J' : 'ID_TOK',
        'K' : 'ID_TOK',
        'L' : 'ID_TOK',
        'M' : 'ID_TOK',
        'N' : 'ID_TOK',
        'O' : 'ID_TOK',
        'P' : 'ID_TOK',
        'Q' : 'ID_TOK',
        'R' : 'ID_TOK',
        'S' : 'ID_TOK',
        'T' : 'ID_TOK',
        'U' : 'ID_TOK',
        'V' : 'ID_TOK',
        'W' : 'ID_TOK',
        'X' : 'ID_TOK',
        'Y' : 'ID_TOK',
        'Z' : 'ID_TOK'
    }.get(lexeme, None)