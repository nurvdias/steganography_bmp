from steganography import Steganography

#ToDo добавить работу с аргументами
#ToDo Проверить работу на всех файлах в архиве
#ToDo Написать ReadMe
if __name__ == "__main__":

    Steganography.encode_to_bmp("palm.bmp", "Jorj")
    Steganography.encode_to_bmp("palm.bmp", "LEHA")
    print(Steganography.decode_from_bmp("palm.bmp"))

    Steganography.delete_message_from_bmp('palm.bmp')
    print(Steganography.decode_from_bmp("palm.bmp"))
