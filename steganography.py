from crypter import Crypter
from converter import Converter


class Steganography:

    #ToDo Добавить возможность всавлять текст перед массивом пикселей (параметром)
    #ToDo Добавить проверку на то, что что-то уже закодировано и если да, то удалить прошлое сообщение (параметр)
    #ToDo Изменять размер файла при вставке сообщения
    @staticmethod
    def encode_to_bmp(file_name, message):
        f = open(file_name, 'ab')
        text_to_input = Steganography._convert_text_to_special_byte_arr_for_encode(
            message)
        f.write(text_to_input)
        f.close()

    @staticmethod
    def decode_from_bmp(file_name):
        f = open(file_name, 'rb')
        file_size = len(f.read())
        f.seek(file_size - 4)

        arr_size = Converter.bytes_to_int(f.read())
        f.seek(file_size - arr_size)
        resut_arr = f.read()
        f.close()
        return Steganography._convert_special_byte_arr_to_text(resut_arr)

    @staticmethod
    def _convert_text_to_special_byte_arr_for_encode(input_text):
        encoded_text = Crypter.encode_text(input_text).encode("UTF-8")
        text_hashcode = Crypter.get_MD5_hash(input_text).encode(
            "UTF-8")
        result_arr_length = Converter.int_to_bytes(
            len(encoded_text) + len(text_hashcode) + 4, 4)
        return encoded_text + text_hashcode + result_arr_length

    @staticmethod
    def _convert_special_byte_arr_to_text(byte_arr):
        text_hash = byte_arr[-36:-4].decode("UTF-8")
        encoded_text = byte_arr[:-36].decode("UTF-8")
        text = Crypter.decode_text(encoded_text)
        hash_of_encoded_text = Crypter.get_MD5_hash(text)

        if (hash_of_encoded_text != text_hash):
            raise Exception("Нарушена целостность данных")

        return Crypter.decode_text(encoded_text)
