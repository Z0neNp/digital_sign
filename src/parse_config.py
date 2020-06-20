import json

def parse_config(config_location):
  err_msg = None
  
  config = None
  file_with_encrypted_message = None
  file_with_plain_message = None
  hash_ceil_value = None
  primary_first = None
  primary_second = None
  public_key = None
  
  try:
    config_file = open(config_location)
    config = json.load(config_file)
  except FileNotFoundError as err:
    err_msg = str(err)
  except json.decoder.JSONDecodeError as err:
    err_msg = str(err)
  finally:
    config_file.close()
  
  if config is None:
    raise RuntimeError(err_msg)

  try:
    file_with_encrypted_message = config["file_with_encrypted_message"]
    file_with_plain_message = config["file_with_plain_message"]
    hash_ceil_value = config["hash_ceil_value"]
    primary_first = config["primary_first"]
    primary_second = config["primary_second"]
    public_index = config["public_index"]
    n = config["N"]
  except KeyError as err:
    raise RuntimeError(str(err))

  if file_with_encrypted_message is None or not type(file_with_encrypted_message) is str \
    or not len(file_with_encrypted_message) > 0:
      err_msg = "Expected file location with encrypted message to be a none-empty String."
  
  if file_with_plain_message is None or not type(file_with_plain_message) is str \
    or not len(file_with_plain_message) > 0:
      err_msg = "Expected file location with plain message to be a none-empty String."
  
  if hash_ceil_value is None or not type(hash_ceil_value) is int \
    or not hash_ceil_value > 0:
      err_msg = "Expected hash max value to be a positive Integer."

  if not err_msg is None:
    raise RuntimeError(err_msg)

  return file_with_encrypted_message, file_with_plain_message, hash_ceil_value, \
    primary_first, primary_second, public_index, n