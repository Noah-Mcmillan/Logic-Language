'''
PUT FILE DIRECTORY IN LINE 16
'''
gates = [
    "And",
    "Or",
    "Not",
    "Nand",
    "Nor",
    "Xor",
    "Xnor"
]

##### FILE READING #####
with open("DIRECTORY HERE", "r") as f:
    tokens = []
    words = []

    variables = []

    ######################### LEXER #########################

    for line in f:
        for word in line.split():
            word = word.upper()
            e = False

            if word[-1] == ";":
                words.append(word[:-1])
                e = True
                words.append(";")
            else:
                words.append(word)

            if word == "AND":
                tokens.append("And")
            elif word == "OR":
                tokens.append("Or")
            elif word == "NOT":
                tokens.append("Not")
            elif word == "NAND":
                tokens.append("Nand")
            elif word == "NOR":
                tokens.append("Nor")
            elif word == "XOR":
                tokens.append("Xor")
            elif word == "XNOR":
                tokens.append("Xnor")
            elif word == "OUT":
                tokens.append("Out")
            elif word == "RESET":
                tokens.append("Reset")
            elif word.isdigit() or word[:-1].isdigit():
                tokens.append("Binary")
            elif word == "BIN":
                tokens.append("Declarator")
            elif word == "=":
                tokens.append("Equal")
            else:
                tokens.append("Declaration")
            
            if e == True:
                tokens.append("End_Line")
    
    #print(tokens)
    #print(words)

    ######################### PARSER/EXECUTER #########################

    variable_index = 0
    parsed_index = 0

    for token in tokens:

        if token == "And" and (tokens[parsed_index+1] == "Binary" or tokens[parsed_index+1] == "Declaration") and (tokens[parsed_index+2] == "Binary" or tokens[parsed_index+2] == "Declaration") and tokens[parsed_index+3] == "End_Line" and tokens[parsed_index-1] == "End_Line":
            t0 = words[parsed_index+1]
            t1 = words[parsed_index+2]
            p = False
            p0 = False
            p1 = False

            if tokens[parsed_index+1] == "Binary" and tokens[parsed_index+2] == "Binary":
                p = True
            if tokens[parsed_index+1] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p = True
            if tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p = True
            if tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p0 = True
                        if p0 and p1 == True:
                            p = True
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p1 = True
                        if p0 and p1 == True:
                            p = True
            if p == True:
                if t0 == "1" and t1 == "1":
                    print("And: "+str(True))
                else:
                    print("And: "+str(False))
        
        elif token == "Or" and (tokens[parsed_index+1] == "Binary" or tokens[parsed_index+1] == "Declaration") and (tokens[parsed_index+2] == "Binary" or tokens[parsed_index+2] == "Declaration") and tokens[parsed_index+3] == "End_Line" and tokens[parsed_index-1] == "End_Line":
            t0 = words[parsed_index+1]
            t1 = words[parsed_index+2]
            p = False
            p0 = False
            p1 = False

            if tokens[parsed_index+1] == "Binary" and tokens[parsed_index+2] == "Binary":
                p = True
            if tokens[parsed_index+1] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p = True
            if tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p = True
            if tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p0 = True
                        if p0 and p1 == True:
                            p = True
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p1 = True
                        if p0 and p1 == True:
                            p = True
            if p == True:
                if t0 == "1" or t1 == "1":
                    print("Or: "+str(True))
                else:
                    print("Or: "+str(False))
        elif token == "Nand" and (tokens[parsed_index+1] == "Binary" or tokens[parsed_index+1] == "Declaration") and (tokens[parsed_index+2] == "Binary" or tokens[parsed_index+2] == "Declaration") and tokens[parsed_index+3] == "End_Line" and tokens[parsed_index-1] == "End_Line":
            t0 = words[parsed_index+1]
            t1 = words[parsed_index+2]
            p = False
            p0 = False
            p1 = False

            if tokens[parsed_index+1] == "Binary" and tokens[parsed_index+2] == "Binary":
                p = True
            if tokens[parsed_index+1] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p = True
            if tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p = True
            if tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p0 = True
                        if p0 and p1 == True:
                            p = True
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p1 = True
                        if p0 and p1 == True:
                            p = True
            if p == True:
                if t0 == "0" or t1 == "0":
                    print("Nand: "+str(True))
                else:
                    print("Nand: "+str(False))
        elif token == "Nor" and (tokens[parsed_index+1] == "Binary" or tokens[parsed_index+1] == "Declaration") and (tokens[parsed_index+2] == "Binary" or tokens[parsed_index+2] == "Declaration") and tokens[parsed_index+3] == "End_Line" and tokens[parsed_index-1] == "End_Line":
            t0 = words[parsed_index+1]
            t1 = words[parsed_index+2]
            p = False
            p0 = False
            p1 = False

            if tokens[parsed_index+1] == "Binary" and tokens[parsed_index+2] == "Binary":
                p = True
            if tokens[parsed_index+1] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p = True
            if tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p = True
            if tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p0 = True
                        if p0 and p1 == True:
                            p = True
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p1 = True
                        if p0 and p1 == True:
                            p = True
            if p == True:
                if t0 == "0" and t1 == "0":
                    print("Nor: "+str(True))
                else:
                    print("Nor: "+str(False))
        elif token == "Xor" and (tokens[parsed_index+1] == "Binary" or tokens[parsed_index+1] == "Declaration") and (tokens[parsed_index+2] == "Binary" or tokens[parsed_index+2] == "Declaration") and tokens[parsed_index+3] == "End_Line" and tokens[parsed_index-1] == "End_Line":
            t0 = words[parsed_index+1]
            t1 = words[parsed_index+2]
            p = False
            p0 = False
            p1 = False

            if tokens[parsed_index+1] == "Binary" and tokens[parsed_index+2] == "Binary":
                p = True
            if tokens[parsed_index+1] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p = True
            if tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p = True
            if tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p0 = True
                        if p0 and p1 == True:
                            p = True
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p1 = True
                        if p0 and p1 == True:
                            p = True
            if p == True:
                if not t0 == t1:
                    print("Xor: "+str(True))
                else:
                    print("Xor: "+str(False))
        elif token == "Xnor" and (tokens[parsed_index+1] == "Binary" or tokens[parsed_index+1] == "Declaration") and (tokens[parsed_index+2] == "Binary" or tokens[parsed_index+2] == "Declaration") and tokens[parsed_index+3] == "End_Line" and tokens[parsed_index-1] == "End_Line":
            t0 = words[parsed_index+1]
            t1 = words[parsed_index+2]
            p = False
            p0 = False
            p1 = False

            if tokens[parsed_index+1] == "Binary" and tokens[parsed_index+2] == "Binary":
                p = True
            if tokens[parsed_index+1] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p = True
            if tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p = True
            if tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p0 = True
                        if p0 and p1 == True:
                            p = True
                    if i["Name"] == words[parsed_index+2]:
                        t1 = i["Value"]

                        p1 = True
                        if p0 and p1 == True:
                            p = True
            if p == True:
                if t0 == t1:
                    print("Xnor: "+str(True))
                else:
                    print("Xnor: "+str(False))

        elif token == "Not" and (tokens[parsed_index+1] == "Binary" or tokens[parsed_index+1] == "Declaration") and tokens[parsed_index+2] == "End_Line" and tokens[parsed_index-1] == "End_Line":
            t0 = words[parsed_index+1]
            p = False

            if tokens[parsed_index+1] == "Binary" and tokens[parsed_index+2] == "Binary":
                p = True
            if tokens[parsed_index+1] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        t0 = i["Value"]

                        p = True
            if p == True:
                if t0 == "1":
                    print("Not: "+str(False))
                else:
                    print("Not: "+str(True))

        elif token == "Declarator" and tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Equal" and tokens[parsed_index+3] == "Binary" and tokens[parsed_index+4] == "End_Line":
            var = {"Name": None,
                   "Value": None}
            
            var["Name"] = words[parsed_index+1]
            var["Value"] = words[parsed_index+3]

            variables.append(var)
        
        elif token == "Reset" and tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "End_Line":
            
            for i in variables:
                if i["Name"] == words[parsed_index+1]:
                    variables.remove(i)
        
        elif token == "Declarator" and tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Equal" and tokens[parsed_index+3] == "Declaration" and tokens[parsed_index+4] == "End_Line":
            var = {"Name": None,
                "Value": None}

            var["Name"] = words[parsed_index+1]
            for i in variables:
                if i["Name"] == words[parsed_index+3]:
                    var["Value"] = i["Value"]
            
            variables.append(var)
        elif token == "Declarator" and tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Equal" and tokens[parsed_index+3] in gates and (tokens[parsed_index+4] == "Binary" or tokens[parsed_index+4] == "Declaration") and (tokens[parsed_index+5] == "Binary" or tokens[parsed_index+5] == "End_Line" or tokens[parsed_index+5] == "Declaration"):
            t0 = words[parsed_index+4]
            t1 = None
            p = False

            log_gate = ""

            if not t1 == "End_Line":
                t1 = words[parsed_index+5]
            
            var = {"Name": None,
                   "Value": None}
            
            var["Name"] = words[parsed_index+1]
            if tokens[parsed_index+3] == "And":
                if tokens[parsed_index+4] == "Declaration" or tokens[parsed_index+5] == "Declaration":
                    for i in variables:
                        if i["Name"] == words[parsed_index+4]:
                            t0 = i["Value"]

                            p = True
                            log_gate = "and"
                        if i["Name"] == words[parsed_index+5]:
                            t1 = i["Value"]

                            p = True
                            log_gate = "and"
                else:
                    p = True
                    log_gate = "and"
            elif tokens[parsed_index+3] == "Or":
                if tokens[parsed_index+4] == "Declaration" or tokens[parsed_index+5] == "Declaration":
                    for i in variables:
                        if i["Name"] == words[parsed_index+4]:
                            t0 = i["Value"]

                            p = True
                            log_gate = "or"
                        if i["Name"] == words[parsed_index+5]:
                            t1 = i["Value"]

                            p = True
                            log_gate = "or"
                else:
                    p = True
                    log_gate = "or"
            elif tokens[parsed_index+3] == "Nand":
                if tokens[parsed_index+4] == "Declaration" or tokens[parsed_index+5] == "Declaration":
                    for i in variables:
                        if i["Name"] == words[parsed_index+4]:
                            t0 = i["Value"]

                            p = True
                            log_gate = "nand"
                        if i["Name"] == words[parsed_index+5]:
                            t1 = i["Value"]

                            p = True
                            log_gate = "nand"
                else:
                    p = True
                    log_gate = "nand"
            elif tokens[parsed_index+3] == "Nor":
                if tokens[parsed_index+4] == "Declaration" or tokens[parsed_index+5] == "Declaration":
                    for i in variables:
                        if i["Name"] == words[parsed_index+4]:
                            t0 = i["Value"]

                            p = True
                            log_gate = "nor"
                        if i["Name"] == words[parsed_index+5]:
                            t1 = i["Value"]

                            p = True
                            log_gate = "nor"
                else:
                    p = True
                    log_gate = "nor"
            elif tokens[parsed_index+3] == "Xor":
                if tokens[parsed_index+4] == "Declaration" or tokens[parsed_index+5] == "Declaration":
                    for i in variables:
                        if i["Name"] == words[parsed_index+4]:
                            t0 = i["Value"]

                            p = True
                            log_gate = "xor"
                        if i["Name"] == words[parsed_index+5]:
                            t1 = i["Value"]

                            p = True
                            log_gate = "xor"
                else:
                    p = True
                    log_gate = "xor"
            elif tokens[parsed_index+3] == "Xnor":
                if tokens[parsed_index+4] == "Declaration" or tokens[parsed_index+5] == "Declaration":
                    for i in variables:
                        if i["Name"] == words[parsed_index+4]:
                            t0 = i["Value"]

                            p = True
                            log_gate = "xnor"
                        if i["Name"] == words[parsed_index+5]:
                            t1 = i["Value"]

                            p = True
                            log_gate = "xnor"
                else:
                    p = True
                    log_gate = "xnor"
            elif tokens[parsed_index+3] == "Not":
                if tokens[parsed_index+4] == "Declaration":
                    for i in variables:
                        if i["Name"] == words[parsed_index+4]:
                            t0 = i["Value"]

                            p = True
                            log_gate = "not"
                else:
                    p = True
                    log_gate = "not"
            
            if p == True and not log_gate == "":
                if log_gate == "and":
                    if t0 == "1" and t1 == "1":
                        var["Value"] = "1"
                    else:
                        var["Value"] = "0"
                elif log_gate == "or":
                    if t0 == "1" or t1 == "1":
                        var["Value"] = "1"
                    else:
                        var["Value"] = "0"
                elif log_gate == "nand":
                    if t0 == "0" or t1 == "0":
                        var["Value"] = "1"
                    else:
                        var["Value"] = "0"
                elif log_gate == "nor":
                    if t0 == "0" and t1 == "0":
                        var["Value"] = "1"
                    else:
                        var["Value"] = "0"
                elif log_gate == "xor":
                    if not t0 == t1:
                        var["Value"] = "1"
                    else:
                        var["Value"] = "0"
                elif log_gate == "xnor":
                    if t0 == t1:
                        var["Value"] = "1"
                    else:
                        var["Value"] = "0"
                elif log_gate == "not":
                    if t0 == "0":
                        var["Value"] = "1"
                    else:
                        var["Value"] = "0"

            variables.append(var)
        elif token == "Out" and (tokens[parsed_index+1] == "Binary" or tokens[parsed_index+1] == "Declaration") and tokens[parsed_index+2] == "End_Line":
            if tokens[parsed_index+1] == "Declaration":
                for i in variables:
                    if i["Name"] == words[parsed_index+1]:
                        print(i["Value"])
            else:
                print(words[parsed_index+1])

        parsed_index += 1

    #print(variables)
    
