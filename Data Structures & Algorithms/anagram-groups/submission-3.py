class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       count_char={}
       for word in strs:
            word_embed=[0]*26
            for char in word:
                index_char= ord(char)-ord('a')
                word_embed[index_char]+=1
            
            if tuple(word_embed) not in count_char:
                count_char[tuple(word_embed)]=[word]
            else:
                count_char[tuple(word_embed)].append(word)

       result=list(count_char.values())  
       return(result)

            
    

                
                
           
   
            
            
  