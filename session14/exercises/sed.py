def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    
    with open(source, 'r') as f_r:
        with open(dest, 'w') as f_w:
            for line in f_r:
                new_line = line.replace(pattern, replace)
                f_w.write(new_line)
    # f_r.close() # not needed
    

#TODO: use regular expression or other way to particularly locate the word 'man'
pattern = " man"
replace = " woman"
source = "session14/output.txt"
dest = "session14/output2.txt"
sed(pattern, replace, source, dest)

