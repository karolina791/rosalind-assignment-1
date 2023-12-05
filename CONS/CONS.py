from Bio import SeqIO
import Bio.motifs 
from Bio.Seq import Seq

instances=[]

for record in SeqIO.parse("rosalind_cons3.txt", "fasta"):
    record=str(record.seq)
    record=record.strip('\\')
    record=record.strip('}')
    instances.append(Seq(record))
    
    
m=Bio.motifs.create(instances)    

A=str(m.counts["A"])
A=A.replace(',','')
A=A.strip('[')
A=A.strip(']')

C=str(m.counts["C"])
C=C.replace(',','')
C=C.strip('[')
C=C.strip(']')

G=str(m.counts["G"])
G=G.replace(',','')
G=G.strip('[')
G=G.strip(']')

T=str(m.counts["T"])
T=T.replace(',','')
T=T.strip('[')
T=T.strip(']')



print(m.consensus)
print('A: '+ A)
print('C: '+ C)
print('G: '+ G)
print('T: '+ T)