class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs==[]:
            return '\U0001f600'
        return "\U0001F606".join(strs)

    def decode(self, s: str) -> List[str]:

        if s=='\U0001f600':
            return []
        
        if s=='':
            return ['']
            
        return s.split('\U0001F606')