class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = [first]
        while encoded:
            num = abs(encoded[0] ^ first)
            output.append(num) 
            encoded = encoded[1:]   
            first = num
        return output  
