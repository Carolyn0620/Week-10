"""
Make this a function:
Input values: num_for_loops, lines, filename
Output value: num_while_loops
(NB: "Output" doesn't mean "stuff we print")
"""

def main():
    """
    Main function. Read file. Count required attributes
    :return:
    """
    filename = input("Enter program filename: ")
    lines = open(filename).readlines()

    count_for_loops(filename, lines)
    count_while_loops(filename, lines)
    count_if_loops(filename, lines)
    
# count for loops     
def count_for_loops(filename, lines):
    num_for_loops = sum(1 for line in lines if line.strip().startswith("for"))
    print(f"Program {filename} contain {num_for_loops} for loops")

# count for loops  
def count_while_loops(filename, lines):
    num_while_loops = sum(1 for line in lines if line.strip().startswith("while"))
    print(f"Program {filename} contain {num_while_loops} for loops")

# count for loops  
def count_if_loops(filename, lines):
    num_if_loops = 0
    for line in lines:
        if line.strip().startswith("if"):
            num_if_loops += 1

    print(f"Program {filename} contain {num_if_loops} for loops")


main()