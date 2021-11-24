def gc_content(data: str):
    """
    Calculates the GC content of a given DNA string
    :param data: the DNA string
    :return: the GC content of the DNA string

    Calculation done by adding the number of G and C nucleotides in the string and dividing by the total number of nucleotides
    and then multiplying by 100 for readability.
    """

    total_length = len(data)
    g_content = data.count("G")
    c_content = data.count("C")

    # Calculating the total GC content ( total number of G and C bases divided by the total length of the string )
    total_gc = ((g_content + c_content) / total_length)*100
    return total_gc


def read_gc_content(file_path: str):
    """
    Reads a file containing DNA strings and returns a dictionary of the GC content of each string
    :param file_path: path to the file containing the DNA strings
    :return: a dictionary of the GC content of each string
    """
    # Opens the file and reads the lines
    with open(f"{file_path}", "r") as file:

        # Creating dictionary for later use
        nucleotide_data = {}
        data_types = ("A", "T", "G", "C")
        file_lines = file.readlines()

        # Iterates over the lines in the file and sees if the line starts with an identifier or not
        for line in file_lines:
            # If the line is an identifier then it is added to the dictionary as a key to be later paired with a value
            if line.startswith(">"):
                # Strpping the new line character for a cleaner output
                fasta_id = line.strip("\n")
                nucleotide_data[fasta_id] = ""
            # If the line doesn't start with an identifier, it is read and added to the dictionary as the value to the fasta_id key
            elif line.startswith(data_types):
                # Used .update here instead of = becase the values of the DNA string were being overwritten, not appended
                nucleotide_data.update(
                    {fasta_id: nucleotide_data[fasta_id] + line.strip("\n")})

        # Creating a dictionary for the later GC content
        gc_content_dict = {}
        # Iterates over the items in the dictionary and calculates the GC content of each string
        for key, value in nucleotide_data.items():
            gc_content_dict[key] = gc_content(value)

        # Gets the highest GC content
        highest_gc = max(gc_content_dict.values())

        # Gets the ID of the string with the highest GC content
        highest_gc_id = [
            key for key, value in gc_content_dict.items() if value == highest_gc][0]

        # Strips the ">" for required output
        highest_gc_id = highest_gc_id.strip(">")

        # Printing the ID and the highest GC content
        print(f"{highest_gc_id}")
        print(f"{highest_gc}")
        file.close()

        return gc_content_dict


read_gc_content("ur path here ;)")
