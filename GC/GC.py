from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
list=[]
id_list=[]
    
for seq_record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    list.append(100*gc_fraction(seq_record))
    maxGC= max(list)
    position= list.index(maxGC)
    id_list.append(seq_record.id)
    
    
print (id_list[position])
print (maxGC)