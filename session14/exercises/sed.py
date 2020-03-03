def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    pass
    

pattern = " man "
replace = " woman "
source = "session14/output.txt"
dest = "session14/output2.txt"
sed(pattern, replace, source, dest)

