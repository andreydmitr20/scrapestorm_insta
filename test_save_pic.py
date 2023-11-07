import os
import random

PICTURES_PATH_PREFIX='./db_pics'
MAX_DIGITS_IN_PICTURE_NAME=5*3

def save_picture(pic_id:int,pic_ext:str)->str:
    pic_name=str(pic_id)
    pic_path=get_path_from_int_str(pic_name)

    # Create directory structure
    pic_path= os.path.join(PICTURES_PATH_PREFIX, 
                                       pic_path)
    os.makedirs(pic_path, exist_ok=True)

    pic_full_path=pic_path+pic_name+'.'+pic_ext
    with open(pic_full_path, 'w') as file:
        file.write("Image content goes here")

    return pic_full_path


def get_path_from_int_str(int_str:str)->str:
    """get_path_from_int_str"""
    int_str = int_str.zfill(MAX_DIGITS_IN_PICTURE_NAME)
    result=''
    for start_index in range(0,MAX_DIGITS_IN_PICTURE_NAME,3):
        result=result + int_str[start_index:start_index+3]+'/'
    return result

if __name__ == "__main__":
    for index in range(10):
        pic_id=random.randint(0, 999999999999999)
        print(f"Image {str(pic_id)} > {save_picture(pic_id,'jpg')}")
