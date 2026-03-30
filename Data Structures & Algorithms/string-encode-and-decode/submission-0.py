class Solution:

    def encode(self, strs: List[str]) -> str:        
          str_enc=""
          for s in strs:
            str_enc+= str(len(s))+"#"+s
          return str_enc
    def decode(self, s: str) -> List[str]:
            res=[]
            i = 0
            while i < len(s):
                j = s.find("#", i)
                length = int(s[i:j])
                res.append(s[j+1 : j+1+length])
                i = j + 1 + length
                    
            return res