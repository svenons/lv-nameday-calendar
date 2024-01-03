import vobject

def read_contacts(file_path):
    contacts = []
    with open(file_path, 'r', encoding='utf-8') as file:
        vcard_data = file.read()
        vcard_list = vobject.readComponents(vcard_data)  # Read all vcard components
        for vcard in vcard_list:
            name_parts = []
            if hasattr(vcard.n, 'parts'):  # Check if 'parts' attribute exists
                for part in vcard.n.parts:  # Use the 'parts' attribute
                    name_parts.append(str(part))
            else:
                name_parts.extend(str(vcard.n).split())  # Split the 'Name' object into parts
            name = ', '.join(name_parts)
            if name.startswith('<N') and name.endswith('>'):
                name = name[3:-2]  # Remove the '<N' and '>' characters
            name = name.replace("}, ", "")  # Remove the character '}'
            name = name.replace("}", "")  # Remove the character '}'
            name = name[:name.rfind(",")]  # Remove the last comma
            if not name == '':
                contacts.append(name)
    return contacts
