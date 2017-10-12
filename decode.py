def decode(RNA):
  n=3
  x = [RNA [i:i+n] for i in range(0, len(RNA), n)] #splits them up into triplets
  for codon in x:
    print (proteinMade(codon)),  #comma makes it all on one line
    if (proteinMade(codon) == '.'): #This can be editted out if you want the entire thing transcoded. However in Vivo the a.a.'s would stop being added on at that point so it's important for accurracy in my opinion.
      break  #what actually stops the rest from being translated. Just # out this line and the one above and it works

#suggestion: Make it start at a methionine

def proteinMade(codon):  #self typed dictionary. Checks for combination and prints answer

    if (codon == 'UUU' or codon == 'UUC'):
        return ('F')
    elif (codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG'):
        return ('L')
    elif (codon == 'UUA' or codon == 'UUG'):
        return ('L')
    elif (codon == 'AUU' or codon == 'AUC' or codon == 'AUA'):
        return ('I')
    elif (codon == 'AUG'):
        return ('M')
    elif (codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG'):
        return ('V')
    elif (codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG') or codon == 'AGU' or codon == 'AGC':
        return ('S')
    elif (codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG'):
        return ('P')
    elif (codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG'):
        return ('T')
    elif (codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG'):
        return ('A')
    elif (codon == 'UAU' or codon == 'UAC'):
        return ('Y')
    elif (codon == 'UAA' or codon == 'UAG' or codon =='UGA'):
        return ('.')
    elif(codon == 'CAU' or codon == 'CAC'):
        return ('H')
    elif (codon == 'CAA' or codon == 'CAG'):
        return ('Q')
    elif (codon == 'AAU' or codon == 'AAC'):
        return ('N')
    elif (codon == 'AAA' or codon == 'AAG'):
       return ('K')
    elif(codon == 'GAU' or codon == 'GAC'):
        return ('D')
    elif (codon == 'GAA' or codon == 'GAG'):
        return ('E')
    elif (codon == 'UGU' or codon == 'UGC'):
        return ('C')
    elif (codon == 'UGG'):
        return ('W')
    elif (codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG'):
        return ('R')
    elif (codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG'):
        return ('L')

#Dictionary can also be used. Cleaner and much more simple. Code would be 10 lines. I wasn't sure if you wanted us to use premade dictionaries so I typed it all out for example see next line:
#codonDic = {'UUU' : 'F', 'CUU' :  'L', 'AUU' : 'I', 'GUU' : 'V', 'UUC' : 'F', 'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V', 'UUA' : 'L', 'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V', 'UUG' : 'L', 'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V', 'UCU' : 'S', 'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A', 'UCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A', 'UCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A', 'UCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A', 'UAU' : 'Y', 'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D', 'UAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D', 'UAA' : 'Stop', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'UAG' : 'Stop', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E', 'UGU' : 'C', 'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G', 'UGC' : 'C', 'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G', 'UGA' : 'Stop', 'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G', 'UGG' : 'W', 'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'}

RNA = 'ACAUAUGCGAAUAGCCGCAUGUACUAGUUA'   #actual rna sequence
decode(RNA) #calling the decode function to translate the RNA to protein
