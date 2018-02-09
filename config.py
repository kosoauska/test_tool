import  configparser
import  sys

class   config_class():
    def  __init__(self, path = r".\config\serial_conf.ini"):
        self.config_file = path
        self.config_handler = configparser.ConfigParser()
        self.config_handler.read(self.config_file)
############################################   section operator   #####################################################
# list section
    def list_section(self):
        return self.config_handler.sections()

# add section
    def add_section(self, section):
        try:
            self.config_handler.add_section(section)
        except Exception as e:
            print("add_section except = %s " % e)
            return False
        else:
            return True

# check section
    def have_section(self , section):
        return self.config_handler.has_section(section)

# remove section
    def rm_section(self , section):
        try:
            self.config_handler.remove_section(section)
        except Exception as e:
            print("rm_section except = %s " % e)
        else:
            self.config_handler.write(open(self.config_file , "w"))

    def get_section_number(self):
        return len(self.list_section())

# clear all section
    def clear_sections(self):
        for i in self.list_section():
            self.rm_section(i)

############################################   option operator   #####################################################
# get select section and option value(string)
    def get(self , section , option):
        return self.config_handler.get(section , option)

# set select section and option value
    def set(self , section , option , value) :
        self.config_handler.set(section , option , value)
        self.config_handler.write(open(self.config_file , "w"))

    def get_all(self , section):
        return self.config_handler.items(section)

# get select section and option value(int)
    def getint(self, section, option):
        return self.config_handler.getint(section , option)

    def __del__(self):
        del self.config_handler


if __name__ == '__main__':
    print("hello config parser \n")
    config_test = config_class()
    config_test.add_section("COM1")
    print(config_test.list_section())
    print(config_test.get_section_number())
    config_test.set("COM1" , "COM" , "COM1")
    config_test.set("COM1" , "Boud" , "38400")
    config_test.set("COM1" , "data" , "8")
    config_test.set("COM1" , "stop" , "1")
    config_test.set("COM1" , "pair" , "None")
    config_test.set("COM1" , "BC" , "WHITE")
    config_test.set("COM1" , "FC" , "BLACK")

