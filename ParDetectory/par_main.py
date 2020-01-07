'''October 09, 2019
The purpose of this program is to detect duplicated paragraphs and to remove
the repetiativiness.
Author @Abinet Kenore
contributor @N/A
            @ N/A
'''
# import datetime
import time

crud_time = time.asctime(time.localtime(time.time()))
crud_msg = "Last time this file was modified: "
space = 40 * '-'


def crud_log():
    crud_par = open("Timelog.txt", "a")
    crud_par.write("\n" + space + "\n" + crud_msg + "\n" + crud_time)
    crud_par.close()


def par_write_to():   # fw, fr
    print("\n" + space)
    get_text = input(str("""Enter your text/ past it here  """))
    with open("textFile.txt", "a") as par:
        for line in open("original.txt"):
            if get_text in line:
                par.write(line)
                print("String exists in original.txt ")
            # else:
                # print("String doesn't exist in original.txt ")
        print("new text added to the textFile. ")
        par.write("\n" + get_text)
        par.close()
        print(space)


if __name__ == '__main__':
    par_write_to()
    crud_log()
    print("The code is rurning fine \n", (crud_time))
