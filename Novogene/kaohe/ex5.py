fp_in = open("5/test05.fsa","r")
fp_out = open("ex5_out.fsa","w")

s = ""
L = []


for eachline in fp_in:
    eachline = eachline.strip()
    
    if eachline.startswith(">"):
        l = eachline.split("|")
        genename = l[1]
    else:
        s = s + eachline
        
        if s.endswith("TAA") or s.endswith("TGA"):
            if len(s) % 3 == 0:
                length  = len(s) 
                num_str = "A:" + str(s.count("A")) + "/" + "T:" + str(s.count("T")) + "/" + "G:" + str(s.count("G")) + "/" "C:" + str(s.count("C")) + "\n"
                L.append(str(genename) + "\t" + str(length) + "\t" + num_str)
            else:
                pass
        else:
            pass
fp_out.writelines(L)


fp_in.close()
fp_out.close()     
    
