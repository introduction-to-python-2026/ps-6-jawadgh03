def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()

    codon_dict = {}
    for row in rows:
        parts = row.strip().split('\t')
        codon = parts[0]
        aa_abbrev = parts[2]
        codon_dict[codon] = aa_abbrev

    return codon_dict

