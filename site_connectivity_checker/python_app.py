# import urlib
# use urlib.request get the data from the url
# writte the funcation that takes url 
# return a response


import urllib.request as urllib



def main(url):
    print("Checking conenctivity: ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was: ", response.getcode())



print("This is a site connectivity checker program")
input_url = input("Input the url of the site: ")


main(input_url)