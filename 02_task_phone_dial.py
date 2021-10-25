class PhoneDial():
    """
    Class PhoneDial represents phone keyboard. You can call type method to get all the combinations.
    Please create the PhoneDial object and next call obj.type([string]) with a string containing
    number you would like to type.
    """
    def type(self, digits):
        if(len(digits) == 0): 
            return []  # return empty list for an empty digits string
        """the underscore character _ stands for space which is availble under '1' button"""
        alphabet = {1:"_",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        result = []  # for empty string return empty list
        self.solve(digits, alphabet, result)
        return result
    def solve(self, digits, alphabet, result, current_string="", current_level=0):
        if current_level == len(digits):
            """end the loop if the iteration is done"""  
            result.append(current_string)
            return
        for i in alphabet[int(digits[current_level])]:
            """Recursivly call the method to get all the combinations"""
            self.solve(digits,alphabet,result,current_string+i,current_level+1)

phone = PhoneDial()
print(phone.type('46'))