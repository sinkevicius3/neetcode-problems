class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + "," + string
            
        return encoded_str # 5,hello3,bye

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            comma_idx = s.find(",", i)
            str_len = int(s[i:comma_idx])
            result.append(s[comma_idx + 1:comma_idx + 1 + str_len])
            i = comma_idx + 1 + str_len

        return result