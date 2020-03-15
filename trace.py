trace_file = open("out.tr","r+")
a = []
for line in trace_file:
    data = line.split() 
    for word in data:
        if (word=='-------'):
            for dash in word:
                a.append(dash)
        else:        
            #break
            a.append(word)
    print(a)
    break
