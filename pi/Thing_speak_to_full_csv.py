import http.client, urllib.request, urllib.parse, urllib.error
from time import localtime, strftime
import json
import time
import csv
import struct

## REMEMBER!! - doit() is for a DRoP message - not a WeP (error message)
def stupid_shit_doit():
    
    #Declare the Message, Tag, and Date (month) dictionaries
    Message_Dictionary = {
        "TUP":0x02,
    }

    Tag_Dictionary = {
        'pH':0,
        'EC':1,
        "Water Level":2,
        "Light Validity":3,
        'Light Count':4,
        'Fluid Motion':5,
        'Env Temp':6,
    }

    Date_Dictionary = {
        1:'Jan',
        2:'Feb',
        3:'Mar',
        4:'Apr',
        5:'May',
        6:'Jun',
        7:'Jul',
        8:'Aug',
        9:'Sep',
        10:'Oct',
        11:'Nov',
        12:'Dec',

    }
    #This stuff is a little uncertain for me - Scott made this from ThingSpeak tutorials
    #The gist of it is the params encodes values to field no's and these get sent to the channel.

    data_from_website = urllib.request.urlopen("https://api.thingspeak.com/channels/732724/feeds.json?api_key=Q79JTILGZLQ92YKG&results=2")
    s = str(data_from_website.read())
    data_from_website.close()


    #This block removes all the unneccesary parts of the ThingSpeak json file.
    #Note: by splitting after entry_id:1, an error will occur if there are more than 
    #one entry. Please edit when pulling data for django server.
    # print(type(s))
    print(s)
    # j = s.split("\"entry_id\":1,")[1]
    # #str_field0 = j.split("field1\":\"")[1]
    # str_field1 = j.split("}")[0] #str_field0.split("}")[0]
    # print(j)
    # new_string = str_field1.replace("\"","")
    # new_string_list = new_string.split(',')
    # print(new_string_list)

    # #new string has a list with all the fields and their data
    # #its all in string types because that was the easiest way to cut it up/edit it, etc.
    # #new_string has the field<no>: still - needs to be removed before converting to hex

    # #messageID
    # messID_string = new_string_list[0].replace("field1:","")
    # messID_hold = Message_Dictionary[messID_string]
    # messID = "0x{:02x}".format(messID_hold)
    # print(messID_string)
    # print(messID)


    # #Planter Address
    # PA_string = new_string_list[1].replace("field2:","")
    # PA = "0x{:02x}".format(int(PA_string))
    # print(PA_string)
    # print(PA)

    # #Tag
    # Tag_string = new_string_list[2].replace("field3:","")
    # Tag_hold = Tag_Dictionary[Tag_string]
    # Tag = "0x{:02x}".format(int(Tag_hold))
    # print(Tag_string)
    # print(Tag)
    # print(type(Tag))

    # #Value
    # Value_string = new_string_list[3].replace("field4:","")
    # f = float(Value_string)
    # Value = hex(struct.unpack('<Q', struct.pack('<d', f))[0])
    # print(Value_string)
    # print(Value)
    # print(type(Value))

    # #format(int(hex_input1[34:36],16),'02')

    # Message_str = messID+PA[2:4]+Tag[2:4]+Value[2:]
    # print(Message_str)
    # print(type(Message_str))

    # #After a bunch of fun gymnastics, I made the string back into an int type (which using hex() can be read in hex notation)
    # #This int data type is what we should expect from the controller (i.e. a number, not a string)
    # Message = int(Message_str,16)
    # print(hex(Message))
    # print(type(Message))


stupid_shit_doit()