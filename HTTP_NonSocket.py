#!/usr/bin/python3

# Status codes are grouped into the following classes:
#  [+] -->   Code 100-199: Informational Responses
#  [+] -->   Code 200-299: Successful Responses
#  [+] -->   Code 300-399: Redirects
#  [+] -->   Code 400-499: Client Errors
#  [+] -->   Code 500-599: Server Errors
#   input('[?]Enter the scheme for URL creation: ')
#   input('[?]Enter the Sub-Domain for URL creation: ')
#   input('[?]Enter the Domain for URL creation: ')
#   input('[?]Enter the Top-Level Domain for URL creation: ')
#   input('[?]Enter the Port for URL creation: ')
#   input('[?]Enter the Path for URL creation: ')
#   input('[?]Enter the Query-String for URL creation: ')
#   input('[?]Enter the Fragment for URL creation: ')

# ExmUrl:  {[(https/http/ftp]://).{www}         .{google}       .{(co.in).(com).(net)}:{1-65535} /{/root/.ssh/rsa_id}         {?}            {acctID=535&hl=en}{#dayone}
# url =    '{<Scheme>}://       .[{<subdomain>}.{<Domain Addr>}.{<Top level domain>}  : {<Port>}]/{<Path>}           {query string separator}{Query String}    {fragment}                   parameter}{<anchor>}'
# url = {<IP>}:{<Port>} 

import requests
  
url = 'http://192.168.185.68:8080/about.html'
server_response = requests.get(url)
flag = str()
choice = input('Enter the type of request to be made to the web server ? \t\t\n [?] Get Content[C] \t\t\n [?] Get Status_Code[S] \t\t\n [?] Get Server Header[H] \t\t\n [?] Get Server Response[T] \n\n Enter your choice: ').strip()

try:
    try:
        if choice:
            if choice == 'C' or choice == 'c':
                # for i in range(50):
                #     uri = url.format(i)
                #     server_response = requests.get(uri)
                #     # For Web content of target URL / WebServer / IP
                    print(server_response.content)
                    # x = server_response.content.decode().strip('\n')
                    # if len(x) != 0:
                    #     flag += x
            elif choice == 'S' or choice == 's':
                # For status code of target URL / WebServer / IP
                print(server_response.status_code)
            elif choice == 'H' or choice == 'h':
                # For Web Headers of the URL / WebServer / IP
                print(server_response.headers)
            elif choice == 'T' or choice == 't':
                # For Server Response of the URL / WebServer / IP
                print(server_response.text)
        else:
            choice = ('Choice not specifed, do you want to run the default request \n Default Requset is "Get Content" [Y/N]: ').strip()
            if choice == 'Y' or choice == 'y':
                print('\t\t[*]Getting the Web content of the %s\n\n: ' %url)
                print(server_response.content.decode())
            else:
                raise KeyboardInterrupt
    except ConnectionRefusedError:
        print('[!]Connection refused by WebServer.')
except KeyboardInterrupt:
    print('[**]Requestor Abort[**]')

print(flag)