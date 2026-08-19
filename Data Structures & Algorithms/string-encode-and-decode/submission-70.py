class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            encode_str += str(len(s)) + "#" +s
                
        return encode_str


    def decode(self, s: str) -> List[str]:        
        decode_list = []
        index = 0

        while index < len(s):
            i = index
            while s[i] != "#":
                i+= 1

            length = int(s[index:i])
            decode_list.append(s[i+1:i+length+1])                        

            index = i + 1 + length

        
        return decode_list
