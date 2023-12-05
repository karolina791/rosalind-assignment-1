from Bio import SeqIO

seq_list=[]
common_string=''
common_string1=''

for seq_record in SeqIO.parse('rosalind_lcsm.txt', 'fasta'):
    seq_list.append(seq_record.seq)
     


for i in range(len(seq_list[0])):
    
        for j in range(i, len(seq_list[0])):
            common_string=((seq_list[0])[i:j])
            
            for k in range (len(seq_list)):
                
                if (k + 1==len(seq_list) and len(common_string1)<len(common_string)):
                    common_string1 = common_string
                    
                elif common_string not in seq_list[k]:
                    break
        
print (common_string1)