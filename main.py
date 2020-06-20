#!/usr/bin/env python3
import json

from src.folding_hash.hash import FoldingHash
from src.rsa_encryption.rsa import RSA
from src.menu import get_user_choice
from src.parse_config import parse_config


error_msg_prefix = "digital_sign encountered an error"

file_with_encrypted_message = None
file_with_plain_message = None

encrypted_msg = None
hash_ceil_value = None
n = None
plain_msg = None
primary_first = None
primary_second = None
public_index = None

rsa_obj = None
sign_obj = None

user_choices = [1, 2, 3, 4]
user_choice = user_choices[0] - 1

try:
  file_with_encrypted_message, file_with_plain_message, hash_ceil_value,\
    primary_first, primary_second, public_index, n = parse_config("./config.json")
  
  while user_choice != user_choices[3]:
    
    try:
      user_choice = get_user_choice(
        user_choices,
        file_with_encrypted_message,
        file_with_plain_message
      )
    except RuntimeError as err:
      print(str(err))
    
    if user_choice == user_choices[0]:
      try:
        encrypted_msg_file = open(file_with_encrypted_message)
        encrypted_msg = encrypted_msg_file.read()
        encrypted_msg_file.close()
      except FileNotFoundError:
        raise RuntimeError(f"Expected the file {file_with_encrypted_message} to exist")
      
      sign_obj = FoldingHash.with_ceil_value(hash_ceil_value)
      print(f"The signature is {sign_obj.sign(encrypted_msg)}")
    
    elif user_choice == user_choices[1]:
      if primary_first is None or primary_second is None:
        err_msg = "Expected config.json to have values for primary_first, primary_second"
        err_msg = err_msg + " to encrypt a message"
        raise RuntimeError(err_msg)
      
      rsa_obj = RSA.with_primary_numbers(primary_first, primary_second)
      
      try:
        plaing_msg_file = open(file_with_plain_message)
        plain_msg = plaing_msg_file.read()
        plaing_msg_file.close()
      except FileNotFoundError as err:
        raise RuntimeError(f"Expected the file {file_with_plain_message} to exist.")
      
      encrypted_msg = rsa_obj.encrypt_msg(plain_msg)
      
      try:
        encrypted_msg_file = open(file_with_encrypted_message, "w")
        for n in encrypted_msg:
          encrypted_msg_file.write(f" {str(n)}")
        encrypted_msg_file.close()
      except FileNotFoundError as err:
        raise RuntimeError(f"Expected the file {file_with_encrypted_message} to exist.")  

      print(f"The encrypted msg has been stored in {file_with_encrypted_message}.")
      msg = "To decrypt the msg, insert into config.json"
      msg = msg + f"\n\t\"public_index\": \"{rsa_obj.public_key[0]}\""
      msg = msg + f"\n\t\"N\": \"{rsa_obj.public_key[1]}\""
      print(msg)
      break
    
    elif user_choice == user_choices[2]:
      if public_index is None or n is None:
        err_msg = "Expected config.json to have a value for"
        err_msg = err_msg + " public index and N to decrypt a message"
        raise RuntimeError(err_msg)

      rsa_obj = RSA.with_public_key((public_index, n))

      try:
        encrypted_msg_file = open(file_with_encrypted_message)
        encrypted_msg = encrypted_msg_file.read()
        encrypted_msg_file.close()
      except FileNotFoundError as err:
        raise RuntimeError(f"Expected the file {file_with_encrypted_message} to exist")
      
      try:
        encrypted_values = [int(n) for n in encrypted_msg.split(" ") if n != ""]
        decrypted_msg = rsa_obj.decrypt_msg(encrypted_values)
      except ValueError as err:
        err_msg = f"Expected {file_with_encrypted_message} to contain a List of Integers."
        raise RuntimeError(err_msg)
      
      try:
        plaing_msg_file = open(file_with_plain_message, "w")
        plaing_msg_file.write(str(decrypted_msg))
        plaing_msg_file.close()
      except FileNotFoundError as err:
        raise RuntimeError(f"Expected the file {file_with_plain_message} to exist")

      print(f"The decrypted msg has been stored in {file_with_plain_message}.")
      break
    
    elif user_choice == user_choices[3]:
      break
    
    else:
      print(f"Please pick a choice in the range {user_choices}.\n")

except RuntimeError as err:
  print(f"Digital Sign has failed.\n{str(err)}")