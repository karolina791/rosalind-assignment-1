sequence= "CTATGAACATGTAGCCGGCGGCAAGTGGCCTGCGAACGTTTTCGATGCAAAGGGTGCGACGACAAAGCATAATGGTGCGAGGGTAGGCTAACTGTGCGGGGGCATCATTTGTCTCGCAAGAAGCAGAGAGGCCGTGACGGTTGGCAGACTAACTCCCAAGTACAAGGGACGTAGTAAGCCGTTAACCCTTACGAGGGCTTTGCGGAGCTACTTGGACACTTGTTGGGGGCTACAAACTCTTCGGAGCTGAATGAGCTTGGGGTACATGTTAAAGTCAGAGCAATAAACCGTGCATTATAATCAGCTGGTTAATGGTGCCCGTGGTGGTCGTCAGCGAGCGCCTCTACCATTTGATTGCCGCCAAGGGCCGAAAGCAAGTAGAAGAAAAAACTTGGGGAGCATGGTAATGCTGAGGAGTCGAGCGGAACCACATGGGTCGGAATTCCGCCCGAAGCTCTGCAAAGGAAATGCAGCTGAATGGCTGGTTCACACTACTCCCATTCTCGGCGTTCGCATTACTCGGTGTTCGCTGGAGAGGCTACTGCAGTCCGACATTGGTTGGACGTTTAAGAAAGGGGACCGACGGTAGGCAAGTGTACCATTCTCCCCCAGGTCGTGAGTTAAGCCAGGCCGTTGAGCGCGTAGGAAACTAGCTGGCCTCTCTACTGTGGCCGACGTACTGGCCCCCCCAGGGTAGAACGGAAAGATAATGTTCGGCATTGACAGGGCTTTAATCCGACGAAGGCAGGATTAGGGGGGGGTTTTCAAGGCTTGCCACCTGGTCACTAGGATTTTGCAGAGTGGTCTCCAATGGGTAGTAGCTTGGAGCTAGTAATTGTATGGTGTTAAAGATCCAAACAGACAGCTCGACCCTAATCGTGAGACTATTTGGGTGTACCAAAGCGTGATCCACCAACTCCGGCACGCGGCCGTCGTACTCGGAG"
dict_count= {"A":0, "C":0, "G":0, "T":0}

for character in sequence:
    dict_count[character]=dict_count[character] + 1
    
print (dict_count)