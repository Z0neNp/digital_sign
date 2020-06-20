def get_user_choice(user_choices, file_with_encrypted_message, file_with_plain_message):
  menu = f"{user_choices[0]}.\tGet message signature stored in {file_with_encrypted_message}"
  menu = menu + f"\n{user_choices[1]}.\tEncrypt message stored in {file_with_plain_message}"
  menu = menu + f"\n{user_choices[2]}.\tDecrypt message stored in {file_with_encrypted_message}"
  menu = menu + f"\n{user_choices[3]}.\tExit\n"
  print("What would you like to perform?")
  result = input(menu)
  try:
    result = int(result)
  except ValueError as err:
    err_msg = "You have entered an illegal option."
    err_msg = f"\nPlease enter a number in the range {user_choices}.\n"
    raise RuntimeError(err_msg)
  return result