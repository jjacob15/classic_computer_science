from dataclasses import dataclass

@dataclass
class CompressGene:
    def compress(self,gene:str)->int:
        self.bit_string:int = 1
        print(f"{bin(self.bit_string)} starting\n")
        for nucleotide in gene.upper():
            print(f"{bin(self.bit_string)} before\n")
            self.bit_string <<= 2 # shift left two bits
            print(f"{bin(self.bit_string)} after\n")
            if nucleotide  == 'A':
                self.bit_string |= 0b00
            elif nucleotide == "C": # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G": # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T": # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
            
            print(f"{bin(self.bit_string)} {nucleotide}\n")


    def decompress(self)->str:
        gene:str = ""
        for i in range(0, self.bit_string.bit_length() -1,2):
            print(f"{bin(self.bit_string >> i)} {bin(self.bit_string >> i & 0b11)}\n")
            bits: int = self.bit_string >> i & 0b11 
            if bits == 0b00 :
                gene += "A"
            elif bits == 0b01 :
                gene += "C"
            elif bits == 0b10 :
                gene += "G"
            elif bits == 0b11 :
                gene += "T"
            else:
                raise ValueError(f"Invalid bit :{bits}")
            
        return gene[::-1]
