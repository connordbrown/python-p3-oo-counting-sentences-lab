#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)

  def is_sentence(self):
    if self.value[-1] == '.':
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[-1] == '?':
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[-1] == '!':
      return True
    else:
      return False
  
  def count_sentences(self):
    new_str = self.value.replace('!', '.').replace('?', '.')
    sentences = new_str.split('.')
    sentences = [sentence.strip() for sentence in sentences if sentence != '']
    return len(sentences)
  
x = MyString("Hi!! I am a string. Are you?")
print(x.count_sentences())