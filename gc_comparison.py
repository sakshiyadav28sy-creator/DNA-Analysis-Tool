import matplotlib.pyplot as plt

# GC content function
def gc_content(dna):
    return (dna.count("G") + dna.count("C")) / len(dna) * 100

# Input
dna1 = input("Enter DNA sequence 1: ").upper()
dna2 = input("Enter DNA sequence 2: ").upper()

# Calculate GC
gc1 = gc_content(dna1)
gc2 = gc_content(dna2)

def find_orf(dna):
    start = "ATG"
    stops = ["TAA", "TAG", "TGA"]
    
    for i in range(len(dna)):
        codon = dna[i:i+3]
        if codon == start:
            for j in range(i, len(dna), 3):
                codon = dna[j:j+3]
                if codon in stops:
                    return dna[i:j+3]
    return "No ORF found"

print("GC Content of DNA 1:", gc1)
print("GC Content of DNA 2:", gc2)

orf1 = find_orf(dna1)
orf2 = find_orf(dna2)

codon_table = {
    "ATG": "M", "TTT": "F", "TTC": "F",
    "TAA": "*", "TAG": "*", "TGA": "*"
}

def translate(dna):
    protein = ""
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon in codon_table:
            if codon_table[codon] == "*":
                break
            protein += codon_table[codon]
    return protein

print("ORF in DNA 1:", orf1)
print("ORF in DNA 2:", orf2)

if orf1 != "No ORF found":
    print("Protein for DNA1:", translate(orf1))

if orf2 != "No ORF found":
    print("Protein for DNA2:", translate(orf2))

# Graph
plt.bar(["DNA1", "DNA2"], [gc1, gc2])
plt.title("GC Content Comparison")
plt.xlabel("Sequences")
plt.ylabel("GC %")
plt.show()


