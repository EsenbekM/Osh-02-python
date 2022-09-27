import re

# text = 'AV Analytics Vidhya AV'
#
# result = re.match(r'AV', text)
# print(result)
#
# result = re.match(r'Analytics', text)
# print(result)
#
# result = re.search(r'Analytics', text)
# print(result)
#
# result = re.findall(r'AV', text)
# print(result)
#
#
# result = re.split(r' ', text)
# print(result)
#
#
# result = re.sub(r'a', r'o', text.lower())
# print(result)

with open("test_regs.txt", "r", encoding='utf-8') as file:
    content = file.read()
    # print(content)
    beeline = re.findall(r"\+996 (?:77[0-9]|22[0-9]) [0-9 ]{8}", content)
    print(beeline)

    nur_telecom = re.findall(r"\+996 (?:[75]0[0-9]) [0-9 ]{8}", content)
    print(nur_telecom)

    megacom = re.findall(r"\+996 (?:55[0-9]|99[0-9]|755) [ 0-9]{8}", content)
    print(megacom)
