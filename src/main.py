'''
PUT FILE DIRECTORY IN LINE 10
'''

errors = [
    "Error: Unable to Assign word to Token ( There is probably a misspelled keyword in the file )",
]

##### FILE READING #####
with open("", "r") as f:
    tokens = []
    words = []

    variables = []

    ######################### LEXER #########################

    for line in f:
        for word in line.split():
            word = word.upper()
            if word == "AND":
                tokens.append("And")
            elif word == "OR":
                tokens.append("Or")
            elif word == "NOT":
                tokens.append("Not")
            elif word in "01" or word[len(word)-2] in "01":
                tokens.append("Binary")
            elif word == "BIN":
                tokens.append("Declarator")
            elif word == "=":
                tokens.append("Equal")
            elif word in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" or word[:-1] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                tokens.append("Declaration")
            else:
                print(errors[0])
            
            if word == ";" or word[len(word)-1] == ";":
                tokens.append("End_Line")

            if not word[len(word)-1] == ";":
                words.append(word)
            else:
                words.append(word[0])
                words.append(";")

    #print(tokens)
    
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
        
        elif token == "Declarator" and tokens[parsed_index+1] == "Declaration" and tokens[parsed_index+2] == "Equal" and (tokens[parsed_index+3] == "And" or tokens[parsed_index+3] == "Or" or tokens[parsed_index+3] == "Not") and (tokens[parsed_index+4] == "Binary" or tokens[parsed_index+4] == "Declaration") and (tokens[parsed_index+5] == "Binary" or tokens[parsed_index+5] == "End_Line" or tokens[parsed_index+5] == "Declaration"):
            t0 = words[parsed_index+4]
            t1 = tokens[parsed_index+5]
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
                        print(t0+" "+t1)
                        print("And: "+str(True))
                        var["Value"] = "1"
                    else:
                        print(t0+" "+t1)
                        print("And: "+str(False))
                        var["Value"] = "0"
                elif log_gate == "or":
                    if t0 == "1" or t1 == "1":
                        print("Or: "+str(True))
                        var["Value"] = "1"
                    else:
                        print("Or: "+str(False))
                        var["Value"] = "0"
                elif log_gate == "not":
                    if t0 == "0":
                        print("Not: "+str(True))
                        var["Value"] = "1"
                    else:
                        print("Not: "+str(False))
                        var["Value"] = "0"

            variables.append(var)

        parsed_index += 1
    
