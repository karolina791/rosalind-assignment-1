from Bio import SeqIO
seq_list=[]
purines= ["A","G"]
pyrimidines=["T","C"]
transitions=0
transversions=0

for seq_record in SeqIO.parse('rosalind_tran.txt','fasta'):
     seq_list.append(str(seq_record.seq))
     
seq1= seq_list[0]
seq2=seq_list[1]
     
for i in range (len(seq1)):
    nuc1=seq1[i]
    nuc2=seq2[i]
    
    if nuc1!=nuc2:
        if nuc1 in purines and nuc2 in purines:
            transitions+=1
        elif nuc1 in pyrimidines and nuc2 in pyrimidines:
            transitions+=1
        else:
            transversions+=1
        
tran_ratio= transitions/transversions

print (tran_ratio)