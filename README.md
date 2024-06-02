# Logic-Language
This is a programming language but only for binary and logic gates.

the .lg file (LogicGate) is a file with planned commands like:
    And
    Nand
    Or
    Nor
    Xor
    Xnor
    Not
    Out

VERSION 0.3.0 JUST CAME OUT!!! YOU CAN NOW STACK GATES IN VARIABLES LIKE THIS:
    bin a = and 1 1;
    bin b = and a 1;
IT IS ALSO NOW RELEASED ON GITHUB!!


The Tokens that are currently implemented are:
    And
    Or
    Not
    Declarator
    Declaration
    End_Line
    Binary
    Equal

The Parsed Token Combinations are:
    And, Binary, Binary, End_Line
    Or, Binary, Binary, End_Line
    Not, Binary, End_Line
    Declarator, Declaration, Equal, Binary, End_Line
    Declarator, Declaration, Equal, Logic_Gate, Binary, Binary, End_Line

The Functions I have currently implemented are:
    And
    Or
    Not

If you want to run the .lg code, you'll have to run the python file.
